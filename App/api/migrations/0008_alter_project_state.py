# Generated by Django 3.2.3 on 2021-05-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_release_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.IntegerField(choices=[('new', 'New'), ('inProgress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='new'),
        ),
    ]
