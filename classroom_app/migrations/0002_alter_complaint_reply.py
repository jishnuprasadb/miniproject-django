# Generated by Django 4.0.2 on 2022-04-02 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
    ]
