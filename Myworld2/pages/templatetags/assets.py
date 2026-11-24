from django import template

from pages.assets import versioned_static

register = template.Library()


@register.simple_tag
def vstatic(path):
    """Like {% static %} but with a ?v= timestamp so edited files are re-downloaded."""
    return versioned_static(path)
