# Generated by Django 2.1.2 on 2019-07-11 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0008_auto_20190711_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='info',
        ),
    ]
