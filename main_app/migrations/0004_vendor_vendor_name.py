# Generated by Django 2.2.3 on 2019-07-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_hospital_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_name',
            field=models.CharField(default='', max_length=50, verbose_name='Vendor Name'),
            preserve_default=False,
        ),
    ]
