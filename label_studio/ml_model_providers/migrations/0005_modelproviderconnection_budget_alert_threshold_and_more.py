# Generated by Django 4.2.15 on 2024-11-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_model_providers', '0004_auto_20240830_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelproviderconnection',
            name='budget_alert_threshold',
            field=models.FloatField(blank=True, default=None, help_text='Budget alert threshold for the given provider connection', null=True, verbose_name='budget_alert_threshold'),
        ),
        migrations.AddField(
            model_name='modelproviderconnection',
            name='budget_last_reset_date',
            field=models.DateTimeField(blank=True, default=None, help_text='Date and time the budget was last reset', null=True, verbose_name='budget_last_reset_date'),
        ),
        migrations.AddField(
            model_name='modelproviderconnection',
            name='budget_limit',
            field=models.FloatField(blank=True, default=None, help_text='Budget limit for the model provider connection (null if unlimited)', null=True, verbose_name='budget_limit'),
        ),
        migrations.AddField(
            model_name='modelproviderconnection',
            name='budget_reset_period',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], default=None, help_text='Budget reset period for the model provider connection (null if not reset)', max_length=20, verbose_name='budget_reset_period'),
        ),
        migrations.AddField(
            model_name='modelproviderconnection',
            name='budget_total_spent',
            field=models.FloatField(blank=True, default=None, help_text='Tracked total budget spent for the given provider connection within the current budget period', null=True, verbose_name='budget_total_spent'),
        ),
        migrations.AddField(
            model_name='modelproviderconnection',
            name='is_internal',
            field=models.BooleanField(default=False, help_text='Whether the model provider connection is internal, not visible to the user', verbose_name='is_internal'),
        ),
    ]
