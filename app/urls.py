from django.urls import path
from app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.signup.as_view(),name='signup')
]