# Generated by Django 3.1.5 on 2021-02-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0002_auto_20210203_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='confirmPassword',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='contactNumber',
            field=models.CharField(max_length=12),
        ),
    ]
