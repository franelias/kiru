from django.db import models

# Create your models here.

class File(models.Model):
    username = models.CharField(blank=False, max_length=50)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
