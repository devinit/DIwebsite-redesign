from django import template
from di_website.vacancies.models import OfficeLocation


register = template.Library()


@register.simple_tag
def columns():
    number_of_offices = OfficeLocation.objects.exclude(
        latitude__isnull=True).exclude(longitude__isnull=True).all().count()
    return number_of_offices
