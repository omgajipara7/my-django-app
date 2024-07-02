# Generated by Django 5.0.6 on 2024-06-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_rename_title_project_name_remove_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
    ]
