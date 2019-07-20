# Generated by Django 2.1.4 on 2019-07-19 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0002_auto_20190716_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='root_comment', to='body.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='c_b_commentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='body.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='c_b_dynamic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='body.DynamicStatus'),
        ),
    ]
