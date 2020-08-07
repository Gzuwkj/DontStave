from django.urls import path, re_path
from mytest import views

urlpatterns = [
    path('bk1/', views.bk1, name='book1'),
    path('bk2/<x>/', views.bk2, name='book2'),
    re_path('bk3/(?P<num>\d+)/', views.bk3, name='book3'),
    path('bk4/', views.bk4.as_view(), name='book4'),

    path('au1/', views.au1, name='auth1'),
    path('au2/', views.au2, name='auth2'),
    path('au3/', views.au3, name='auth3'),

    path('problem/', views.creatproblem),
    path('problemsubmit/', views.creatproblemsubmit),
    path('matchinclude/', views.creatcontestinclude),
]