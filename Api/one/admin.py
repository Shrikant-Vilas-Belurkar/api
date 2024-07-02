from django.contrib import admin
from .models import Api
# Register your models here.
class ApiAdmin(admin.ModelAdmin):
    list_display =['fname', 'fstart','fend','ffare','fdate']



admin.site.register(Api,ApiAdmin)


