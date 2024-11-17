from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Country, City, State
from .utils import async_send_email
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError

User = get_user_model()

import shortuuid
import uuid
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

def file_size(value): 
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')
    
def UniqueEmailValidator( email ):
	if not User.objects.filter( email=email ).exists():
		return email
	raise ValidationError("User with this email already exists.")
    

class AdminSerializer(serializers.ModelSerializer):
    aadhar_card = serializers.ImageField(validators=[file_size])
    pan_card = serializers.ImageField(validators=[file_size], required=False)
    passport_front = serializers.ImageField(validators=[file_size], required=False)
    passport_back = serializers.ImageField(validators=[file_size], required=False)
    email = serializers.EmailField( validators=[ UniqueEmailValidator ] )
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['username', 'password']

    def validate(self, attrs):
        # Ensure required fields are provided
        required_fields = ['first_name', 'last_name', 'email', 'aadhar_card', 'city', 'pincode', 'contact_no', 'address']
        for field in required_fields:
            if field not in attrs:
                raise ValidationError({field: f"{field} is required."})

        # Validate city
        city = attrs.get('city')
        if city and not isinstance(city, City):
            raise ValidationError("City must be a valid city instance.")

        # Validate pincode if provided
        pincode = attrs.get('pincode')
        if pincode and (pincode < 100000 or pincode > 999999):
            raise ValidationError("Pincode must be a 6-digit number.")

        return attrs

    def create(self, validated_data):

        #auto generate unique username 
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        username = f"{first_name.lower()}.{last_name.lower()}"
        if User.objects.filter(username=username).exists():
            username+=str(shortuuid.ShortUUID().random(length=5))

        #auto generate unique password
        password = str(uuid.uuid4())
        user = User(username=username, 
                    email=validated_data.get('email'), 
                    is_superuser=True, is_staff=True, is_active= True,
                    first_name = first_name,
                    last_name = last_name,
                    aadhar_card =validated_data.get('aadhar_card'),
                    pan_card=validated_data.get('pan_card'),
                    passport_front=validated_data.get('passport_front'),
                    passport_back =validated_data.get('passport_back '),
                    contact_no = validated_data.get('contact_no'),
                    address = validated_data.get('address'),
                    city = validated_data.get('city'),
                    pincode = validated_data.get('pincode')
                    )
        
        # mail
        async_send_email(
            subject = "Account Account Details",
            message = f"Your Account Details:- Username: {username}, Password:{password}",
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [ user.email ]
        )
        user.set_password(password)  # convert to hashed password
        user.save()

        return user
    

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    State = StateSerializer(read_only=True)
    class Meta:
        model = City
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

	def create(self,validated_data):
		return User.objects.create_user(**validated_data)
     

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
        data['is_superuser'] = self.user.is_superuser
        return data

    


    