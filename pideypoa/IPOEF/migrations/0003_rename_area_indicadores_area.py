# Generated by Django 3.2.8 on 2023-05-24 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPOEF', '0002_rename_area_indicadores_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicadores',
            old_name='Area',
            new_name='area',
        ),
    ]