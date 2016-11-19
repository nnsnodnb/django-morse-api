from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^alphabet', views.alphabet, name = 'alphabet'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
