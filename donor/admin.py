from django.contrib import admin
from .models import Donor,Hospital,User
# Register your models here.
admin.site.register(Donor)
admin.site.register(Hospital)
admin.site.register(User)
