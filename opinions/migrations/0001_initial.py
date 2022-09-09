# Generated by Django 3.2.14 on 2022-09-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('advise', models.CharField(max_length=200)),
                ('client_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]