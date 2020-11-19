from django.shortcuts import render

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import send_mail

from .forms import EstimateForm, ContactUsForm

# Create your views here.
def estimate_request(request):
    data = dict()
    if request.method == "POST":
        form = EstimateForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            context = {
                "name": name,
                "email": email,
                "phone": form.cleaned_data["phone"],
                "city": form.cleaned_data["city"],
                "state": form.cleaned_data["state"],
                "message": form.cleaned_data["message"],
            }

            ### SEND EMAIL ###

            template = get_template("pages/emails/estimate_request.txt")
            content = template.render(context)
            send_mail(
                "NEW ESTIMATE REQUEST",
                content,
                "{}<{}>".format(name, email),
                ["service@solventsolutionsus.com"],
                fail_silently=False,
            )

            data["html_success_message"] = render_to_string(
                "pages/includes/partial_estimate_submit_success.html",
                request=request,
            )
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
    else:
        estimate_form = EstimateForm()
        data["html_form"] = render_to_string(
            "pages/includes/partial_estimate_form.html",
            {"estimate_form": estimate_form},
            request=request,
        )
    return JsonResponse(data)


def contact_us_form(request):
    data = dict()
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            context = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": form.cleaned_data["message"],
            }

            ### SEND EMAIL ###

            template = get_template("pages/emails/contact_us.txt")
            content = template.render(context)
            send_mail(
                "NEW CONTACT REQUEST",
                content,
                "WEBSITE REQUEST<donotreply@solventsolutionsus.com>",
                ["service@solventsolutionsus.com"],
                fail_silently=False,
            )

            data["html_success_message"] = render_to_string(
                "pages/includes/partial_contact_success.html",
                request=request,
            )
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
    return JsonResponse(data)