from django import template
from ..models import MenuItem

register = template.Library()

@register.filter
def get_item(items, item_id):
    return items.get(id=item_id)
