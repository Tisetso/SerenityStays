import os

# Define BASE_DIR at the top of your settings.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'listings',  # Register our app
]

# Add Stripe keys (replace these with your actual keys when going live)
STRIPE_PUBLIC_KEY = 'pk_test_51Q02leEvFmUjZecbk73tq3DYiYditxO1Zpsl0XaTtjgEqrhmKwDwYLsfD4WtzXLx1eq2n7TDa6k9dHwq3HTjoaZ200mlkUW9Fr'
STRIPE_SECRET_KEY = 'sk_test_51Q02leEvFmUjZecbAq6t6b2lJfGpWirgYCIdv60GrM7TfA9cdVLP6q9XeJVpGYnSntTogEdvdGcvvxb2navO7PSK00jCbae43W'

# Set up PostgreSQL (Make sure you have PostgreSQL installed)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'serenity_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
