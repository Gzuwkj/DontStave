from rest_framework import serializers
from mytest.models import book, Auth

class bookSerializer(serializers.ModelSerializer):
    s = serializers.CharField(default="")
    class Meta:
        model = book
        # exclude = ()
        fields = '__all__'


class AuthSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source="book.bn")

    class Meta:
        model = Auth
        fields = "__all__"
        # depth = 1

