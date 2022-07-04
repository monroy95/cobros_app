from django.contrib import admin
from .models import Charge


class ChargeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'monto',
    )

    search_fields = ('user',)


# Register your models here.
admin.site.register(Charge, ChargeAdmin)
