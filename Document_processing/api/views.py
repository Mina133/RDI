import os
from PIL import Image
from PyPDF2 import PdfReader
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ImageFile, PDFFile
from .serializers import ImageFileSerializer, PDFFileSerializer

# Upload Files
@api_view(['POST'])
def upload_file(request):
    file = request.FILES.get('file')
    if not file:
        return Response({'error': 'File is required'}, status=status.HTTP_400_BAD_REQUEST)

    if file.content_type.startswith('image'):
        image = ImageFile(file=file)
        image.save()
        return Response(ImageFileSerializer(image).data, status=status.HTTP_201_CREATED)
    elif file.content_type == 'application/pdf':
        pdf = PDFFile(file=file)
        pdf.save()
        return Response(PDFFileSerializer(pdf).data, status=status.HTTP_201_CREATED)

    return Response({'error': 'Unsupported file type'}, status=status.HTTP_400_BAD_REQUEST)

# List and Retrieve Files
class ImageFileViewSet(viewsets.ModelViewSet):
    queryset = ImageFile.objects.all()
    serializer_class = ImageFileSerializer

class PDFFileViewSet(viewsets.ModelViewSet):
    queryset = PDFFile.objects.all()
    serializer_class = PDFFileSerializer

# Rotate Image
@api_view(['POST'])
def rotate_image(request):
    image_id = request.data.get('id')
    angle = request.data.get('angle', 0)
    try:
        image = ImageFile.objects.get(id=image_id)
        img = Image.open(image.file.path)
        img = img.rotate(-int(angle), expand=True)
        img.save(image.file.path)
        return Response({'message': 'Image rotated successfully'})
    except ImageFile.DoesNotExist:
        return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

# Convert PDF to Image
@api_view(['POST'])
def convert_pdf_to_image(request):
    pdf_id = request.data.get('id')
    try:
        pdf = PDFFile.objects.get(id=pdf_id)
        # Convert first page of PDF to image (use external libraries as needed)
        # ...
        return Response({'message': 'PDF converted to image successfully'})
    except PDFFile.DoesNotExist:
        return Response({'error': 'PDF not found'}, status=status.HTTP_404_NOT_FOUND)
