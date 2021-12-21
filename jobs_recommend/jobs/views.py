from django.shortcuts import render
from jobs import models

# Create your views here.
def jobs_list(request):
	jobs_queryset = models.JobsData.objects.all()
	return render(request,"jobs_list.html",{"jobs_queryset":jobs_queryset})