# Generated by Django 3.2.4 on 2021-08-04 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210804_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='like',
        ),
        migrations.RemoveField(
            model_name='board',
            name='like_count',
        ),
    ]
