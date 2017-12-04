from django.conf.urls import url, include
from django.contrib import admin

from simplemooc.core import views, urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(urls, namespace='core')),
]
