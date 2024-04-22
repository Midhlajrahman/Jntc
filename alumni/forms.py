from django import forms
from django.utils.translation import gettext_lazy as _

from .models import AlumniNetworkRegistration


class RegistrationForm1(forms.ModelForm):
    class Meta:
        model = AlumniNetworkRegistration
        fields = [
            "first_name",
            "last_name",
            "gender",
            "marital_status",
            "phone_number",
            "email",
            "address",
            "image",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"id": "first_name", "oninput": "removeSpecialCharacters(this)"}
            ),
            "last_name": forms.TextInput(
                attrs={"id": "last_name", "oninput": "removeSpecialCharacters(this)"}
            ),
            "phone_number": forms.TextInput(attrs={"id": "phone_number"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gender"].empty_label = "Select"
        self.fields["marital_status"].empty_label = "Select"

        placeholders = {
            "first_name": "Enter your first name",
            "last_name": "Enter your last name",
            "gender": "Select",
            "marital_status": "Select",
            "email": "Enter your email",
            "phone_number": "Enter your Phone number",
            "address": "Enter here",
        }

        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update(
                {
                    "id": field_name,
                    "class": "input",
                    "placeholder": placeholders.get(field_name, ""),
                }
            )

        self.fields["address"].widget.attrs.update(
            {"class": "input", "rows": 3, "cols": 61, "placeholder": "Enter here"}
        )

    def clean(self):
        cleaned_data = super().clean()

        phone_number = cleaned_data.get("phone_number")
        email = cleaned_data.get("email")

        # Check if phone_number or email already exists in the database
        if (
            phone_number
            and AlumniNetworkRegistration.objects.filter(
                phone_number=phone_number
            ).exists()
        ):
            self.add_error("phone_number", _("Phone number already exists."))

        if email and AlumniNetworkRegistration.objects.filter(email=email).exists():
            self.add_error("email", _("Email already exists."))

        return cleaned_data


class RegistrationForm2(forms.ModelForm):
    class Meta:
        model = AlumniNetworkRegistration
        fields = ["b_ed_subject", "year_of_study", "educational_status"]
        widgets = {
            "b_ed_subject": forms.Select(
                attrs={"id": "b_ed_subject", "class": "input"}
            ),
            "year_of_study": forms.Select(
                attrs={"id": "year_of_study", "class": "input"}
            ),
            "educational_status": forms.Select(
                attrs={"id": "educational_status", "class": "input"}
            ),
        }
        labels = {
            "b_ed_subject": "B.Ed. subject",
            "year_of_study": "Year of study",
            "educational_status": "Present educational status",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["b_ed_subject"].empty_label = "Select"
        self.fields["year_of_study"].empty_label = "Select"
        self.fields["educational_status"].empty_label = "Select"


class RegistrationForm3(forms.ModelForm):
    class Meta:
        model = AlumniNetworkRegistration
        fields = ["jntc_period", "suggestion"]
        labels = {
            "jntc_period": ("Fondest memories of JNTC period"),
            "suggestion": ("Suggestions"),
        }
        widgets = {
            "jntc_period": forms.Textarea(
                attrs={
                    "id": "jntc_period",
                    "class": "input text-area",
                    "placeholder": "What are your favorite memories from   your time at JNTC?",
                    "rows": 4,
                    "cols": 61,
                }
            ),
            "suggestion": forms.Textarea(
                attrs={
                    "id": "suggestion",
                    "class": "input area",
                    "placeholder": "Enter here",
                    "rows": 4,
                    "cols": 61,
                }
            ),
        }
