from datetime import datetime
import random

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

# Create your views here.
from django.urls import reverse
from rest_framework.views import APIView

from Contest.models import *
from Contest.serializers import *
from Issue.serializers import *
from UserProfile.serializers import UserSerializer
from UserProfile.util import check_auth
from mytest.serializers import *
from .models import *
from Issue.models import *




def bk1(request):
    bookList = book.objects.all()
    paginator = Paginator(bookList, 5)
    page = paginator.page(1)
    print(type(paginator))
    print(type(page))
    print(page)
    page_concent = page.object_list
    print(type(page_concent))
    print(page_concent)
    book_serializers = bookSerializer(page_concent, many = True)
    print(book_serializers.data)
    for bk in book_serializers.data:
        print(bk)
    return JsonResponse({"ok":book_serializers.data})


def bk2(request, x):
    s1 = "xx"
    s2 = "yy"
    s = "bk2 %s" % x
    a = request.POST.get('m')
    print(a)
    return HttpResponse(s)


def bk3(request, num):
    s = dict({'num2':num}, {'num1':2})
    print(s)
    return HttpResponse(s)





class bk4(APIView):
    def get(self, request):
        data = {"ok":"xx"}
        a = {"username":"xz", "password":"123321", "major":"jk"}

        user = UserSerializer(data = a)
        if user.is_valid():
            print("yyyy")
        else:
            print("xxxx")
        return JsonResponse(data)
    def post(self, request):
        # problem = Problem.objects.get(no = 1000)
        # match = Match.objects.get(id = 1)
        # user = User.objects.get(username = "yiuyh")
        # ms = MatchSubmit()
        # ms.match = match
        # ms.problem = problem
        # ms.user = user
        # ms.save()
        # matchInclude = MatchInclude()
        # matchInclude.problem = problem
        # matchInclude.match = match
        # matchInclude.save()


        return JsonResponse(request.POST)

def au1(request):
    bk = book.objects.get(id = request.GET["id"])
    for i  in range(1,10):
        au = Auth()
        au.bk = bk
        au.name = "au"+str(i)
        au.save()
    return HttpResponse("ok")

def au2(request):
    bk = book.objects.get(id = request.GET["id"])
    bk_s = bookSerializer(bk)
    au = bk.auth_set
    au_s = AuthSerializer(au, many = True)
    return JsonResponse({"ok":au_s.data, "bk":bk_s.data})
    # return  HttpResponse("ok")

def au3(request):

    return JsonResponse({"ok":""})
    # return  HttpResponse("ok")

def creatproblem(request):
    for i in range(1011, 1015):
        problem = Problem()
        problem.probAuthority = '私有'
        problem.no = i
        problem.title = "di" + str(problem.no)
        problem.save()
    return HttpResponse("ok")


def creatproblemsubmit(request):
    user = User.objects.get(username="yiuyh")
    p = Problem.objects.all()
    for pp in p:
        ps = ProblemSubmit()
        ps.user = user
        ps.problem = pp
        ps.save()
    return HttpResponse("ok")

def creatcontestinclude(request):
    m = Match.objects.get(id = 1)
    p = Problem.objects.get(no = request.GET.get("no"))

    mi = MatchInclude()

    mi.match = m
    mi.problem = p
    mi.save()
    return HttpResponse("ok")