# Generated by Django 5.0.1 on 2024-01-18 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_user_motto'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='views',
            field=models.FloatField(default=0),
        ),
    ]