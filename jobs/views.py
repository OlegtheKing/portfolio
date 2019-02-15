from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects  # collecting job objects from db
    return render(request, "jobs/home.html", {"jobs": jobs})
