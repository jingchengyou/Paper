# Generated by Django 2.0.5 on 2018-05-31 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
    ]
