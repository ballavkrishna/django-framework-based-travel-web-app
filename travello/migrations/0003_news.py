# Generated by Django 3.0.7 on 2020-06-19 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('category', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
