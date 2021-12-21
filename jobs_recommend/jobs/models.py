from django.db import models


class JobsData(models.Model):
    jobid = models.CharField(primary_key=True, max_length=255)
    job_href = models.CharField(max_length=255)
    job_name = models.CharField(max_length=255)
    company_href = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    providesalary = models.CharField(max_length=255, blank=True, null=True)
    workarea = models.CharField(max_length=255, blank=True, null=True)
    company_type = models.CharField(max_length=255, blank=True, null=True)
    jobwelf = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    companysize = models.CharField(max_length=255, blank=True, null=True)
    companyind = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs_data'