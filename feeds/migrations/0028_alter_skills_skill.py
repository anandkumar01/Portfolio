# Generated by Django 4.0.5 on 2024-10-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0027_rename_mini_about_personalinformation_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
