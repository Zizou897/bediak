from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('detail', blogDetail, name="detail-blog"),
    path('blog', blog, name="blog"),
    path('contact', contact, name="contact"),
    path('about', about, name="about"),
]
