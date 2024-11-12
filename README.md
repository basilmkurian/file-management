# Introduction to File Management & Celery

## 1. Introduction to Static Files in Django

- Purpose of static files (CSS, JavaScript)
- Configuring Django to serve static files
- `django.contrib.staticfiles` and usage of `collectstatic`

## 2. Serving Media Files

- Difference between static and media files
- Configuring media files in Django (MEDIA_URL, MEDIA_ROOT)
- Serving media files in development vs. production

## 3. Asynchronous Tasks with Celery
- Purpose of Asynchronous Tasks: Improving user experience by offloading tasks.
- Setting Up Celery with Django:
  - Basic Celery installation and setup with a celery.py file in the project.
- Creating and Running Tasks:
  - Using `@shared_task` for background tasks (e.g., sending emails).
- Message Broker Options:
  - Introduction to Redis and RabbitMQ and their configuration as Celery brokers.
"# file-management" 
