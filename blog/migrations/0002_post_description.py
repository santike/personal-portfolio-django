# Generated by Django 4.1.6 on 2023-02-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
