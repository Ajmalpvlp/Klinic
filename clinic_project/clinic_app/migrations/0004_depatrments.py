# Generated by Django 4.2.6 on 2023-10-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0003_rename_messageq_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depatrments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
