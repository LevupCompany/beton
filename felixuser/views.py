from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse_lazy
from felixuser.forms import *
from felixuser.models import SmsVerify
import random
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from .models import Profile,Notification
from catalog.models import Count
from product.models import Tariff
from .smsc_api import *
def verify(request):
    if request.POST.get("param2"):
        param2 = request.POST.get('param2', None)
        rd = random.randint(10000,99999)
        smsc = SMSC()
        r = smsc.send_sms("%s" %param2, "Ваш пароль для входа: %s" %rd, sender="sms")
        if r[1] > "0":
            try:
                verify = SmsVerify.objects.get(number=param2)
                verify.number=param2
                verify.code=rd
                verify.save()
            except SmsVerify.DoesNotExist:
                SmsVerify.objects.create(number=param2,code=rd)
            return render(request,'felixuser/checkphone.html')
        else:
            l = r[1][1:]
            if l == "7":
                return HttpResponse('<span class="offset-md-5 col-md-7 font-weight-bold text-danger">Неверный номер</span>')
            elif l == "8":
                return HttpResponse('<span class="offset-md-5 col-md-7 font-weight-bold text-danger">Получение смс заблокировано</span>')
            elif l == "4":
                return HttpResponse('<span class="offset-md-5 col-md-7 font-weight-bold text-danger">Ваш ip адрес заблокирован на 60 минут</span>')
    if request.POST.get("param_checker"):
        param2_check = request.POST.get('param_check', None)
        param2_checker = request.POST.get('param_checker', None)
        try:
            SmsVerify.objects.get(number=param2_check,code=param2_checker)
            return HttpResponse('<span class="offset-md-5 col-md-7 font-weight-bold text-success">Верифицирован</span><input type="hidden" name="verificate" value=1/>')
        except SmsVerify.DoesNotExist:
            return render(request,'felixuser/checkphone.html',{'r':'Неправильный код'})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.company = form.cleaned_data.get('company')
            user.profile.identificate = form.cleaned_data.get('identificate')
            user.profile.director = form.cleaned_data.get('director')
            user.profile.site = form.cleaned_data.get('site')
            user.profile.manager = form.cleaned_data.get('manager')
            user.profile.image = form.cleaned_data.get('image')
            user.profile.logo = form.cleaned_data.get('logo')
            user.profile.admin = form.cleaned_data.get('admin')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.street = form.cleaned_data.get('street')
            user.profile.street2 = form.cleaned_data.get('street2')
            user.profile.specialisation.set(form.cleaned_data.get('specialisation'))
            user.profile.regions.set(form.cleaned_data.get('regions'))
            user.save()
            raw_password = form.cleaned_data.get('password1')
            c = Count(profile=user)
            c.save()
            t = Tariff(user=user.profile)
            t.save()
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile_index')
    else:
        form = SignUpForm()
    return render(request, 'felixuser/signup.html', {'form': form})

class UpdateProfile(UpdateView):
     template_name = 'felixuser/signup.html'
     form_class = EditProfile
     model = Profile
     success_url = reverse_lazy('profile_index')
     def get_object(self, queryset=None,):
         '''This loads the profile of the currently logged in user'''

         return Profile.objects.get(user=self.request.user)

     def form_valid(self, form):
         '''Here is where you set the user for the new profile'''

         instance = form.instance # This is the new object being saved
         instance.user = self.request.user
         instance.save()

         return super(UpdateProfile, self).form_valid(form)
class UpdateProfiler(UpdateView):
     template_name = 'felixuser/signup.html'
     form_class = EditRegions
     model = Profile
     success_url = reverse_lazy('profile_index')
     def get_object(self, queryset=None,):
         '''This loads the profile of the currently logged in user'''

         return Profile.objects.get(user=self.request.user)

     def form_valid(self, form):
         '''Here is where you set the user for the new profile'''

         instance = form.instance # This is the new object being saved
         instance.user = self.request.user
         instance.save()

         return super(UpdateProfiler, self).form_valid(form)
class UpdateProfiles(UpdateView):
     template_name = 'felixuser/signup.html'
     form_class = EditSpec
     model = Profile
     success_url = reverse_lazy('profile_index')
     def get_object(self, queryset=None,):
         '''This loads the profile of the currently logged in user'''
         return Profile.objects.get(user=self.request.user)
     def form_valid(self, form):
         instance = form.instance # This is the new object being saved
         instance.user = self.request.user
         instance.save()

         return super(UpdateProfiles, self).form_valid(form)
@login_required
def profile(request):
    count=Count.objects.get(profile=request.user.id)
    return render(request, 'felixuser/profile.html',{'count':count})
def index_notify(request):
    notify = Notification.objects.all()
    if  request.user.is_authenticated:
        e=Profile.objects.get(user=request.user)
        check_user = [notify for notify in Notification.objects.exclude(zones=request.user.id)]
        e.read.set(check_user)
        e.save()
    return render(request, 'product/notify.html',{'notify':notify})