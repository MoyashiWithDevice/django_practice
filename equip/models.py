from django.db import models
from django.conf import settings
from django_boost.models.mixins import LogicalDeletionMixin

# Create your models here.
class Equip(LogicalDeletionMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locate = models.CharField(max_length=100)
    ipaddress = models.GenericIPAddressField(default=0)
    etc = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name