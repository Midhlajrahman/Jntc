from django import forms

from .models import BEdStudent


class StudentResultForm(forms.Form):
    exam_id = forms.CharField(widget=forms.HiddenInput(attrs={"id": "exam_id"}))
    register_no = forms.CharField(
        label="Register No:",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your Register Number",
                "id": "register_no",
                "maxlength": "21",
            }
        ),
    )
    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(
            attrs={
                "placeholder": "Enter your Date of Birth",
                "id": "date_of_birth",
                "type": "text",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        exam_id = cleaned_data.get("exam_id")
        register_no = cleaned_data.get("register_no")
        date_of_birth = cleaned_data.get("date_of_birth")

        if (
            register_no
            and not BEdStudent.objects.filter(
                results__id=exam_id, register_number=register_no
            ).exists()
        ):
            self.add_error("register_no", "Invalid Register Number")

        if (
            date_of_birth
            and not BEdStudent.objects.filter(
                results__id=exam_id, date_of_birth=date_of_birth
            ).exists()
        ):
            self.add_error("date_of_birth", "Invalid Date of Birth")
