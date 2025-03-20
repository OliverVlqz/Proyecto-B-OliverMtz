from .models import CustomUser
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#Serializador para API_REST
class CustomUserSerializer(serializers.ModelSerializer):
   class Meta:
      model = CustomUser
      fields = '__all__'

#Serializador para los tokens
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
   @classmethod
   def get_token(cls, user):
      token = super().get_token(user)
      token['email'] = user.email
      #Se pueden agregar más campos
      return token
   
