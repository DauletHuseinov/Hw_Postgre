from django.contrib import admin

# Register your models here.
from employee.models import *

admin.site.register(Employee)
admin.site.register(Passport)
admin.site.register(WorkProject)
admin.site.register(Membership)
admin.site.register(Client)
admin.site.register(VIPClient)