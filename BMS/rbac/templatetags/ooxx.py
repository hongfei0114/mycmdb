
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag(filename="my_menu.html")
def show_menu(request):
    menu_list = request.session[settings.MENU_SESSION_KEY]
    return {"menu_list": menu_list}
