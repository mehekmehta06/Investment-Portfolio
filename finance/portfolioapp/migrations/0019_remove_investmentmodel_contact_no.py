# Generated by Django 4.2.4 on 2024-01-27 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0018_investmentmodel_contact_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investmentmodel',
            name='contact_no',
        ),
    ]
