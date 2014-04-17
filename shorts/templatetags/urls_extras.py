from django import template
from core.bing import get_iotd

register = template.Library()

@register.simple_tag
def get_random_image():
    url = get_iotd()
    return url