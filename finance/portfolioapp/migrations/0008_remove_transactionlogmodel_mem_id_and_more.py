# Generated by Django 4.2.4 on 2024-01-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0007_rename_strat_time_membershipmodel_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionlogmodel',
            name='mem_id',
        ),
        migrations.AlterField(
            model_name='membershipmodel',
            name='start_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transactionlogmodel',
            name='trans_id',
            field=models.IntegerField(),
        ),
    ]
