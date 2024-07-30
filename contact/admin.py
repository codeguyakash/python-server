from django.contrib import admin
from contact.models import *
# Register your models here.

admin.site.register(SolarInquiry)
admin.site.register(SolarStatus)
admin.site.register(SolarMaintainceStatus)
admin.site.register(SolarMaintanceInquries)