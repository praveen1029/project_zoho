# Generated by Django 3.2.18 on 2023-08-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0010_bankdetails_commentmodel_payroll'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='additem',
            name='status_stock',
            field=models.TextField(default='active'),
        ),
    ]