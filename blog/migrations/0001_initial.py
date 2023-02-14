# Generated by Django 4.1.6 on 2023-02-14 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='blog/iamges/')),
                ('date', models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]
