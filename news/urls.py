from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from app.views import about, contact, faqs, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("adsfalkjasd kfjaslkd fjalsdkjf laskjdflk asjdfl aldkfj lasdkjf laksdjfla ksdflk jasldkfj lasdkjf/", about, name='about'),
    path("fsdfaqasdfs/", faqs, name="faqs"),
    path("asdf/", contact, name="contact"),
]
