from django.utils.safestring import mark_safe
from django import template
from web_project.template_helpers.theme import TemplateHelper

register = template.Library()


# Register tags as an adapter for the Theme class usage in the HTML template


@register.simple_tag
def get_theme_variables(scope):
    return mark_safe(TemplateHelper.get_theme_variables(scope))


@register.simple_tag
def get_theme_config(scope):
    return mark_safe(TemplateHelper.get_theme_config(scope))


@register.filter
def filter_by_url(submenu, url):
    if submenu:
        for subitem in submenu:
            subitem_url = subitem.get("url")
            if subitem_url == url.path or subitem_url == url.resolver_match.url_name:
                return True

            # Recursively check for submenus
            elif subitem.get("submenu"):
                if filter_by_url(subitem["submenu"], url):
                    return True

    return False
