# Generated by Django 5.0.6 on 2024-07-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangohelp', '0006_alter_auth_password_alter_auth_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='branch',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='auth',
            name='enroll',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='auth',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]
