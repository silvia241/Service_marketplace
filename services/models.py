from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ServiceRequest(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester.username} requested {self.service.title}"

