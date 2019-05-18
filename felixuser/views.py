from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from felixuser.forms import *
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from .models import Profile
from catalog.models import Count
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
    count=Count.objects.get(profile=request.user)
    return render(request, 'felixuser/profile.html',{'count':count})
