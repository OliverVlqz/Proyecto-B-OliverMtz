from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .forms import CustomUserForm


#Hacer las vistas del api rest de usuarios
class UserViewSets(viewsets.ModelViewSet):
    #3 variables
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]

    #Si quieres agregar la parte de seguridad
    #Pon estas 2 variables
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    #Qué métodos va a proteger
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated()]
        return []

#Hacer una vista que me devuelva mi token
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    

class CustomUserFormAPI(APIView):
    def get(self, request, *args, **kwargs):
        form = CustomUserForm()
        fields = {}
        for field in form.fields:
            fields[field] = {
                'label': form[field].label,
                'input': form[field].field.widget.attrs,
                'type': getattr(form[field].field.widget, 'input_type', 'text'),
            }
        return Response(fields)

    def post(self, request, *args, **kwargs):
        form = CustomUserForm(request.data)
        if form.is_valid():
            user_data = form.cleaned_data
            User = get_user_model()
            user = User.objects.create_user(
                email=user_data['email'],
                password=user_data['password'],
                name=user_data['name'],
                surname=user_data['surname'],
                control_number=user_data['control_number'],
                age=user_data['age'],
                tel=user_data['tel'],
            )
            return Response({'message': 'Usuario creado con éxito'},
                            status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
