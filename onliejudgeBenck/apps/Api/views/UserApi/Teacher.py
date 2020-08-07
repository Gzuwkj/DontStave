#获取用户列表
import re

from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.views import APIView

from UserProfile.serializers import UserSerializer
from apps.util import get_data

from UserProfile.models import User


class UsersList(APIView):
    def get(self, request):
        data = {'status': 200, 'msg': '获取成功', 'data': {}} #返回集

        #权限验证 待添加

        submit_Username = request.GET.get("submit_Username", "")
        submit_User_Id = request.GET.get("submit_User_Id", "")

        query_Criteria = {} #查询集

        #用户列表筛选条件  两个都没有则为查询所有用户列表
        if submit_Username != '':
            query_Criteria['username__iregex'] = submit_Username
        if submit_User_Id != '':
            query_Criteria['id'] = submit_User_Id

        user_List = User.objects.filter(**query_Criteria)

        #分页处理

        dataList = ["id", "username", "nickname", "myClass"]
        page_Num = request.GET.get("page", 1)
        paginator_OfUserAll = Paginator(user_List, 30)
        user_List = paginator_OfUserAll.page(page_Num).object_list
        user_List = get_data(obj=user_List, serializer=UserSerializer, dataList=dataList, many=True)

        data["data"].update({"user_List":user_List})

        return JsonResponse(data)


#修改用户密码
class UsersPwChange(APIView):
    def post(self, request):
        data = {'status': 200, 'msg': '修改成功', 'data': {}}  # 返回集

        # 权限验证 待添加

        #获取修改用户和修改后密码
        submit_Username = request.POST.get("submit_Username", "")
        submit_Password = request.POST.get("submit_Password", "")
        print(submit_Password)

        if not re.search(r'^[0-9a-zA-Z]{8,16}$', submit_Password):  # 判断密码是否合法
            data['status'] = 400
            data['msg'] = '密码由8-16位数字字母组成'
            return  JsonResponse(data)

        #修改
        chang_User = User.objects.get(username = submit_Username)
        chang_User.set_password(submit_Password)
        chang_User.save()

        return JsonResponse(data)


