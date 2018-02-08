from django.conf.urls import url, include
from django.contrib import admin
from core.views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'core/', include('core.urls')),
]
