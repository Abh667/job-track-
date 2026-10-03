from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Shortlisted", "Shortlisted"),
        ("Technical Interview", "Technical Interview"),
        ("HR Interview", "HR Interview"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
    ]

    JOB_TYPE_CHOICES = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Internship", "Internship"),
        ("Contract", "Contract"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job_applications"
    )

    company_name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    location = models.CharField(max_length=100, blank=True)
    job_type = models.CharField(
        max_length=50,
        choices=JOB_TYPE_CHOICES,
        default="Full Time"
    )

    salary = models.CharField(max_length=100, blank=True)
    job_url = models.URLField(blank=True)

    applied_date = models.DateField()

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Applied"
    )

    interview_date = models.DateField(null=True, blank=True)

    interview_round = models.CharField(
        max_length=100,
        blank=True
    )

    interview_mode = models.CharField(
        max_length=50,
        blank=True
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
