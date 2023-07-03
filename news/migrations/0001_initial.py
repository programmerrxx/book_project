# Generated by Django 4.2.2 on 2023-07-03 03:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('lname', models.CharField(default='', max_length=60)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('position', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('newsdata', models.CharField(default='', max_length=900)),
                ('data_of_news', models.DateField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.authormodel')),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]