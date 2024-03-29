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

    class Meta:
        model = ImageSetting


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'created_date', 'updated_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']
    ordering = ["name"]

    class Meta:
        model = Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_location', 'start_date', 'end_date', 'created_date', 'updated_date']
    search_fields = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date']
    list_editable = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date']
    ordering = ["-start_date"]

    class Meta:
        model = Experience


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'school_location', 'graduation_type', 'start_date', 'end_date', 'created_date', 'updated_date']
    search_fields = ['school_name', 'school_location', 'graduation_type', 'start_date', 'end_date']
    list_editable = ['school_name', 'school_location', 'graduation_type', 'start_date', 'end_date']
    ordering = ["-start_date"]

    class Meta:
        model = Education


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon', 'created_date', 'updated_date']
    search_fields = ['order', 'link']
    list_editable = ['order', 'link', 'icon']
    ordering = ["link"]

    class Meta:
        model = SocialMedia


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'slug', 'button_text', 'file', 'created_date', 'updated_date']
    search_fields = ['order', 'slug', 'button_text']
    list_editable = ['order', 'slug', 'button_text', 'file']
    ordering = ["order"]

    class Meta:
        model = Document
