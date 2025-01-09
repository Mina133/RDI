from django.db import models


# Create your models here.
class ImageFile(models.Model):
    file = models.ImageField(upload_to='images/')
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    channels = models.IntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class PDFFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
    page_count = models.IntegerField(null=True, blank=True)
    page_width = models.FloatField(null=True, blank=True)
    page_height = models.FloatField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
