# Generated by Django 4.1.7 on 2023-04-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_remove_job_company_remove_job_levels_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='working_time',
            field=models.CharField(blank=True, choices=[('t2_t6', 'Monday - Friday'), ('t2_t7', 'Monday - Saturday')], max_length=200, null=True),
        ),
    ]