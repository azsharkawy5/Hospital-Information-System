# Generated by Django 4.2 on 2023-04-19 19:16

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
        ('Records', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='phone',
            new_name='phone_1',
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='address',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contact_address', to='Hospital.address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='phone_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=1, max_length=128, null=1, region=None),
            preserve_default=1,
        ),
    ]
