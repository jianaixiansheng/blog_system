# Generated by Django 2.1.4 on 2019-07-20 17:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttentionPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_content', models.TextField(null=True, verbose_name='内容')),
                ('comment_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('c_b_commentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='body.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='DynamicStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('d_content', models.TextField(verbose_name='内容')),
                ('d_picture', models.FileField(max_length=1000, null=True, upload_to='picture', validators=[django.core.validators.FileExtensionValidator('jpg', 'png', 'txt')], verbose_name='图片')),
                ('d_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('d_move', models.IntegerField(default=0)),
                ('d_like', models.IntegerField(default=0, verbose_name='喜欢数')),
                ('new_content', models.TextField(null=True, verbose_name='转发')),
            ],
        ),
        migrations.CreateModel(
            name='GuestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_b_user', models.IntegerField()),
                ('g_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='levelsystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signnumber', models.IntegerField(db_column='sign_num', verbose_name='登陆天数')),
                ('memberopendata', models.DateField(db_column='member_open_data', null=True, verbose_name='会员充值日期')),
                ('duedata', models.DateField(db_column='member_due_data', null=True, verbose_name='会员到期时间')),
                ('sign', models.BooleanField(default=False, verbose_name='当天是否签到')),
                ('userimg', models.TextField(verbose_name='用户头像编码')),
            ],
            options={
                'db_table': 'level_system',
            },
        ),
        migrations.CreateModel(
            name='love',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('U_Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.DynamicStatus')),
            ],
        ),
        migrations.CreateModel(
            name='Move_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_b_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('d_user', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thumps_up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='body.DynamicStatus')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_numbers', models.BigIntegerField(null=True, verbose_name='账号')),
                ('user_password', models.CharField(max_length=20, null=True, verbose_name='密码')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('user_sex', models.CharField(default='请修改', max_length=20, verbose_name='性别')),
                ('user_sign', models.TextField(default='空空如也', verbose_name='个性签名')),
                ('user_birth', models.DateField(auto_now_add=True, verbose_name='出生日期')),
                ('user_city', models.CharField(default='请修改', max_length=20, verbose_name='所在地')),
                ('user_one_level', models.IntegerField(default=0, verbose_name='用户等级')),
                ('user_member_level', models.IntegerField(default=0, verbose_name='会员等级')),
            ],
        ),
        migrations.AddField(
            model_name='thumps_up',
            name='u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='body.UserInfo'),
        ),
        migrations.AddField(
            model_name='move_text',
            name='d_z_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.UserInfo'),
        ),
        migrations.AddField(
            model_name='love',
            name='u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.UserInfo'),
        ),
        migrations.AddField(
            model_name='levelsystem',
            name='userid',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='body.UserInfo', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='guestlog',
            name='g_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.UserInfo'),
        ),
        migrations.AddField(
            model_name='dynamicstatus',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.UserInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='c_b_dynamic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='body.DynamicStatus'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to='body.UserInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='root_comment', to='body.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='body.UserInfo'),
        ),
        migrations.AddField(
            model_name='attentionperson',
            name='a_b_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.UserInfo'),
        ),
    ]
