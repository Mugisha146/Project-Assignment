# Generated by Django 5.0 on 2023-12-19 16:27

import ValidationApp.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, validators=[ValidationApp.models.validate_email])),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(limit_value=6), ValidationApp.models.validate_phone, django.core.validators.RegexValidator(message='Invalid phone number format.', regex='^\\+\\d{1,15}$')])),
                ('birth_date', models.DateField(validators=[ValidationApp.models.validate_birth_date])),
                ('reference_number', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(limit_value=3), ValidationApp.models.validate_reference_number])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('plate_type', models.CharField(choices=[('GR', 'Government (GR)'), ('IT', 'Import Temporary (IT)'), ('RNP', 'Rwanda National Police (RNP)'), ('RDF', 'Rwanda Defence Force (RDF)'), ('CD', 'Ambassador (CD)'), ('RAA', 'RAA'), ('RAB', 'RAB'), ('RAC', 'RAC'), ('RAD', 'RAD'), ('RAE', 'RAE'), ('RAF', 'RAF'), ('RAG', 'RAG'), ('RAH', 'RAH')], max_length=3, validators=[ValidationApp.models.validate_plate_type], verbose_name='Plate Type')),
                ('plate_number', models.CharField(max_length=10, validators=[ValidationApp.models.validate_rwandan_plate_number])),
                ('car_color', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_manufacture_name', models.CharField(max_length=50)),
                ('car_manufacture_date', models.DateField(validators=[ValidationApp.models.validate_manufacture_date])),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_type', models.CharField(choices=[('GR', 'Government (GR)'), ('IT', 'Import Temporary (IT)'), ('RNP', 'Rwanda National Police (RNP)'), ('RDF', 'Rwanda Defence Force (RDF)'), ('CD', 'Ambassador (CD)'), ('RAA', 'RAA'), ('RAB', 'RAB'), ('RAC', 'RAC'), ('RAD', 'RAD'), ('RAE', 'RAE'), ('RAF', 'RAF'), ('RAG', 'RAG'), ('RAH', 'RAH')], max_length=3, validators=[ValidationApp.models.validate_plate_type], verbose_name='Plate Type')),
                ('plate_number', models.CharField(help_text='Enter a valid Rwandan plate number.', max_length=10, validators=[ValidationApp.models.validate_rwandan_plate_number])),
                ('car_color', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_manufacture_name', models.CharField(max_length=50)),
                ('car_manufacture_date', models.DateField(validators=[ValidationApp.models.validate_manufacture_date])),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ValidationApp.participant')),
            ],
        ),
    ]
