# Generated by Django 4.2.2 on 2023-12-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djid_app', '0003_alter_dashboarddata_added_alter_dashboarddata_impact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboarddata',
            name='added',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='dashboarddata',
            name='published',
            field=models.CharField(default='', max_length=255),
        ),
    ]
