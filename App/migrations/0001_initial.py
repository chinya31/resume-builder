# Generated by Django 3.2.4 on 2021-07-10 07:54

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('skills', models.CharField(max_length=100)),
                ('about_you', models.CharField(max_length=300)),
                ('career', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=300)),
            ],
        ),
    ]
