# Generated by Django 3.2.18 on 2023-08-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0011_auto_20230802_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='billable',
            field=models.CharField(blank=True, choices=[('Billed', 'Billed'), ('Not Billed', 'Not Billed')], default='Not Billed', max_length=255, null=True),
        ),
    ]
