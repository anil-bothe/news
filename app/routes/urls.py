from django.urls import path

from app.controllers.news import about, contact, faqs, home


urlpatterns = [
    path("", home, name="home"),
    path("adsfalkjasd kfjaslkd fjalsdkjf laskjdflk asjdfl aldkfj lasdkjf laksdjfla ksdflk jasldkfj lasdkjf/", about, name='about'),
    path("fsdfaqasdfs/", faqs, name="faqs"),
    path("asdf/", contact, name="contact"),
]

    