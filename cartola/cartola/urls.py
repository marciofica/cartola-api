"""cartola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from clubes import views

router = routers.DefaultRouter()
router.register(r'clubes', views.ClubeViewSet)
router.register(r'times', views.TimeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'user/me', views.UserLoggedViewSet)
router.register(r'jogadores', views.JogadorViewSet)
router.register(r'partidas', views.PartidaViewSet)
router.register(r'indicadores', views.IndicadorViewSet)
router.register(r'partidas-confirmacao', views.PartidaConfirmacaoViewSet)
router.register(r'partidas-gols', views.PartidaGolViewSet)
router.register(r'partidas-indicadores', views.PartidaIndicadorViewSet)
router.register(r'partidas-notas', views.PartidaNotaViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
]