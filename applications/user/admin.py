from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'full_name',
        'active_until',
    )

    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    search_fields = ('id', 'active_until', 'email', 'phone',)


# Register your models here.
admin.site.register(User, UserAdmin)
