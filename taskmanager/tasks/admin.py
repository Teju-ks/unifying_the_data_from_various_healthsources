# patient_data/admin.py
from django.contrib import admin
from .models import Patient, EHRData, WearableData, LabResult, Insurance, Pharmacy

admin.site.register(Patient)
admin.site.register(EHRData)
admin.site.register(WearableData)
admin.site.register(LabResult)
admin.site.register(Insurance)  # Register Insurance model
admin.site.register(Pharmacy)   # Register Pharmacy model

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _(" MediDoc")
admin.site.site_title = _("MediDoc")
admin.site.index_title = _("MediDoc")
