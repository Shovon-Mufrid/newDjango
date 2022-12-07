# Video 7.3

from django import template

register = template.Library()

# def my_filter(value):
#     return value + "this is string from custom filter"

# to use parameter in filter
def my_filter(value, arg):
    return value + " " + arg



register.filter('custom_filter', my_filter)   #register naming>>if i type custom filter, my_filter will load 