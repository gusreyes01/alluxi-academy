# Generated by Django 2.0.1 on 2019-09-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20190909_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='careers',
            field=models.ManyToManyField(blank=True, to='landing.Career'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='github_account',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='indeed_account',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='last_second_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='phase',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
