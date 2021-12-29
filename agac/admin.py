from django.contrib import admin
from .models import *

@admin.register(Sele)
class SeleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sele._meta.fields]
    list_display_links = ["sele_ismi"]
    search_fields = ["sele_ismi"]
    list_filter = ["sele_ismi"]

    class Meta:
        model = Sele


@admin.register(Tekerlek)
class TekerlekAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tekerlek._meta.fields]
    list_display_links = ["teker_ismi"]
    search_fields = ["teker_ismi"]
    list_filter = ["teker_ismi"]

    class Meta:
        model = Tekerlek


@admin.register(Govde)
class GovdeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Govde._meta.fields]
    list_display_links = ["govde_ismi"]
    search_fields = ["govde_ismi"]
    list_filter = ["govde_ismi"]

    class Meta:
        model = Govde


@admin.register(Bisiklet)
class BisikletAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bisiklet._meta.fields]

    class Meta:
        model = Bisiklet