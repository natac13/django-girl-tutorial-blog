from django.urls import url
from . import views

urlpattterns = [
    url(r'^$', views.post_list, name='post_list'),
]
