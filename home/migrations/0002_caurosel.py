# Generated by Django 4.1.1 on 2022-11-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caurosel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
