# Generated by Django 4.0.6 on 2022-12-07 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
    ]
