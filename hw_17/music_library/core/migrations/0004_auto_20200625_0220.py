# Generated by Django 3.0.6 on 2020-06-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200625_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='duration',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
    ]
