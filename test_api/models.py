from django.db import models

class TempForms(models.Model):
    name_temp = models.CharField(max_length=255)
    name_field = models.CharField(max_length=255)
    name_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name_temp