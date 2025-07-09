from django import template
import markdown

register = template.Library()

@register.filter
def markdown(value):
    return markdown.markdown(value, extensions=['fenced_code', 'codehilite']) 