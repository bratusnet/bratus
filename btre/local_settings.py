# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kpzx7vt3#51ue1)oepnq1=4jix4jv*3gfx*k3his&1bm+rx7ay'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['167.71.113.107']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bratus',
        'USER': 'dbadmin',
        'PASSWORD': 'nescafe40$',
        'HOST': 'localhost',
    }
}
