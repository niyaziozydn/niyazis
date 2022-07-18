from dataclasses import fields
from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django import forms
from account.models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class SoruModeli(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    title = models.CharField(max_length=100,blank=False, null=False)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from = 'isim', unique=True)
    resim = models.ImageField(upload_to='yazi_resimleri',default='selamdunya')
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    düzenlenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'isim'
        verbose_name_plural = 'Soru Modeli'
        verbose_name = 'Soru Modeli'

    def __str__(self):
        return self.isim

class YorumModeli(models.Model):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yorum = RichTextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        db_table ='yorum'
        verbose_name= 'Yorum'
        verbose_name_plural='Yorumlar'

class BanaUlasModeli(models.Model):
    email = models.EmailField(max_length=60)
    isim_soyisim=models.CharField(max_length=70)
    mesaj = models.TextField()

    class Meta:
        db_table ='iletisim'
        verbose_name= 'Bana Ulas'
        verbose_name_plural='Ulasma'
    def __str__(self):
        return self.email
    
class ProjelerimModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    title = models.CharField(max_length=100,blank=False, null=False)
    icerik = RichTextField()
    resim = models.ImageField(upload_to='yazi_resimleri',default='selamdunya')
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    düzenlenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        db_table ='Projelerim'
        verbose_name= 'Bana Proje'
        verbose_name_plural='Projema'



class BanaUlasForm(forms.ModelForm):
    class Meta:
        model = BanaUlasModeli
        fields = ('isim_soyisim','email','mesaj')

class KayıtFormu(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )