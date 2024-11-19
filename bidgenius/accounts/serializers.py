from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

   
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):   
     def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if not username or not password:
            raise ValidationError({'detail': 'Username and password are required.'})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError({'detail': 'Incorrect username or password.'})
        if not user.check_password(password):
            raise ValidationError({'detail': 'Incorrect username or password.'})
        if not user.is_active:
            raise ValidationError({'detail': 'Inactive account.'})
            
        data =  super().validate(attrs)
        data['username'] = self.user.username
        print(self.user.username)
        data['is_superuser'] = self.user.is_superuser
        return data
