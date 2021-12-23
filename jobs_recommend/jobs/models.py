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


class Table1User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    live_city_id = models.CharField(max_length=255, blank=True, null=True)
    desire_jd_city_id = models.CharField(max_length=255, blank=True, null=True)
    desire_jd_industry_id = models.CharField(max_length=255, blank=True, null=True)
    desire_jd_type_id = models.CharField(max_length=255, blank=True, null=True)
    desire_jd_salary_id = models.CharField(max_length=255, blank=True, null=True)
    cur_industry_id = models.CharField(max_length=255, blank=True, null=True)
    cur_jd_type = models.CharField(max_length=255, blank=True, null=True)
    cur_salary_id = models.CharField(max_length=255, blank=True, null=True)
    cur_degree_id = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    start_work_date = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(db_collation='utf16_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table1_user'


class Table2Jd(models.Model):
    jd_no = models.CharField(primary_key=True, max_length=255)
    jd_title = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    jd_sub_type = models.CharField(max_length=255, blank=True, null=True)
    require_nums = models.CharField(max_length=255, blank=True, null=True)
    max_salary = models.CharField(max_length=255, blank=True, null=True)
    min_salary = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.CharField(max_length=255, blank=True, null=True)
    end_date = models.CharField(max_length=255, blank=True, null=True)
    is_travel = models.CharField(max_length=255, blank=True, null=True)
    min_years = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    min_edu_level = models.CharField(max_length=255, blank=True, null=True)
    max_edu_level = models.CharField(max_length=255, blank=True, null=True)
    is_mangerial = models.CharField(max_length=255, blank=True, null=True)
    resume_language_required = models.CharField(max_length=255, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table2_jd'


class Table3Action(models.Model):
    user_id = models.CharField(max_length=255, blank=True, null=True)
    jd_no = models.CharField(max_length=255, blank=True, null=True)
    browsed = models.CharField(max_length=255, blank=True, null=True)
    delivered = models.CharField(max_length=255, blank=True, null=True)
    satisfied = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table3_action'


def mysql_search_by_jobid(database, keystring):
	return database.objects.filter(jobid=keystring)

def mysql_search_count(database):
	return database.objects.count()