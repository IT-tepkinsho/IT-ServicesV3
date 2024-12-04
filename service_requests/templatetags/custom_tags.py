# service_requests/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})

def format_timedelta(td):
    if td is None:
        return "N/A"
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{days} วัน {hours} ชั่วโมง {minutes} นาที"