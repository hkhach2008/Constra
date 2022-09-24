# Generated by Django 4.1.1 on 2022-09-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_footerworkinghour_about_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='FooterService name')),
                ('servic', models.CharField(max_length=75, verbose_name='FooterService service')),
            ],
            options={
                'verbose_name': 'FooterService',
                'verbose_name_plural': 'FooterServices',
            },
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='HeaderContact',
        ),
    ]