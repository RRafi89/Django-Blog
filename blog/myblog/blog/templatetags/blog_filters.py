from django import template
import re

register = template.Library()

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def get_first_image(content):
    """Extract the first image URL from HTML content"""
    if not content:
        return None
    match = re.search(r'<img[^>]*src="([^"]*)"', content)
    return match.group(1) if match else None