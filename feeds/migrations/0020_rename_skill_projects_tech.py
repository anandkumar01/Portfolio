# Generated by Django 4.0.5 on 2023-08-23 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0019_rename_num_skills_percent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='skill',
            new_name='tech',
        ),
    ]
