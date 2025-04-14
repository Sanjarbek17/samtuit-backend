"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
# make_password
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.conf.urls.static import static


class LoginHome(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class Resigter(APIView):
    def post(self, request):
        try:
            data = request.data
            user = User.objects.create(
                username=data['username'],
                password=make_password(str(data['password'])),
            )
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ClassRoom.urls')),
    path('lesson/', include('LessonPlanner.urls')),
    path('payment/', include('PayMents.urls')),
    path('login/', LoginHome.as_view()),
    path('register/', Resigter.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
