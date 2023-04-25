# Generated by Django 4.2 on 2023-04-25 22:16

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=1, related_name='patient_record', serialize=False, to='Hospital.patient')),
                ('diagnosis', models.TextField()),
                ('allergies', models.TextField()),
                ('family_history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('height', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField()),
                ('blood_pressure', models.PositiveSmallIntegerField()),
                ('heart_rate', models.PositiveSmallIntegerField()),
                ('temperature', models.PositiveSmallIntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_vital', to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveSmallIntegerField()),
                ('bed_number', models.PositiveSmallIntegerField()),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField()),
                ('diagnosis', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patient_doctor', to='Hospital.doctor')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patient_nurse', to='Hospital.nurse')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inpatient', to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='SurgeryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surgery_type', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('documentation', models.FileField(upload_to='')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='surgeon', to='Hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_surgery', to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=1, max_length=254, null=1, unique=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('relative_relation', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Cousin', 'Cousin'), ('Sister', 'Sister'), ('Brother', 'Brother'), ('Aunt', 'Aunt'), ('Uncle', 'Uncle'), ('Grandfather', 'Grandfather'), ('Grandmother', 'Grandmother'), ('Husband', 'Husband'), ('Wife', 'Wife'), ('Others', 'Others')], max_length=12)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_emergency_conact', to='Hospital.patient')),
            ],
        ),
    ]
