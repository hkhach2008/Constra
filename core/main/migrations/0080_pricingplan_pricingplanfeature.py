# Generated by Django 4.1.1 on 2022-09-30 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0079_pricingtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='PricingPlan title')),
                ('price', models.FloatField(verbose_name='PricingPlan price')),
                ('date', models.CharField(max_length=50, verbose_name='PricingPlan date')),
            ],
            options={
                'verbose_name': 'PricingPlan',
                'verbose_name_plural': 'PricingPlans',
            },
        ),
        migrations.CreateModel(
            name='PricingPlanFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.TextField(verbose_name='PricingPlanFeatures features')),
                ('pricingplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcateg', to='main.pricingplan')),
            ],
            options={
                'verbose_name': 'PricingPlanFeature',
                'verbose_name_plural': 'PricingPlanFeatures',
            },
        ),
    ]