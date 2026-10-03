from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            "company_name",
            "job_title",
            "location",
            "job_type",
            "salary",
            "job_url",
            "applied_date",
            "status",
            "interview_date",
            "interview_round",
            "interview_mode",
            "notes",
        ]

        widgets = {
            "applied_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "interview_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "notes": forms.Textarea(
                attrs={"rows": 4}
            ),
        }