# Generated by Django 4.1.1 on 2022-09-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_course_user_alter_place_course_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='hashtag',
        ),
        migrations.AddField(
            model_name='course',
            name='hashtag',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
