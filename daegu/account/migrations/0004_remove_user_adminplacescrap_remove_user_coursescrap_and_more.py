# Generated by Django 4.1.1 on 2022-09-24 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_adminplacescrap_alter_user_coursescrap_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='adminplacescrap',
        ),
        migrations.RemoveField(
            model_name='user',
            name='coursescrap',
        ),
        migrations.RemoveField(
            model_name='user',
            name='placescrap',
        ),
    ]
