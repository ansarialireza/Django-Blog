from django.contrib import admin
from webapp.models import Contact,Newsletter


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')
    date_hierarchy = 'created_date'
    list_filter = ('email',)
    search_fields = ('name', 'message')

    


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
# Register your models here.
