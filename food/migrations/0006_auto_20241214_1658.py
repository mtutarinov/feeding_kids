# Generated by Django 5.1.1 on 2024-12-14 16:58
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20241214_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
