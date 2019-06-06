from django.conf.urls import url, include
from django.urls import include, path
from . import views as core_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('profile/', core_views.profile, name='profile_index'),
    path('profile/edit/', login_required(core_views.UpdateProfile.as_view()), name='profile_edit'),
    path('profile/edit/regions/', login_required(core_views.UpdateProfiler.as_view()), name='profile_edit_regions'),
    path('profile/edit/specialisation/', login_required(core_views.UpdateProfiles.as_view()), name='profile_edit_spec'),
    path('notify/', login_required(core_views.index_notify), name='notify_index'),
    path('verify/', core_views.verify,name='verify'),
]
