import jwt
from rest_framework.exceptions import AuthenticationFailed
from core.models import User
from django.conf import settings
from django.contrib.gis.geos import Point

def get_user_from_token(request):
    authorization_header = request.headers.get('Authorization')
    
    if not authorization_header:
        raise AuthenticationFailed('No Auth Header Provided')

    token = authorization_header.split()[1]  #Supossing formar is: "Bearer <token>"

    try:
    
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token Expired')
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Not Valid Token')


    user_id = payload.get('user_id')
    user = User.objects.get(pk=user_id)

    return user





