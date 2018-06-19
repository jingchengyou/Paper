# Generated by Django 2.0.5 on 2018-05-17 09:45

from django.db import migrations, models
import django.db.models.deletion
import mysite.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('telephone', models.CharField(max_length=15, unique=True)),
                ('nickname', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('upload', models.FileField(upload_to=mysite.models.user_directory_path)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Author')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ManyToManyField(to='mysite.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('summary', models.TextField(max_length=1000)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Author')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='novel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Novel'),
        ),
    ]
