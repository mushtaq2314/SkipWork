# Generated by Django 4.2 on 2023-08-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_order_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
