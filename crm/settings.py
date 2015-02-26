# coding: utf-8
"""
Django settings for crm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
BASE_DIR = Path(__file__).parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '.localhost',
    '127.0.0.1',
    '.herokuapp.com',
    '.ow7.com.br',
]


# Application definition

INSTALLED_APPS = (
    # 'suit',

    'grappelli_extensions',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'xadmin',
    # 'crispy_forms',
    # 'reversion',
    'south',
    'import_export',

    'crm.core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'crm.current_user.CurrentUserMiddleware',
)

ROOT_URLCONF = 'crm.urls'

WSGI_APPLICATION = 'crm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEFAULT_FROM_EMAIL = 'Prefeitura de Palmeirina <no-reply@palmeirina.pe.gov.br>'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtpi.kinghost.net'
# EMAIL_HOST_USER = 'contato@palmeirina.pe.gov.br'
# EMAIL_HOST_PASSWORD = 'pmsAl@9090'
# EMAIL_PORT = 587


# django-tinymce
# TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'theme_advanced_buttons1': "cut,copy,paste,|,undo,redo,|,cleanup,|,bold,\
                                italic,underline,strikethrough,|,forecolor,\
                                backcolor,|,justifyleft,justifycenter,\
                                justifyright,justifyfull,|,help,|,code",
    'theme_advanced_buttons2': "removeformat,formatselect,fontsizeselect,|,\
                                bullist,numlist,outdent,indent,|,link,unlink,\
                                anchor,sub,sup,|,hr,advhr,visualaid,|,image,\
                                media,|,preview,",
    'height': '350',
    'file_browser_callback': 'mce_filebrowser',
}


# grappelli
GRAPPELLI_ADMIN_TITLE = 'OW7 | CRM'

# GRAPPELLI_EXTENSIONS_NAVBAR = 'pmsal.extensions.Navbar'

# GRAPPELLI_EXTENSIONS_SIDEBAR = 'pmsal.extensions.Sidebar'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


# south {taggit}
SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

# # filebrowser
# FILEBROWSER_MEDIA_URL = MEDIA_URL
# FILEBROWSER_URL_FILEBROWSER_MEDIA = MEDIA_URL + 'filebrowser/'
# FILEBROWSER_URL_TINYMCE = MEDIA_URL + "/tiny_mce/"
# FILEBROWSER_PATH_TINYMCE = "tiny_mce/"


# Templates
TEMPLATE_DIRS = (
    BASE_DIR.child('core', 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
