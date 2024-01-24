from django.db import models
from django.utils import timezone
# from datetime import datetime

# Create your models here.
class Dropdown(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    shortName = models.CharField(max_length=100, blank=True, null=True)

    # isDefaultSelected = models.BooleanField(default=False)
    # isDefault = models.BooleanField(default=False)
    # isActive = models.BooleanField(default=True)
    # modified_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_by = models.IntegerField(default=0)
    # created_by = models.IntegerField(default=0)

    class Meta:
        abstract = True

class Dropdown1(Dropdown):
    pass

    def __str__(self):
        return str(self.id)

class Dropdown2(Dropdown):
    pass

    def __str__(self):
        return str(self.id)

class Dropdown3(Dropdown):
    pass

    def __str__(self):
        return str(self.id)        