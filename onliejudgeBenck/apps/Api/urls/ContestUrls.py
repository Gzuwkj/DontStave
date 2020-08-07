from django.urls import path, re_path
from Api import views

urlpatterns_Contest = [
    path('contest', views.ContestApi.GetContestPage.as_view(), name='contests'),
    path('contest/<int:match_id>', views.ContestShowContent.as_view(), name='contestContent'),
    path('contest/<int:match_id>/problem', views.ContestGetProblems.as_view()),
    path('contest/<int:match_id>/problem/<int:problem_id>',
         views.ContestProblemPage.as_view(), name='contestProblemPage'),
    path('contest/<int:match_id>/submit', views.ContestGetStatus.as_view(), name='contestContentStatus'),
    path('contest/<int:match_id>/code/<int:run_id>', views.GetContestSubmitCode.as_view()),
    path('contest/<int:match_id>/rank', views.ContestGetRank.as_view(), name='contestContentRanks'),

    # re_path(r'^contest/problems/(?P<match_id>\d+)/$', views.ContestShowContent.as_view(), name='contest_pro'),
    path('test/', views.UserApi.Test.as_view(), name ='test'),
]