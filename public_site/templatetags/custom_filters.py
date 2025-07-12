from django import template

register = template.Library()

@register.filter
def get_by_key(queryset, key):
    try:
        for obj in queryset:
            if obj.key == key:
                return obj
    except Exception:
        pass
    return None

@register.filter
def get_content_by_lang(content_obj, lang):
    if content_obj:
        return content_obj.content_ar if lang == 'ar' else content_obj.content_en
    return ''

@register.filter
def get_text(content_list, key):
    if not content_list:
        return ''
    for item in content_list:
        if item.get('key') == key:
            return item.get('content')
    return ''
