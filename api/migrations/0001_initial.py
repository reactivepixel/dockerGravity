# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SetlistPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('cycles', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Set')),
                ('setlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Setlist')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('image_path', models.ImageField(null=True, upload_to='uploads')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Set')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Track')),
            ],
        ),
        migrations.AddField(
            model_name='setlist',
            name='sets',
            field=models.ManyToManyField(through='api.SetlistPosition', to='api.Set'),
        ),
        migrations.AddField(
            model_name='set',
            name='tracks',
            field=models.ManyToManyField(through='api.TrackPosition', to='api.Track'),
        ),
    ]
