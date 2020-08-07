from rest_framework_jwt.settings import api_settings
from .serializers import UserSerializer
from apps.util import get_data


# 在token中封装有 username user_id ip
def jwt_response_payload_handler(user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }

    """
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 获取token载荷
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # HS256 加密
    payload = jwt_payload_handler(user)
    # 获取ip地址 防止同token异地登录
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    payload['ip'] = ip
    token = jwt_encode_handler(payload)
    return {
        'token': token,
        'user': get_data(obj=user, serializer=UserSerializer, context={'request': request})
    }


from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class MyVerifyJWTSerializer(VerifyJSONWebTokenSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, token):
        payload = self._check_payload(token=token)
        user = self._check_user(payload=payload)
        return {
            'payload': payload,
            'user': user
        }


class MyJWTAuthentication(JSONWebTokenAuthentication):
    #  验证时 验证用户是否存在 验证ip是否相同 验证token是否过期
    def authenticate(self, request):
        token = self.get_jwt_value(request)
        if not token:
            return None
        t = MyVerifyJWTSerializer().validate(token)
        payload = t.get('payload')
        user = t.get('user')
        # 获取ip地址 防止同token异地登录
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        if ip != payload['ip']:
            return None
        if user:
            return user
        else:
            return None


def check_auth(request):
    # 通过自定义验证函数 检查用户是否有效， 有效即返回该用户实例 无效即返回None
    user = MyJWTAuthentication().authenticate(request)
    if user:
        is_login = True
    else:
        is_login = False
    return is_login, user

# JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InlpdXloIiwiZXhwIjoxNTgzMzEyMzU5LCJlbWFpbCI6IiIsImlwIjoiMTI3LjAuMC4xIn0.YEYqDxGKfHKYToRBsZQTEY9q86i2hVJ-EU1ag6WbrtE
