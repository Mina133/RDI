# RDI
# Document Processing App

This Django-based Document Processing App is designed for converting PDF documents into images, with added functionalities for extracting document metadata and rotating images. It integrates seamlessly with PostgreSQL and provides a RESTful API for user interaction. The project is built with a structured and maintainable architecture for deployment on platforms like PythonAnywhere.

---

## Features

### 1. **PDF to Image Conversion**

- Converts all pages of a PDF document into high-quality PNG images.
- Handles large multi-page PDFs efficiently.

### 2. **Image Rotation**

- Supports rotating images extracted from PDFs to correct orientation or for specific use cases.

### 3. **Metadata Extraction**

- Automatically extracts and saves document metadata, including:
  - Width and height of images.
  - Page count.

### 4. **RESTful API**

- Provides endpoints to:
  - Upload PDFs.
  - Trigger PDF-to-image conversion.
  - Retrieve processed images.
- Built using Django REST Framework (DRF) for easy integration with other applications.

### 5. **Admin Panel Integration**

- Admins can upload and manage PDF files and their processed images through Django’s admin interface.

### 6. **Database Integration**

- Stores PDF files and associated metadata in a PostgreSQL database.
- Relational structure linking PDFs to their converted images.

### 7. **Dockerized Deployment**

- Includes a `Dockerfile` for containerized deployment.
- Compatible with hosting platforms like PythonAnywhere and Docker-based environments.

---

## Technologies Used

### Backend

- **Django** (5.1.4): Framework for building the application.
- **Django REST Framework**: To create APIs for external access.

### Database

- **PostgreSQL**: Relational database for storing PDF metadata and image details.

### PDF & Image Processing

- **PyMuPDF (Fitz)**: For PDF parsing and image extraction.

### Deployment

- **Docker**: For creating portable and consistent development environments.
- **PythonAnywhere**: For hosting the application.

---

## Installation and Setup

### Prerequisites

- Python 3.12 or above.
- PostgreSQL.
- Docker (optional for containerized deployment).

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Mina133/RDI.git
   cd document-processing-app
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   Update the `DATABASES` section in `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Server**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000`.

---

## API Endpoints

### PDF File Management

- **Upload PDF:**
  ```
  POST /api/upload-pdf/
  ```
- **List PDFs:**
  ```
  GET /api/list-pdfs/
  ```

### PDF to Image Conversion

- **Convert PDF to Images:**
  ```
  POST /api/convert-pdf-to-image/
  ```
- **Retrieve Images:**
  ```
  GET /api/images/
  ```

### Image Rotation

- **Rotate Image:**
  ```
  POST /api/rotate-image/
  ```

---

## Project Structure

```
Document_processing/
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── Document_processing/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
├── templates/
├── manage.py
└── Dockerfile
```

---

## Deployment

### Docker Deployment

1. **Build the Docker Image**

   ```bash
   docker build -t document-processing-app .
   ```

2. **Run the Container**

   ```bash
   docker run -p 8000:8000 document-processing-app
   ```

### Deploy on PythonAnywhere

1. Upload the project files to PythonAnywhere.
2. Set up a virtual environment and install dependencies.
3. Configure PostgreSQL settings in `settings.py`.
4. Set up a web application and link it to the `wsgi.py` file.

---

## Future Enhancements

- Add OCR capabilities to extract text from images.
- Support additional file formats like Word and Excel.
- Implement user authentication and role-based access control.
- Add frontend with React or Vue.js for better user experience.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

Special thanks to the open-source community for providing the tools and libraries that made this project possible.

