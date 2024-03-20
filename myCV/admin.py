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

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'created_date', 'updated_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']
    ordering = ["name"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'created_date', 'updated_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']
    ordering = ["name"]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_location', 'start_date', 'end_date']
    search_fields = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date']
    list_editable = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date']
    ordering = ["-start_date"]