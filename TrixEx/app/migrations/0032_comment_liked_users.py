# Generated by Django 5.0.1 on 2024-01-18 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_comments', to='app.user'),
        ),
    ]