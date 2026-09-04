from django.contrib import admin
from .models import ExchangeRequest, Exchange, ExchangeDispute, Rating

admin.site.register(ExchangeRequest)
admin.site.register(Exchange)
admin.site.register(ExchangeDispute)
admin.site.register(Rating)