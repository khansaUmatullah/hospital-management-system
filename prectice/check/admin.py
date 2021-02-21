from django.contrib import admin
from .models import contact,doctors,employee,patient,visited,admitted,nurses,receiptionist,pharmacy,attend,records,prescription,prescribed,room,furniture,surgical_instruments,staff_supplies
# Register your models here.

admin.site.register(contact)
admin.site.register(doctors)
admin.site.register(employee)
admin.site.register(patient)
admin.site.register(visited)
admin.site.register(admitted)
admin.site.register(nurses)
admin.site.register(receiptionist)
admin.site.register(pharmacy)
admin.site.register(attend)

admin.site.register(records)
admin.site.register(prescribed)
admin.site.register(prescription)
admin.site.register(room)
admin.site.register(furniture)
admin.site.register(surgical_instruments)
admin.site.register(staff_supplies)
