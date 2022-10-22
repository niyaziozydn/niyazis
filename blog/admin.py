from django.contrib import admin

from blog.models import BanaUlasModeli, ProjelerimModel, SoruModeli, YorumModeli, KategoriModel, UserSkill

# Register your models here.


class SoruAdmin(admin.ModelAdmin):
    list_display= (
        'isim','olusturulma_tarihi','düzenlenme_tarihi'
    )

admin.site.register(SoruModeli, SoruAdmin)

class YorumAdmin(admin.ModelAdmin):
    list_display= (
        'yazan','olusturulma_tarihi','guncellenme_tarihi'
    )

admin.site.register(YorumModeli, YorumAdmin)
admin.site.register(BanaUlasModeli)
admin.site.register(ProjelerimModel)
admin.site.register(KategoriModel)

admin.site.register(UserSkill)
