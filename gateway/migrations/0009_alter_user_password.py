# Generated by Django 3.2.5 on 2021-11-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0008_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=300),
        ),
    ]
