from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')

class CustomerAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class RequestStatus(models.Model):
    name = models.CharField(max_length=50)
