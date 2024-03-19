from django.contrib import admin
from myCV.models import *


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'created_date', 'updated_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']
    ordering = ["name"]

    class Meta:
        model = GeneralSetting
