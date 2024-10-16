# Generated by Django 5.1.1 on 2024-10-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='dish',
            name='product',
            field=models.ManyToManyField(related_name='products', to='main_app.ingredient'),
        ),
    ]
