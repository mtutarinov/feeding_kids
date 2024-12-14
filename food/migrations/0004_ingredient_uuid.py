import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_dishhistory_uniq_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
