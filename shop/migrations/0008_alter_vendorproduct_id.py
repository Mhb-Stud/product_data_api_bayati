# Generated by Django 3.2.5 on 2021-12-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_vendor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorproduct',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
