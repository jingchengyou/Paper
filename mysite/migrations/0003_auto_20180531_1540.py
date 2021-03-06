# Generated by Django 2.0.5 on 2018-05-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_author_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(default=None, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='password',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
