# Generated by Django 3.0.4 on 2020-03-20 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200319_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothesset',
            old_name='chothes',
            new_name='clothes',
        ),
    ]
