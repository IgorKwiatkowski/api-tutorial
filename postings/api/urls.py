from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import BlogPostRudView

app_name = 'api'

urlpatterns = [
    url(r'^(?P<pk>(\d)+)/$', BlogPostRudView.as_view(), name='post-rud'),
]