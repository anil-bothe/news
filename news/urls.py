from django.contrib import admin
from django.urls import path, include

from app.controllers.news import about, contact, faqs, home


urlpatterns = [
    path('admin/', admin.site.urls),
    # our app urls
    path("", include("app.routes.urls")), 
]
