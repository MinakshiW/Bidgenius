from accounts.models import User
from rest_framework import viewsets
from accounts.serializers import UserSerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = MyTokenObtainPairSerializer
    queryset = User.objects.all()
    http_method_names = ['get','post']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



