from django.urls import path

from .views import index, post_add


app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('post_add/', post_add, name='post_add')
]
