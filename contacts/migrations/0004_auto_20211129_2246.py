# Generated by Django 3.2.6 on 2021-11-29 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contactemail_contactphone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactemail',
            old_name='contact_id',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='contactphone',
            old_name='contact_id',
            new_name='contact',
        ),
    ]
