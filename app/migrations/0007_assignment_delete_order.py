# Generated by Django 4.2 on 2023-09-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_order_order_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderID', models.CharField(max_length=50)),
                ('order_category', models.CharField(default='None', max_length=100)),
                ('document', models.FileField(null=True, upload_to='')),
                ('payment', models.FileField(null=True, upload_to='app')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_mobile', models.CharField(max_length=20)),
                ('customer_email', models.CharField(max_length=100)),
                ('customer_school', models.CharField(max_length=100)),
                ('special_instructions', models.CharField(default='None', max_length=1000)),
                ('frontpage_instructions', models.CharField(default='None', max_length=1000)),
                ('order_status', models.CharField(default='None', max_length=100)),
                ('order_date', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
