from django.urls import path, re_path
from Api import views

urlpatterns_Test = [
    path('test/', views.UserApi.Test.as_view(), name ='test'),
]