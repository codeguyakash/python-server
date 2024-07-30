# Generated by Django 5.0.6 on 2024-07-28 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statecity', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_in', models.CharField(choices=[('Solar for Home', 'Solar for Home'), ('Solar for Office or Society', 'Solar for Office or Society'), ('Solar for Industry or Organization or Trust', 'Solar for Industry or Organization or Trust')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('contract_number', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('distributor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolarMaintanceInquries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_in', models.CharField(choices=[('Solar for Home', 'Solar for Home'), ('Solar for Office or Society', 'Solar for Office or Society'), ('Solar for Industry or Organization or Trust', 'Solar for Industry or Organization or Trust')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('contract_number', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('pin_code', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintance_inquiries', to='statecity.city')),
                ('distributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintance_inquiries', to='statecity.statesubsidy')),
            ],
        ),
        migrations.CreateModel(
            name='SolarStatus',
            fields=[
                ('solar_inquiry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='status', serialize=False, to='contact.solarinquiry')),
                ('order_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('incomplete', 'Incomplete')], default='pending', max_length=50)),
                ('site_survey_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('incomplete', 'Incomplete')], default='pending', max_length=50)),
                ('installation_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('incomplete', 'Incomplete')], default='pending', max_length=50)),
                ('grid_connectivity_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('incomplete', 'Incomplete')], default='pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SolarMaintainceStatus',
            fields=[
                ('solar_inquiry', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='contact.solarmaintanceinquries')),
                ('Technician_status', models.CharField(choices=[('Assigned', 'Assigned'), ('Not Assigned', 'Not Assigned')], default='pending', max_length=50)),
                ('service_status', models.CharField(choices=[('Complete', 'Complete'), ('Not complete', 'Not complete')], default='pending', max_length=50)),
                ('request_status', models.CharField(choices=[('Closed', 'Closed'), ('Open', 'Open')], default='pending', max_length=50)),
            ],
        ),
    ]
