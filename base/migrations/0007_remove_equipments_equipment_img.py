# Generated by Django 3.2.8 on 2022-04-19 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_equipments_equipment_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipments',
            name='equipment_img',
        ),
    ]
