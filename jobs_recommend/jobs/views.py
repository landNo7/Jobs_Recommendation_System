from django.shortcuts import render
from jobs import models
from django.http import JsonResponse
from predictmodel.Round1.predict import pred
# Create your views here.

def jobs_list(request):
	jobs_queryset = models.JobsData.objects.all()
	return render(request,"jobs_list.html",{"jobs_queryset":jobs_queryset})

def predict(request):
	ret_mes = {}
	ret_mes['issucceed'] = 0
	if request.method == "POST":
		userInfo = request.POST["userInfo"]
		jobs = pred(userInfo)
		ret_mes['jobs'] = jobs
		ret_mes['issucceed'] = 1

	return JsonResponse(ret_msg, safe=False)

