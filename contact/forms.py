from django import forms

from .models import ContactUsEnquiry


class ContactUsEnquiryForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"id": "email", "class": "input", "placeholder": "Email"}
        )
    )

    class Meta:
        model = ContactUsEnquiry
        fields = ["first_name", "last_name", "email", "phone_number", "message"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "id": "first_name",
                    "class": "input",
                    "placeholder": "First name",
                    "oninput": "removeSpecialCharacters(this)",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "id": "last_name",
                    "class": "input",
                    "placeholder": "Last name",
                    "oninput": "removeSpecialCharacters(this)",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "id": "phone_number",
                    "class": "input",
                    "placeholder": "Phone number",
                }
            ),
            "message": forms.Textarea(
                attrs={"id": "message", "class": "input", "placeholder": "Message"}
            ),
        }
