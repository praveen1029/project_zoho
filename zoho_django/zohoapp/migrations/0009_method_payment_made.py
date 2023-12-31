# Generated by Django 3.2.18 on 2023-07-26 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0008_auto_20230724_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='payment_made',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('current_balance', models.IntegerField(blank=True, null=True)),
                ('gst', models.TextField(blank=True, max_length=255, null=True)),
                ('cash', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.banking')),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.method')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_table')),
            ],
        ),
    ]
