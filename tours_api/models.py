from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=255, blank=False)
    price = models.FloatField(blank=True)
    info = models.TextField()
    image = models.ImageField(upload_to='tour/', blank=True)

    def __str__(self):
        return self.name
