# Generated by Django 5.1.6 on 2025-03-10 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name']},
        ),
    ]
