# Generated by Django 4.2.5 on 2023-10-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Mail', models.EmailField(max_length=100)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=1000)),
            ],
        ),
    ]
