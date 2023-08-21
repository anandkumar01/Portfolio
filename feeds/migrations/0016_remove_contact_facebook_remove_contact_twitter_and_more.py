# Generated by Django 4.0.5 on 2023-08-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0015_alter_about_about_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='personalinformation',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='personalinformation',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='image',
        ),
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='skill',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
