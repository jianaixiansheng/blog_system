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
    if Thumps_up.objects.filter(u_id=u_id, article_id=a_id).exists():
        return True
    else:
        return False


register.filter('thumps_up', Thumps_ups)


@register.filter
def get_like_num(a_id):
    d = DynamicStatus.objects.get(id=a_id)
    if d.d_num == 0:
        return 0
    else:
        d_num = d.d_num
        return d_num




@register.filter
def love_art(a_id):
    d = DynamicStatus.objects.get(id=a_id)
    d_like = d.d_like
    return d_like


@register.filter

def get_one_comment(a_id):
    c_all = Comment.objects.filter(c_b_dynamic_id=a_id, c_b_commentID_id=None)
    return c_all


@register.filter

def get_thump_name(aid):
    name_list = []
    u_id = Thumps_up.objects.filter(article_id=aid).values_list('u_id')
    name = UserInfo.objects.filter(id__in=u_id).values_list('user_name', flat=True)
    for i in name:
        name_list.append(str(i).replace("'", "").replace("'", ''))
    return str(name_list).replace('[', '').replace(']', '').replace(',', '')



@register.filter

def get_like_statu(a_id):
    if Thumps_up.objects.filter(article_id=a_id).exists():
        return 'active'
    else:
        return ''


@register.filter

def get_love_statu(a_id):
    if love.objects.filter(U_Article_id=a_id).exists():
        return 'active'
    else:
        return ''

@register.filter

def get_content(a_id):
    d_all = DynamicStatus.objects.filter(id=a_id)
    if d_all.values_list('new_content', flat=True)[0] != None:
        return True
    else:
        return False



