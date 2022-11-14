from paints.models import Collection
from django import template

register = template.Library()


@register.simple_tag
def collections():
    return Collection.objects.all()


@register.simple_tag
def years():
    return Collection.objects.all()


@register.simple_tag
def collections():
    return Collection.objects.all()


@register.simple_tag
def collections():
    return Collection.objects.all()
