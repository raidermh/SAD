# Generated by Django 3.2.3 on 2021-05-16 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_requirement_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='specification',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.specification'),
        ),
    ]
