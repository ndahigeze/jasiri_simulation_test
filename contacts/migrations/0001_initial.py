# Generated by Django 3.2.6 on 2021-11-29 16:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('deleted_status', models.BooleanField(default=False)),
                ('doneAt', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now_add=True)),
                ('done_by', models.CharField(editable=False, max_length=255)),
                ('last_updated_by', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
