# Generated by Django 5.1.6 on 2025-03-14 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='commissions.commission'),
        ),
    ]
