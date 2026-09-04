from django.contrib import admin
from .models import Wallet, CreditTransaction

admin.site.register(Wallet)
admin.site.register(CreditTransaction)