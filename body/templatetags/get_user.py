from django import template
from body.models import *
from datetime import datetime
from django import template
from django.utils.timezone import now as now_func
register = template.Library()


def get_user(u_id):
    u = UserInfo.objects.get(id=u_id)
    return u.user_name


register.filter("get_user", get_user)




def get_member(u_id):
    u = UserInfo.objects.get(id=u_id)
    return u.user_member_level


register.filter("get_member", get_member)


def get_one_level(u_id):
    u = UserInfo.objects.get(id=u_id)
    return u.user_one_level


register.filter("get_one_level", get_one_level)


def get_picture(d_id):
    d = DynamicStatus.objects.get(id=d_id)
    picture = eval(str(d.d_picture))
    return picture

register.filter('get_picture', get_picture)


@register.filter
def time_since(value):
    if not isinstance(value, datetime):
        return value
    now = datetime.now()
    timestamp = (now - value).total_seconds()
    if timestamp < 60:
        return '刚刚'

    elif timestamp >= 60 and timestamp < 60 * 60:
        minutes = int(timestamp / 60)
        return '%s分钟前' % minutes
    elif timestamp >= 60 * 60 and timestamp < 60 * 60 * 24:
        hours = int(timestamp / 60 / 60)
        return '%s小时前' % hours
    elif timestamp >= 60 * 60 * 24 and timestamp < 60 * 60 * 24 * 30:
        days = int(timestamp / 60 / 60 / 24)
        return '%s天前' % days
    else:
        return value.strftime('%Y/%m/%d %H:%M')




def Thumps_ups(u_id, a_id):
    dynamic = DynamicStatus.objects.get(id=a_id)
    if Thumps_up.objects.filter(u_id=u_id, article_id=a_id).exists():
        Thumps_up.objects.filter(u_id=u_id, article_id=a_id).delete()
        dynamic.d_num -= 1
        dynamic.save()
        return True
    else:
        Thumps_up.objects.create(u_id=2, article_id=a_id)
        dynamic.d_num += 1
        dynamic.save()
        return False


register.filter('thumps_up', Thumps_ups)




