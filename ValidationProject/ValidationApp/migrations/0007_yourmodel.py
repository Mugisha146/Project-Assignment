# Generated by Django 5.0 on 2023-12-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValidationApp', '0006_alter_vehicle_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
