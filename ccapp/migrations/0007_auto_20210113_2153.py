# Generated by Django 3.0.7 on 2021-01-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0006_calculator_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suit',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10),
        ),
    ]
