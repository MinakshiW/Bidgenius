
"""from accounts.models import User
from rest_framework import viewsets
from accounts.serializers import UserSerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = MyTokenObtainPairSerializer
    queryset = User.objects.all()
    http_method_names = ['get','post']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]"""



from rest_framework import generics
from rest_framework.views import APIView
from .serializers import AdminSerializer, CountrySerializer, StateSerializer, CitySerializer, UserSerializer
from .models import User, Country, State, City
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt import tokens as jwt_tokens
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate

from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken



class AdminCreateAPI(generics.ListCreateAPIView):
    serializer_class = AdminSerializer
    queryset = User.objects.all()


class CountryCreateAPI(generics.ListCreateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class StateCreateAPI(generics.ListCreateAPIView):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def get_queryset(self):
        country_id = self.request.query_params.get('country_id')
        if country_id:
            return State.objects.filter(country_id=country_id)
        return State.objects.all()

class CityCreateAPI(generics.ListCreateAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_queryset(self):
        state_id = self.request.query_params.get('state_id')
        if state_id:
            return City.objects.filter(state_id=state_id)
        return City.objects.all()
    
    
    
class LogoutAPI(APIView):
    permission_classes = [ IsAuthenticated ]
    authentication_classes = [JWTAuthentication] 

    def post(self, request):
        try:
            # Get the user's tokens
            user = request.user
            
            # Get the tokens associated with the user
            outstanding_tokens = OutstandingToken.objects.filter(user=user)
            
            # Blacklist each outstanding token
            for token in outstanding_tokens:
                BlacklistedToken.objects.create(token=token)
                token.delete()  # Optionally delete the token from outstanding tokens

            return Response(data={"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

