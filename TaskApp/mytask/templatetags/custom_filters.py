from django import template

register=template.Library()

@register.filter

def percentage(value,total_tasks):

    return 0 if total_tasks==0 else round((value/total_tasks)*100)