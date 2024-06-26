# Generated by Django 4.2.10 on 2024-04-07 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT_APP', '0003_alter_hotelimage_hotel_image'),
        ('USER_APP', '0003_paymentmodel_credit_card_number_paymentmodel_cvv_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGENT_APP.hotelmodel')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGENT_APP.packagemodel')),
            ],
            options={
                'db_table': 'selected_packages',
            },
        ),
    ]
