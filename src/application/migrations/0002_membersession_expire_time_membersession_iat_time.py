# Generated by Django 4.1.5 on 2023-01-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersession',
            name='expire_time',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membersession',
            name='iat_time',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]