# Generated by Django 3.2.3 on 2021-05-16 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210516_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.requirement'),
        ),
    ]