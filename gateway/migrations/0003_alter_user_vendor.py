# Generated by Django 3.2.5 on 2021-11-24 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0002_product_title idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gateway.vendor'),
        ),
    ]
