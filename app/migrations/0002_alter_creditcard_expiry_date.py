# Generated by Django 4.1.5 on 2023-03-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='expiry_date',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
