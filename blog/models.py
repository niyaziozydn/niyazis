from dataclasses import fields
from distutils.command.upload import upload
from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django import forms
from account.models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    slug=AutoSlugField(populate_from='isim', unique=True)

    class Meta:
        db_table = 'kategori'
        verbose_name_plural='Kategoriler'
        verbose_name='Kategori'

    def __str__(self):
        return self.isim

 
class SoruModeli(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    Sirket = models.CharField(max_length=100,blank=False, null=False)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from = 'isim', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    resim = models.ImageField(upload_to='yazi_resimleri', default='isilan.png')
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    düzenlenme_tarihi = models.DateTimeField(auto_now=True)
   

    class Meta:
        db_table = 'isim'
        verbose_name_plural = 'İş İlanları'
        verbose_name = 'İş ilanları'

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


class UserSkill(models.Model):
    user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    skill=models.ForeignKey(KategoriModel,on_delete=models.CASCADE)
    class Meta:
        db_table ='user_skill'
        verbose_name= 'userskill'
        verbose_name_plural='skills'

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
            'is_staff',
            
        )

class isekleModelForm(forms.ModelForm):
    class Meta:
        model = SoruModeli
        exclude = ('slug','resim')

class SkillModelForm(forms.ModelForm):
    class Meta:
        model = UserSkill
        exclude = ('user',)




