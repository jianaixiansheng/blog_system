# Generated by Django 2.1.4 on 2019-07-11 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0012_auto_20190710_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicstatus',
            name='d_move',
            field=models.IntegerField(default=0),
        ),
    ]