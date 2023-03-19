from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('navbar',views.navbar,name='navbar'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('account',views.account,name='account'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    #content
    path('What-is-Quantum-Computing',views.quantumcom,name='quantumcom'),
    path('What-is-Cloud-Computing',views.cloudcom,name='cloudcom'),
    path('ChatGPT-AI-tool',views.chatgpt,name='chatgpt'),
    path('Future-of-Artificial-Intelligence',views.ai,name='ai'),
    path('Starlink-Satellite-explain',views.starlink,name='starlink'),
    path('Augmented-Reality',views.augmented_r,name='augmented_r'),
    path("The-Bard-Google's-AI-Tool",views.bard,name='bard'),

    

]