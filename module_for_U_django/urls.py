"""
URL configuration for module_for_U_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect, render
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

def base(request):
    return render(request, 'base.html')

from by_pass_sheet.urls import router as by_pass_sheet_router
from employee.urls import router as employee_router
from reference.urls import router as reference_router
from student.urls import router as student_router

from two_factor.urls import urlpatterns as tf_urls

router = DefaultRouter()

router.registry.extend(by_pass_sheet_router.registry)
router.registry.extend(employee_router.registry)
router.registry.extend(reference_router.registry)
router.registry.extend(student_router.registry)

urlpatterns = [
    path('', base),
    path(r'', include(tf_urls)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
