# Generated by Django 3.1.1 on 2021-04-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='marks',
            field=models.IntegerField(),
        ),
    ]