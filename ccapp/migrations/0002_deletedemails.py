# Generated by Django 3.0.7 on 2020-10-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]