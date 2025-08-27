from django import template
import markdown as md

register = template.Library()

@register.filter(name='markdown')
def render_markdown(value):
    return md.markdown(value, extensions=['fenced_code', 'codehilite'])
