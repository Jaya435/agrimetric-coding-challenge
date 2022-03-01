
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from orders import views


router = routers.DefaultRouter()
router.register(r'sandwich', views.SandwichViewSet, 'sandwich')
router.register(r'orders', views.Orders, 'orders')

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
