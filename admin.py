from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "job_title",
        "status",
        "applied_date",
        "interview_date",
    )

    list_filter = (
        "status",
        "job_type",
    )

    search_fields = (
        "company_name",
        "job_title",
        "location",
    )