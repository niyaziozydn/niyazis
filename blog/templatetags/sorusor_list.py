from atexit import register
from django import template
from blog.models import SoruModeli

register = template.Library()

@register.simple_tag
def sorusor_list():
    sorular=SoruModeli.objects.all()
    return sorular