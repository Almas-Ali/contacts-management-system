from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ["created_at", "updated_at", "is_deleted", "deleted_at"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter first name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter last name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter phone number"}),
            "mobile": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter mobile number"}),
            "address": forms.Textarea(attrs={"rows": 3, "class": "form-control", "placeholder": "Enter address"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter city"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter state"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter zip code"}),
            "country": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter country"}),
            "notes": forms.Textarea(attrs={"rows": 3, "class": "form-control", "placeholder": "Enter notes"}),
        }
