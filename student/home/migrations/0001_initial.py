# Generated by Django 4.1.3 on 2022-12-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=20)),
                ('student_phone', models.CharField(max_length=10)),
                ('student_email', models.CharField(max_length=100)),
                ('student_address', models.CharField(max_length=100)),
                ('student_place', models.CharField(max_length=100)),
            ],
        ),
    ]
