# Generated by Django 4.1.6 on 2023-02-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JohnCarAirCo', '0003_alter_productunit_unitprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='productunit',
            name='unitName',
            field=models.CharField(default='aircon', max_length=255),
        ),
    ]
