# Generated by Django 4.1.1 on 2022-09-29 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0074_faqcattitle2'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqCat1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=175, verbose_name='FaqCat1 name')),
            ],
            options={
                'verbose_name': 'FaqCat1',
                'verbose_name_plural': 'FaqCats1',
            },
        ),
        migrations.CreateModel(
            name='FaqCat2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=175, verbose_name='FaqCat2 name')),
            ],
            options={
                'verbose_name': 'FaqCat2',
                'verbose_name_plural': 'FaqCats2',
            },
        ),
        migrations.AlterField(
            model_name='faqcatsubcat1',
            name='faqcat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcat1', to='main.faqcat1'),
        ),
        migrations.AlterField(
            model_name='faqcatsubcat2',
            name='faqcat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcat2', to='main.faqcat2'),
        ),
        migrations.DeleteModel(
            name='FaqCat',
        ),
    ]