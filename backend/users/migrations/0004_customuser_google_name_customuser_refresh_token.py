# Generated by Django 5.1.5 on 2025-02-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_email_verification_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='google_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='refresh_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
