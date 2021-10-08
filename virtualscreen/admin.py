from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ['name', 'phone_number']


admin.site.register(Contact, ContactAdmin)
