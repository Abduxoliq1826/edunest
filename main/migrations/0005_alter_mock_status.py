# Generated by Django 4.1.3 on 2023-09-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_mock_date_mock_price_mock_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mock',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Disactive')], default=1),
        ),
    ]
