from urllib import response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime

from home.serializer import UserSerializer
from rest_framework.response import Response

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class LoginView(APIView):
    def post(self, request):
        email= request.data['email']
        password= request.data['password']

        user =User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload ={
            'id': user.id,
            'exp': datetime.datetime.utcnow() +datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        
        response= Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data ={
            'jwt':token
        }
        
        return response
