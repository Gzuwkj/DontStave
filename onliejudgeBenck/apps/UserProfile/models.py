from django.db import models
from django.contrib.auth.models import AbstractUser
import os


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.username, ext)
    return os.path.join('user/', str(instance.id), filename)


class User(AbstractUser):
    GENDER_CHOICE = (('男', '男'), ('女', '女'))
    nickname = models.CharField(max_length=50, blank=True, default=True)
    school = models.CharField(max_length=30, default="贵州大学", blank=True)                              # 学校
    major = models.CharField(max_length=10,default="计科", blank=True)                                                    # 专业
    myClass = models.CharField(max_length=15, default="175",blank=True)                                                  # 班级
    stuId = models.CharField(max_length=20, default="1717000000",blank=True)                                                    # 学号
    headImage = models.ImageField(upload_to=user_directory_path, default="default.jpg", blank=True)               # 头像
    synopsis = models.TextField(default="这个人很懒，什么都没有写...", blank=True)                        # 简介
    tel = models.CharField(max_length=11, blank=True)                                                     # 手机号
    rating = models.IntegerField(default=1500)                                                            # rating
    ac_nums = models.IntegerField(default=0)                                                              # accept nums


    def change_token(self, token): # 修改token
        usertoken = self.usertoken
        usertoken.token = token
        usertoken.save()

    def updata_user(self, data): #改
        self.nickname = data.get('nickname',self.nickname)
        self.GENDER_CHOICE = data.get('sex', self.GENDER_CHOICE)
        self.school = data.get('school', self.school)
        self.email = data.get('email', self.email)
        self.tel = data.get('tel', self.tel)
        self.major = data.get('major',self.major)
        self.myClass = data.get('myClass',self.myClass)
        self.synopsis = data.get('synopsis', self.synopsis)
        self.stuId = data.get('stuId', self.stuId)
        self.headImage = data.get('headImage',self.headImage)
        self.save()

    def add_user(self, data): #增
        user = User.objects.create_user(
            username=data['username'], password=data['password'], stuId=data.get('stuId', ""),
            school=data.get('school', ""), email=data.get('email', ""), tel=data.get('tel', ""), )

    def get_user(self): #查
        from .serializers import UserSerializer
        userSerializer = UserSerializer(self)
        return userSerializer.data

    class Meta(AbstractUser.Meta):
        pass


class UserToken(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE)
    token = models.CharField(max_length=200, blank=True, null=True)

    def add_usertoken(self): #增
        pass

    # def get_usertoken(self): #查
    #     from .serializers import UserTokenSerializer
    #     tokenSerializer = UserTokenSerializer(self)
    #     return tokenSerializer.data
    def updata_usertoken(self, data): #改
        pass  #由于token是伴随user  修改方法在User模型中实现
