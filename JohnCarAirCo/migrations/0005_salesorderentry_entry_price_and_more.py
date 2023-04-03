# Generated by Django 4.1.7 on 2023-03-27 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JohnCarAirCo', '0004_serviceorderpayment_salesorderpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorderentry',
            name='entry_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='serviceorderentry',
            name='entry_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='salesorderentry',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='JohnCarAirCo.salesorder'),
        ),
        migrations.AlterField(
            model_name='serviceorderentry',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='JohnCarAirCo.serviceorder'),
        ),
    ]
