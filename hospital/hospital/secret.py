# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f645&z765$*n=+e!@o_p$-hnj$skbbvkyz71y*#nmm2@lw*yj@'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hospital',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }

}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'

STATIC_URL = '/static/'

STATIC_ROOT = 'static'