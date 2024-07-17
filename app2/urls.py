
from django.urls import path

from app2 import views

urlpatterns = [
    path('',views.index,name='home'),
    path('feature',views.feature,name='feature'),
    path('services',views.services,name='services'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
]
