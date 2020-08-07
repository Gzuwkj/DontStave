from rest_framework import serializers
from UserProfile.models import User, UserToken


class UserSerializer(serializers.ModelSerializer):

    def create(self, pwd):
        data = self.data
        user = User.objects.create_user(
            username=data['username'],
            password=pwd,
            stuId=data.get('stuId', ""),
            school=data.get('school', ""),
            email=data.get('email', ""),
            tel=data.get('tel', "")
        )
        return UserSerializer(user), user

    class Meta:
        model = User
        fields = ("id", "password", "last_login", "is_superuser", "username", "first_name",
                  "last_name", "email", "is_staff", "is_active", "date_joined", "nickname", "school",
                  "major", "myClass", "stuId", "headImage", "synopsis", "tel", "rating", "ac_nums",
                  "groups", "user_permissions",)

        # fields = ("id",  "username", "password", "GENDER_CHOICE", "school", "major", "myClass",
        #           "stuId", "headImage", "synopsis", "tel", "rating", "ac_nums")


# class OtherUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("nickname", "GENDER_CHOICE", "school", "major", "headImage", "synopsis", "rating", "ac_nums")


# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "username", "nickname", "myClass")



class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = '__all__'

        # depth = 1 #代表找嵌套关系的第几层
        # read_only_fields = ["id"] #将多个字段指定为只读


