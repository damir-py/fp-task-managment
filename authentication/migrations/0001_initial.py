# Generated by Django 5.1.1 on 2024-10-07 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('deadline', models.DateTimeField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=14)),
                ('password', models.CharField(max_length=100)),
                ('role', models.IntegerField(choices=[(1, 'Manager'), (2, 'User')], default=2)),
                ('tasks', models.ManyToManyField(to='authentication.task')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
