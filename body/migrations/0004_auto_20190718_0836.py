# Generated by Django 2.1.4 on 2019-07-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0003_auto_20190718_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_city',
            field=models.CharField(default='请修改', max_length=20, verbose_name='所在地'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_sign',
            field=models.TextField(default='空空如也', verbose_name='个性签名'),
        ),
    ]
