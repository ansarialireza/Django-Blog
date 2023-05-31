from django.contrib import admin
from webapp.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')
    date_hierarchy = 'created_date'
    list_filter = ('email',)
    search_fields = ('name', 'message')

    


admin.site.register(Contact, ContactAdmin)
# Register your models here.
