import os
from PIL import Image
from PyPDF2 import PdfReader
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ImageFile, PDFFile
from .serializers import ImageFileSerializer, PDFFileSerializer
from pdf2image import convert_from_path
import fitz  # PyMuPDF


# Upload Files
@api_view(['POST'])
def upload_file(request):
    file = request.FILES.get('file')
    if not file:
        return Response({'error': 'File is required'}, status=status.HTTP_400_BAD_REQUEST)

    if file.content_type.startswith('image'):
        image = ImageFile(file=file)
        image.save()  # This will auto-populate width, height, and channels
        return Response(ImageFileSerializer(image).data, status=status.HTTP_201_CREATED)
    elif file.content_type == 'application/pdf':
        pdf = PDFFile(file=file)
        pdf.save()  # PDF will auto-populate page_count, page_width, page_height
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
    if not pdf_id:
        return Response({'error': 'PDF ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        pdf = PDFFile.objects.get(id=pdf_id)
        pdf_path = pdf.file.path

        # Open the PDF file
        doc = fitz.open(pdf_path)

        # Prepare output directory
        output_dir = os.path.join(os.path.dirname(pdf_path), 'converted_images')
        os.makedirs(output_dir, exist_ok=True)

        # List to store paths of generated images
        image_paths = []

        # Iterate over all pages and convert them to images
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # Load the page
            pix = page.get_pixmap()  # Generate pixmap (image)
            output_image_path = os.path.join(output_dir, f"pdf_{pdf_id}_page_{page_num + 1}.png")
            pix.save(output_image_path)  # Save the image
            image_paths.append(output_image_path)  # Append to the list

        doc.close()

        return Response({
            'message': 'PDF converted to images successfully',
            'image_paths': image_paths
        }, status=status.HTTP_200_OK)

    except PDFFile.DoesNotExist:
        return Response({'error': 'PDF not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)