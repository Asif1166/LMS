from django import template
import math
register = template.Library()

@register.simple_tag
def calculate_price(price, discount):
    
    sellprice = price
    sellprice = price - (price * discount * 0.01)
    return math.floor(sellprice)

@register.filter
def taka(price):
    
    return f'৳{price}'