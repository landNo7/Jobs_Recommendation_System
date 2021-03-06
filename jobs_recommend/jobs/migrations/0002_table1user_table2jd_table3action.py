# Generated by Django 3.2.10 on 2021-12-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table1User',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('live_city_id', models.CharField(blank=True, max_length=255, null=True)),
                ('desire_jd_city_id', models.CharField(blank=True, max_length=255, null=True)),
                ('desire_jd_industry_id', models.CharField(blank=True, max_length=255, null=True)),
                ('desire_jd_type_id', models.CharField(blank=True, max_length=255, null=True)),
                ('desire_jd_salary_id', models.CharField(blank=True, max_length=255, null=True)),
                ('cur_industry_id', models.CharField(blank=True, max_length=255, null=True)),
                ('cur_jd_type', models.CharField(blank=True, max_length=255, null=True)),
                ('cur_salary_id', models.CharField(blank=True, max_length=255, null=True)),
                ('cur_degree_id', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.CharField(blank=True, max_length=255, null=True)),
                ('start_work_date', models.CharField(blank=True, max_length=255, null=True)),
                ('experience', models.TextField(blank=True, db_collation='utf16_general_ci', null=True)),
            ],
            options={
                'db_table': 'table1_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Table2Jd',
            fields=[
                ('jd_no', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('jd_title', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('jd_sub_type', models.CharField(blank=True, max_length=255, null=True)),
                ('require_nums', models.CharField(blank=True, max_length=255, null=True)),
                ('max_salary', models.CharField(blank=True, max_length=255, null=True)),
                ('min_salary', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('end_date', models.CharField(blank=True, max_length=255, null=True)),
                ('is_travel', models.CharField(blank=True, max_length=255, null=True)),
                ('min_years', models.CharField(blank=True, max_length=255, null=True)),
                ('key', models.CharField(blank=True, max_length=255, null=True)),
                ('min_edu_level', models.CharField(blank=True, max_length=255, null=True)),
                ('max_edu_level', models.CharField(blank=True, max_length=255, null=True)),
                ('is_mangerial', models.CharField(blank=True, max_length=255, null=True)),
                ('resume_language_required', models.CharField(blank=True, max_length=255, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'table2_jd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Table3Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('jd_no', models.CharField(blank=True, max_length=255, null=True)),
                ('browsed', models.CharField(blank=True, max_length=255, null=True)),
                ('delivered', models.CharField(blank=True, max_length=255, null=True)),
                ('satisfied', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'table3_action',
                'managed': False,
            },
        ),
    ]
