from django import template

register = template.Library()

@register.filter(name='lookup')
def dict_lookup(dictionary, key):
    return dictionary.get(key)
