from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.response import Response
from apps.UserProfile.util import *
from apps.UserProfile.serializers import *
import re
from .Teacher import *
from .Administrator import *
from rest_framework.views import APIView
from apps.util import get_data


# 获取用户信息或修改用户信息(登录用户)
class UserOwn(APIView):
    def get(self, request):
        print("xxxxxx")
        is_login, user = check_auth(request._request) # 获取登录的用户
        data = {'status': 200, 'msg': '成功获取用户信息','data':{}}
        if is_login:
            data['data'] = get_data(obj=user, serializers=UserSerializer)
        else:
            data['msg'] = '未登录'
            data['status'] = 400
        return JsonResponse(data=data)

    def post(self, request):
        is_login, user = check_auth(request._request)  # 获取登录的用户
        data = {'status': 200, 'msg': '修改成功', 'data': {}}
        if is_login:
            user.updata_user(request.data)
        else:
            data['msg'] = '用户不存在'
            data['status'] = 400

        return JsonResponse(data=data)


class UserInfo(APIView):
    @staticmethod
    def get(request, id):
        data = {'status': 200, 'msg': '成功获取用户信息'}
        try:
            user = User.objects.get(id=id)
            dataList = ["nickname", "GENDER_CHOICE", "school", "major", "headImage", "synopsis", "rating", "ac_nums"]
            data['user'] = get_data(obj=user, serializer=UserSerializer, dataList=dataList)
        except:
            data['msg'] = '用户不存在'
            data['status'] = 400
        return JsonResponse(data=data)


# 获取他人用户信息
class UserOther(APIView):
    def get(self, request, username):
        data = {'status': 200, 'msg': '成功获取用户信息', 'data': {}}
        try:
            user = User.objects.get(username=username)  # 获取不到会抛异常
            dataList = ["nickname", "GENDER_CHOICE", "school", "major", "headImage", "synopsis", "rating", "ac_nums"]
            data['data'] = get_data(obj = user, serializer=UserSerializer, dataList=dataList)
        except:
            data['msg'] = '用户不存在'
            data['status'] = 400
        return JsonResponse(data=data)


# 获取token列表
# class Tokens(View):
#     def get(self, request):
#         tokenList = UserToken.objects.all()
#         userTokenSerializer = UserTokenSerializer(tokenList, many=True)
#         data = {
#             'msg': '已获取所有用户的Token',
#             'data': userTokenSerializer.data
#         }
#         return JsonResponse(data=data)


# 注册
class Register(APIView):
    @staticmethod
    def post(request):
        data = {'status': 200, 'msg': '注册成功', 'data': {}}  # 返回信息
        userPassword = request.data['password']
        userRepassword = request.data['repassword']
        userUsername = request.data['username']

        if userPassword != userRepassword: # 判断密码与确认密码是否相同
            data['status'] = 400  # 400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误
            data['msg'] = '重复密码错误'
            return JsonResponse(data=data)
        elif not re.search(r'^[a-zA-Z_]\w{4,15}$', userUsername):
            # 判断用户名是否合法
            data['status'] = 400
            data['msg'] = '用户名只能包含字母数字下划线，不能以数字起头,长度不少于5'
        elif not re.search(r'^[0-9a-zA-Z]{8,16}$', userPassword):
            # 判断密码是否合法
            data['status'] = 400
            data['msg'] = '密码由8-16位数字字母组成'
        elif User.objects.filter(username=userUsername).exists():
            # 判断用户名是否已经存在
            data['status'] = 400
            data['msg'] = '用户名已存在'
        else:
            # 反序列化
            userSerializer = UserSerializer(data=request.data)
            # 判断合法
            if userSerializer.is_valid():
                userSerializer, user = userSerializer.create(userPassword)
                # 生成token
                userJwt = jwt_response_payload_handler(user, request._request)
                # 创建UserToken
                # userToken = UserToken(user=user, token=userJwt['token'])
                # userToken.save()
                data['data'] = userJwt
        return JsonResponse(data=data)

    def get(self, request):
        return HttpResponse("ok")


# 登录
class Login(APIView):
    @staticmethod
    def post(request):
        data = {'status': 200, 'msg': '登录成功'}  # 返回信息
        username = request.data['username']
        password = request.data['password']
        if User.objects.filter(username=username).exists():
            # Django内部的User认证系统
            user = authenticate(username=username, password=password)
            if user:
                # 生成token
                userJwt = jwt_response_payload_handler(user, request)
                # 修改token
                # user.change_token(userJwt['token'])
                data.update(userJwt)
            else:
                data['status'] = 400
                data['msg'] = '密码错误'
        else:
            data['status'] = 400
            data['msg'] = '该用户名不存在'
        return Response(data)


class Authenticate(APIView):
    @staticmethod
    def get(request):
        is_login, user = check_auth(request)  # 获取登录的用户
        return JsonResponse({
            'is_login': is_login,
            'user': get_data(obj=user, serializer=UserSerializer, context={'request':request}),
            'status': 200
        })


class Test(APIView):
    def get(self, request):
        # users = User.objects.all()
        # user_serializer = UserSerializer(users, many=True)
        #
        # return JsonResponse(user_serializer.data, safe=False)
        data = {"ok": "xx"}
        return JsonResponse(data)

    def post(self, request):
        # User.objects.create(**request.data)
        User.objects.create(username = request.data['username'],
                            password = request.data['password']
                            )
        # username = request.data['username']
        # user = User.objects.filter(username = username)
        # print(type(user))
        # user = user.first()
        # print(type(user))
        # usertoken = user.usertoken
        # print(usertoken.token)
        # usertoken_serializer = UserTokenSerializer(usertoken)
        # user_serializer = UserSerializer(user)
        return JsonResponse({'data1':request.data})


