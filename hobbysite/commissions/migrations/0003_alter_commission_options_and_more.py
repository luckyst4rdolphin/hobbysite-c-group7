# Generated by Django 5.1.6 on 2025-05-12 02:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0002_alter_comment_commission'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commission',
            options={'ordering': [models.Case(models.When(status='Open', then=0), models.When(status='Full', then=1), models.When(status='Completed', then=2), models.When(status='Discontinued', then=3), default=4, output_field=models.IntegerField()), 'created_on']},
        ),
        migrations.RemoveField(
            model_name='commission',
            name='people_required',
        ),
        migrations.AddField(
            model_name='commission',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='commission',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Full', 'Full'), ('Completed', 'Completed'), ('Discontinued', 'Discontinued')], default='Open', max_length=20),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('manpower_required', models.PositiveBigIntegerField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Full', 'Full')], default='Open', max_length=20)),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commissions.commission')),
            ],
            options={
                'ordering': [models.Case(models.When(status='Open', then=0), models.When(status='Full', then=1), default=2, output_field=models.IntegerField()), '-manpower_required', 'role'],
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commissions.job')),
            ],
            options={
                'ordering': [models.Case(models.When(status='Pending', then=0), models.When(status='Accepted', then=1), models.When(status='Rejected', then=2), default=3, output_field=models.IntegerField()), '-applied_on'],
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
