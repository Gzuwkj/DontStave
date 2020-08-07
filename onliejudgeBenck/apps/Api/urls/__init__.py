from django.urls import path, re_path
from Api import views
from .TestUrls import urlpatterns_Test
from .ContestUrls import urlpatterns_Contest
from .IssueUrls import urlpatterns_Issue
from .UserUrls import urlpatterns_User

urlpatterns = [
    path('', views.Api, name='api'),
] + urlpatterns_Test \
  + urlpatterns_Contest \
  + urlpatterns_Issue \
  + urlpatterns_User