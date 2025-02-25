# Generated by Django 5.1.6 on 2025-02-25 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_session_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Идентификатор сессии Stripe')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Статус оплаты заказа')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='order.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Оплата заказа',
                'verbose_name_plural': 'Оплаты заказов',
            },
        ),
    ]
