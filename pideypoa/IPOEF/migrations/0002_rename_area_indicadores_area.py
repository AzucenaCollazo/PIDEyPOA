# Generated by Django 3.2.8 on 2023-05-24 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPOEF', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicadores',
            old_name='area',
            new_name='Area',
        ),
    ]