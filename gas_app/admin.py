from django.contrib import admin
from .models import ServiceRequest, CustomerAccount, RequestStatus

admin.site.register(ServiceRequest)
admin.site.register(CustomerAccount)
admin.site.register(RequestStatus)
