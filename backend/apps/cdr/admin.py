from django.contrib import admin
from apps.cdr.models import CDR

# Register your models here.


@admin.register(CDR)
class CRDAmmin(admin.ModelAdmin):
    model_fields = [field.name for field in CDR._meta.fields]
    list_display = model_fields