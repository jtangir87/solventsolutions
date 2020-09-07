from django.urls import path, include

from django.views.generic import TemplateView

from .views import estimate_request, contact_us_form

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html")),
    path("estimate", estimate_request, name="estimate_request"),
    path("contact", contact_us_form, name="contact_us_form"),
]
