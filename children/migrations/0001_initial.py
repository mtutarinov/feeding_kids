# Generated by Django 5.1.1 on 2024-12-07 11:24

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('months', models.IntegerField(blank=True, null=True)),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]