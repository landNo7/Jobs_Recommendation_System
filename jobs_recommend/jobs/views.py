from django.shortcuts import render
from jobs import models
from django.http import JsonResponse
from predictmodel.views import pred
# Create your views here.

def jobs_list(request):
	jobs_queryset = models.JobsData.objects.all()
	return render(request,"jobs_list.html",{"jobs_queryset":jobs_queryset})

def predict(request):
	ret_msg = {}
	ret_msg['issucceed'] = 0
	# if request.method == "POST":
	# 	userInfo = request.POST["userInfo"]
	# 	jobs = pred(s=userInfo)
	# 	ret_msg['jobs'] = jobs
	# 	ret_msg['issucceed'] = 1
	jobs = pred()
	ret_msg['jobs'] = jobs
	ret_msg['issucceed'] = 1
	return render(request,"predict.html",{"ret_msg":jobs})

