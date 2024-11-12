from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/")
    thumbnail = models.ImageField(upload_to="thumbnail/", null=True, blank=True)

    def __str__(self):
        return str(self.title)
