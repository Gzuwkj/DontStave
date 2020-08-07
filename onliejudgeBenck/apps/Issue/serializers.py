from rest_framework import serializers
from apps.util import get_data
from .models import *


class ProblemSerializer(serializers.ModelSerializer):
    # problemData = serializers.SerializerMethodField()
    problemExample = serializers.SerializerMethodField()

    # @staticmethod
    # def get_problemData(obj):
    #     data = {}
    #     problemDataList = obj.problemdata_set.all()
    #     data = get_data(obj=problemDataList, serializer=ProblemExampleSerializer)
    #     return data

    @staticmethod
    def get_problemExample(obj):
        data = {}
        problemExampleList = obj.problemexample_set.all()
        data = get_data(obj=problemExampleList, serializer=ProblemExampleSerializer, many=True)
        return data

    class Meta:
        model = Problem
        fields = '__all__'
        method_fields = ["problemExample"]


class ProblemDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProblemData
        fields = ("standardInput", "standardOutput")


class ProblemExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProblemExample
        fields = ("sampleInput", "sampleOutput")


class ProblemSubmitSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    problem = serializers.SerializerMethodField()

    @staticmethod
    def get_user(obj):
        from UserProfile.serializers import UserSerializer
        user = obj.user
        dataList = ["id", "username", "nickname"]
        data = get_data(obj=user, serializer=UserSerializer, dataList=dataList)
        return data

    @staticmethod
    def get_problem(obj):
        problem = obj.problem
        dataList = ["no", "title"]
        data = get_data(obj=problem, serializer=ProblemSerializer, dataList=dataList)
        return data

    class Meta:
        model = ProblemSubmit
        fields = "__all__"
        method_fields = ["user", "problem"]




