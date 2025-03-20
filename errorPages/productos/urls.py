from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'api', ProductoViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('agregar/', agregar_view, name='agregar_producto'),
]