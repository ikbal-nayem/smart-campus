# Generated by Django 3.0.6 on 2020-06-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200609_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(default='abc', max_length=100, null=True),
        ),
    ]
