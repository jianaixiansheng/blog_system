# Generated by Django 2.1.3 on 2019-07-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0006_auto_20190718_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_IP',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]