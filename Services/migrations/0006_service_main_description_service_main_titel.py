# Generated by Django 4.1 on 2022-10-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_service_feature_summery_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='main_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='main_titel',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
