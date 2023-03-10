# Generated by Django 4.1.6 on 2023-02-08 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=255)),
                ('customerContact', models.CharField(max_length=12)),
                ('customerEmail', models.CharField(max_length=255)),
                ('customerAddress', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitPrice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unitQuantity', models.IntegerField()),
                ('unitType', models.CharField(choices=[('Split Type', 'Split Type'), ('Window Air Conditioner', 'Window Air Conditioner'), ('N/A', 'N/A')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceChoice', models.CharField(choices=[('Cars', 'Cars'), ('House', 'House'), ('Office', 'Office'), ('N/A', 'N/A')], max_length=50, null=True)),
                ('estimatedCost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppName', models.CharField(max_length=255)),
                ('suppPhone', models.CharField(max_length=12)),
                ('suppEmail', models.CharField(max_length=255)),
                ('suppAddress', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicianDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techName', models.CharField(max_length=255)),
                ('techPhone', models.CharField(max_length=12)),
                ('techEmail', models.CharField(max_length=255)),
                ('techSched', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='serviceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOrdered', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.customerdetails')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.servicetype')),
            ],
        ),
        migrations.CreateModel(
            name='salesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOrdered', models.DateField(auto_now_add=True)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.customerdetails')),
                ('unitOrdered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.productunit')),
            ],
        ),
    ]
