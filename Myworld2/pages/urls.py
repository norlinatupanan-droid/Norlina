from django.urls import path

from .views import ContactView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
]
