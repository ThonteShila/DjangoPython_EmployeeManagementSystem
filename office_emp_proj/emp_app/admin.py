from django.contrib import admin
from .models import Employee, Department, Role


# Register your models here.
#admin.py  to create and show all modeules after going into admin portal

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
