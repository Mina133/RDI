from django.db import models
from PIL import Image as PILImage
from PyPDF2 import PdfReader



# Create your models here.
class ImageFile(models.Model):
    file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically set width, height, and channels when saving
        if self.file:
            img = PILImage.open(self.file)
            self.width, self.height = img.size
            self.channels = len(img.getbands())  # Number of color channels (RGB, RGBA, etc.)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file.name

class PDFFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



def save(self, *args, **kwargs):
    if not self.file or not self.file.path:
        raise FileNotFoundError("The file path is invalid or the file does not exist.")

    # Calculate PDF metadata
    try:
        reader = PdfReader(self.file.path)
        self.pages = len(reader.pages)
        self.width = reader.pages[0].mediabox.width
        self.height = reader.pages[0].mediabox.height
    except Exception as e:
        raise ValueError(f"Error processing the PDF file: {str(e)}")

    super().save(*args, **kwargs)
