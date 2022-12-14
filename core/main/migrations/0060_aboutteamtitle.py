# Generated by Django 4.1.1 on 2022-09-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_alter_aboutfact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeamTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='AboutTeamTitle title')),
                ('name', models.CharField(max_length=50, verbose_name='AboutTeamTitle name')),
            ],
            options={
                'verbose_name': 'AboutTeamTitle',
                'verbose_name_plural': 'AboutTeamTitles',
            },
        ),
    ]
