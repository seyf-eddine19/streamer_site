from django import template

register = template.Library()

@register.filter
def get_text(content_list, key):
    if not content_list:
        return ''
    for item in content_list:
        if item.get('key') == key:
            return item.get('content')
    return ''
