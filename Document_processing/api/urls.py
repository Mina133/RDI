from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'images', views.ImageFileViewSet, basename='image')
router.register(r'pdfs', views.PDFFileViewSet, basename='pdf')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', views.upload_file, name='upload_file'),
    path('rotate/', views.rotate_image, name='rotate_image'),
    path('convert-pdf-to-image/', views.convert_pdf_to_image, name='convert_pdf_to_image'),
]
