from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.AboutView, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]