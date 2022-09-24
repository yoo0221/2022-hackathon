# Generated by Django 4.1.1 on 2022-09-24 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_adminplacecomment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='scrap_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('hashtag', models.CharField(max_length=100, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
    ]