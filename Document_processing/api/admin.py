from django.contrib import admin
from .models import ImageFile, PDFFile

admin.site.register(ImageFile)
admin.site.register(PDFFile)