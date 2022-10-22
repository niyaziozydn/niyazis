"""amazingniyaziblog URL Configuration

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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from blog.views import anasayfa, game_action, detay, BanaUlas, cikis,  sifre_degistir, kayit, is_ekle, niyaziskill
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',anasayfa,name='anasayfa'),
    path("game/",niyaziskill,name ='game_action'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('iletisim', BanaUlas, name='iletisim'),
    path('cikis', cikis, name='cikis'),
    path('sifre-degistir', sifre_degistir, name='sifre-degistir'),
    path('kayit', kayit, name='kayit'),
    path('is_ekle', is_ekle, name='is_ekle'),
    path('giris', auth_views.LoginView.as_view(
        template_name = 'pages/giris.html'
    ), name='giris'),
    path('hakkimda', TemplateView.as_view(
        template_name = 'pages/hakkimda.html'
    ), name='hakkimda'),
    path('bilgilendirme', TemplateView.as_view(
        template_name = 'pages/bilgilendirme.html'
    ), name='bilgilendirme')
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
