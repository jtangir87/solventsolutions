from django import forms


class EstimateForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    city = forms.CharField(max_length=150, required=False)
    state = forms.CharField(max_length=100, required=False)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "How can we help?"}), required=False
    )


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "How can we help?"})
    )
