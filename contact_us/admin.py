from django.contrib import admin
from .models import contactus
# Register your models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display= ['name','phone','problem']


admin.site.register(contactus,ContactModelAdmin)
