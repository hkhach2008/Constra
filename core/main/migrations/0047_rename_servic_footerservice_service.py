# Generated by Django 4.1.1 on 2022-09-24 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_alter_headercontact_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footerservice',
            old_name='servic',
            new_name='service',
        ),
    ]
