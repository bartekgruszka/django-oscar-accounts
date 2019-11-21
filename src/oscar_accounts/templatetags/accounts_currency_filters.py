from oscar.templatetags.currency_filters import currency as oscar_currency
from django import template
from django.conf import settings


register = template.Library()

@register.filter(name='currency')
def currency(value, currency=None):
    if currency is None:
        currency = getattr(settings, 'OSCAR_ACCOUNTS_DEFAULT_CURRENCY', settings.OSCAR_DEFAULT_CURRENCY)

    return oscar_currency(value, currency)
