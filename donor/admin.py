from django.contrib import admin
from .models import Donor, Hospital, BloodRequest, BloodDrive
# Register your models here.
admin.site.register(Donor)
admin.site.register(Hospital)
admin.site.register(BloodRequest)
admin.site.register(BloodDrive)
