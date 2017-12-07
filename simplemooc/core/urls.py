from django.conf.urls import url, include

from simplemooc.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contact, name='contact'),
]
