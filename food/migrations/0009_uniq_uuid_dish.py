# Generated by Django 5.1.1 on 2024-12-14 17:24
import uuid

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_gen_uuid_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
