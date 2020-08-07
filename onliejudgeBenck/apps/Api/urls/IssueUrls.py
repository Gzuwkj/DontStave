from django.urls import path, re_path
from Api import views

urlpatterns_Issue = [

    path('problem', views.IssueApi.GetProblemPage.as_view(), name='problem_page'),
    path('problem/<int:problem_id>', views.IssueApi.GetProblem.as_view()),

    path('status', views.IssueApi.GetProblemSubmitPage.as_view(), name ='problemsubmit_page'),
    path('issue/problemsubmit', views.IssueApi.GetProblemSubmit.as_view(), name ='problemsubmit'),
]