# Generated by Django 5.2 on 2025-05-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0004_alter_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
