from audioop import reverse
from email import message
from turtle import title
from django.shortcuts import redirect, render, get_object_or_404
from blog.models import BanaUlasModeli, KategoriModel, YorumModeli, SoruModeli, BanaUlasForm, KayıtFormu, isekleModelForm, UserSkill, SkillModelForm
from django.core.paginator import Paginator
from django.contrib import messages
import random
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import logging
from autoslug import AutoSlugField
from django.db.models import Q


def anasayfa(request):
    Projelerim = SoruModeli.objects.all()
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(Projelerim, 3)
    sorgu = request.GET.get('sorgu')
    if sorgu:
        Projelerim = Projelerim.filter(
            Q(Sirket__icontains=sorgu) |
            Q(icerik__icontains=sorgu)
        ).distinct()
        
    kategori = UserSkill.objects.filter(user_id=request.user.id)
    skill_list = []
    for kate in kategori:
        skill_list.append(kate.id)
    Projelerim = SoruModeli.objects.filter(
    kategoriler__in=skill_list).order_by('-id')


    return render(request,'pages/anasayfa.html',context={
        'Projelerim': paginator.get_page(sayfa)
    })


def detay(request, slug):
    Proje = get_object_or_404(SoruModeli, slug=slug)
    return render(request, 'pages/detay.html', context={
        'Proje': Proje,
    })


@login_required(login_url='giris')
def game_action(request):
    post = request.POST
    sayi = post.get('sayi')
    hak = post.get('hak')

    if not sayi:
        sayi = random.randint(1, 100)
    else:
        sayi = int(sayi)
    if not hak:
        hak = 5
    else:
        hak = int(hak)

    result = ''
    if post:
        value = post.get('value')
        print(value)

        girilen = int(value)
        hak -= 1

        if girilen > sayi:
            result = f"Daha düsük bir sayi giriniz. Kalan hakkınız: {hak} "

        elif girilen < sayi:
            result = f"Daha yüksek bir sayi giriniz. Kalan hakkınız: {hak} "
        elif girilen == sayi:
            result = "Tebrikler dogru bildiniz"

        if hak == 0:
            result = f"hakkınız Bitti. Doğru Cevap: {sayi}"

    return render(request, 'pages   /game.html', context={'result': result, 'hak': hak, 'sayi': sayi})


def BanaUlas(request):
    form = BanaUlasForm()
    if request.method == 'POST':
        form = BanaUlasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Mesajınızı aldım. En kısa zamanda dönüş sağlayacağım.')

            return redirect('anasayfa')

    context = {
        'form': form
    }
    return render(request, 'pages/iletisim.html', context=context)


def cikis(request):
    logout(request)
    return redirect('anasayfa')


@login_required(login_url='/')
def sifre_degistir(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            kullanici = form.save()
            update_session_auth_hash(request, kullanici)
            messages.success(request, 'şifreniz güncellendi')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'pages/sifre-degistir.html', context={
        'form': form
    })


def kayit(request):
    if request.method == 'POST':
        form = KayıtFormu(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Kayıt oldunuz. Girişiniz yapıldı')

            return redirect('anasayfa')
    else:
        form = KayıtFormu()

    return render(request, 'pages/kayit.html', context={
        'form': form
    })


def is_ekle(request):
    form = isekleModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()
        messages.success(request, 'İş ilanınız başarı ile Eklendi')
        return redirect('anasayfa')

    return render(request, 'pages/is_ekle.html', context={
        'form': form
    })

@login_required(login_url='/')
def niyaziskill(request):
    post = request.POST
    kategoriler = KategoriModel.objects.filter()
    user_skill = UserSkill.objects.filter()
    if post:
        print(post)
        skill = post.getlist('skills')
        UserSkill.objects.filter(user_id=request.user.id).delete()
        for x in skill:

            user_skill_create = UserSkill()
            user_skill_create.skill_id = x
            user_skill_create.user = request.user

            user_skill_create.save()
        messages.success(request, 'Yeteneğiniz başarı ile eklendi')
        return redirect('anasayfa')

    return render(request, 'pages/game.html', context={
        'kategoriler': kategoriler, 'user_skill': user_skill
    })
