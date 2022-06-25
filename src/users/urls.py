from django.urls import path

from .views import profile, profile_change


app_name = 'users'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/change/', profile_change, name='profile_change'),
]
