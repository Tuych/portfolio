# Generated by Django 5.0.1 on 2024-10-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rezume_alter_projects_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezume',
            name='link_for_name',
            field=models.URLField(blank=True, null=True),
        ),
    ]
