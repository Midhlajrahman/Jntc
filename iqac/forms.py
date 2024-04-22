from django import forms

from .models import IQACComplaint


class IQACComplaintForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "id": "first_name",
                "placeholder": "Enter your first name",
                "oninput": "removeSpecialCharacters(this)",
            }
        ),
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "id": "last_name",
                "placeholder": "Enter your last name",
                "oninput": "removeSpecialCharacters(this)",
            }
        ),
    )
    complaint = forms.CharField(
        label="Complaint",
        widget=forms.Textarea(
            attrs={"class": "input", "id": "complaint", "placeholder": "Enter here"}
        ),
    )

    class Meta:
        model = IQACComplaint
        fields = ["first_name", "last_name", "year_of_batch", "subject", "complaint"]
        widgets = {
            "year_of_batch": forms.Select(
                attrs={"class": "input", "id": "year_of_batch"}
            ),
            "subject": forms.Select(attrs={"class": "input", "id": "subject"}),
        }
        labels = {"year_of_batch": "Batch year", "subject": "Subject"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["year_of_batch"].empty_label = "Select"
        self.fields["subject"].empty_label = "Select"
