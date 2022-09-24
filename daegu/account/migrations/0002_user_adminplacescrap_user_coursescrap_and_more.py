# Generated by Django 4.1.1 on 2022-09-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_adminplace_address_adminplace_lat_adminplace_lng_and_more'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adminplacescrap',
            field=models.ManyToManyField(blank=True, null=True, related_name='scrapper', to='main.adminplace'),
        ),
        migrations.AddField(
            model_name='user',
            name='coursescrap',
            field=models.ManyToManyField(blank=True, null=True, related_name='scrapper', to='main.course'),
        ),
        migrations.AddField(
            model_name='user',
            name='placescrap',
            field=models.ManyToManyField(blank=True, null=True, related_name='scrapper', to='main.place'),
        ),
    ]
