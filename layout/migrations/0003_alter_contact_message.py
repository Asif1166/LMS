# Generated by Django 4.1.1 on 2022-09-29 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0002_contact_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
