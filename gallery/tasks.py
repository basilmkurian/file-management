import time
from celery import shared_task
from django.core.mail import send_mail
from celery import shared_task
from PIL import Image
from io import BytesIO
import os
from django.conf import settings
from .models import Photo
from django.core.files.uploadedfile import InMemoryUploadedFile


def send_welcome_mail_realtime():
    time.sleep(5)
    send_mail(
        "Welcome!",
        "Thanks for uploading a photo! This mail was send in realtime.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )


@shared_task
def send_welcome_email_async():
    time.sleep(5)
    send_mail(
        "Welcome!",
        "Thanks for uploading a photo! This mail was send asynchronously.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )


 
@shared_task
def generate_thumbnail(photo_id):
    photo = Photo.objects.get(id=photo_id)
    image_path = photo.image.path
    img = Image.open(image_path)
    thumbnail_size = (100, 100)
    img.thumbnail(thumbnail_size)
    thumb_io = BytesIO()
    img.save(thumb_io, img.format)
    thumb_io.seek(0)
    photo.thumbnail.save(
        os.path.basename(photo.image.name),
        InMemoryUploadedFile(
            thumb_io, None, photo.image.name, 'image/jpeg', thumb_io.getbuffer().nbytes, None
        ),
        save=True
    )