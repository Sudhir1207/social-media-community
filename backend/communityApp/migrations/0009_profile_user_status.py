# Generated by Django 5.1.6 on 2025-02-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityApp', '0008_community_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_status',
            field=models.BooleanField(default=False),
        ),
    ]
