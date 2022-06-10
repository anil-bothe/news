from django.contrib import admin
from django.urls import path

from app.views import about, contact, faqs, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("about/", about),
    path("faqs/", faqs),
    path("contact/", contact),
]
