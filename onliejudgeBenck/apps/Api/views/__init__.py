from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .UserApi import *
from .IssueApi import *
from .ContestApi import *

# Create your views here.


def Api(request):
    if request.method == "POST":
        return JsonResponse({'msg': 'post'})
    if request.method == "GET":
        return JsonResponse({'msg': 'get'})

