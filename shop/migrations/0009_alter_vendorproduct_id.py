# Generated by Django 3.2.5 on 2021-12-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_vendorproduct_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorproduct',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
