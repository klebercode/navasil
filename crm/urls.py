from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.register_models()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(xadmin.site.urls))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
