# Generated by Django 4.1.3 on 2023-09-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_mock_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mock',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
