from django import template
import misaka as m

register = template.Library()

@register.filter
def markdown_to_html(markdown_text):
    return m.html(markdown_text)