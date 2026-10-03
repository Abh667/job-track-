from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import JobApplication
from .forms import JobApplicationForm


@login_required
def dashboard(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    ).order_by("-created_at")

    context = {
        "total_jobs": jobs.count(),

        "applied": jobs.filter(
            status="Applied"
        ).count(),

        "interviews": jobs.filter(
            status__in=[
                "Technical Interview",
                "HR Interview"
            ]
        ).count(),

        "selected": jobs.filter(
            status="Selected"
        ).count(),

        "rejected": jobs.filter(
            status="Rejected"
        ).count(),

        "recent_jobs": jobs[:5],
    }

    return render(
        request,
        "jobs/dashboard.html",
        context
    )


@login_required
def job_list(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    ).order_by("-applied_date")

    search = request.GET.get("search")

    if search:
        jobs = jobs.filter(
            company_name__icontains=search
        ) | jobs.filter(
            job_title__icontains=search
        )

    status = request.GET.get("status")

    if status:
        jobs = jobs.filter(status=status)

    return render(
        request,
        "jobs/job_list.html",
        {
            "jobs": jobs
        }
    )


@login_required
def job_detail(request, pk):

    job = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "jobs/job_detail.html",
        {
            "job": job
        }
    )


@login_required
def add_job(request):

    if request.method == "POST":

        form = JobApplicationForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)
            job.user = request.user
            job.save()

            return redirect("job_list")

    else:

        form = JobApplicationForm()

    return render(
        request,
        "jobs/job_form.html",
        {
            "form": form,
            "title": "Add Job"
        }
    )


@login_required
def edit_job(request, pk):

    job = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = JobApplicationForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            return redirect(
                "job_detail",
                pk=job.pk
            )

    else:

        form = JobApplicationForm(
            instance=job
        )

    return render(
        request,
        "jobs/job_form.html",
        {
            "form": form,
            "title": "Edit Job"
        }
    )


@login_required
def delete_job(request, pk):

    job = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        job.delete()

        return redirect("job_list")

    return render(
        request,
        "jobs/job_confirm_delete.html",
        {
            "job": job
        }
    )