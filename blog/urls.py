from django.urls import path,include
from . import views

app_name = 'blog_url'
urlpatterns = [
    path('',views.profile_list(),name='profile_list')
]
