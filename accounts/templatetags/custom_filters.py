from django import template


register = template.Library()


@register.filter
def placeholder(value, token):
    value.field.widget.attrs['placeholder'] = token
    return value

# def label(value, token):
#
#     value.fields['is_admin'].label = token
#     return value