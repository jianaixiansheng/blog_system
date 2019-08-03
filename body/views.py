import time
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import JsonResponse
from django import views
from body.forms import *
from queue import Queue
from .models import *
from . import models
import time
import os


# Create your views here.
def index(request):
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')
    limit = 4
    paginator = Paginator(info, limit)
    page = request.GET.get('page', 1)
    result = paginator.page(page)
    is_sign = models.levelsystem.objects.filter(sign=time.strftime("%Y-%m-%d"), userid=u_id)
    if is_sign:
        hh = 2
    else:
        hh = 1

    return render(request, "index.html", {"head_info": head_info,
                                          'hh': hh,
                                          "info": result})


# def get_page(request):
#     data = {}
#     infos = DynamicStatus.objects.all().order_by('-d_time')[5:8]
#     print(infos)
#     for info in infos:
#         print(info)

#     return JsonResponse(data)


class publish1(views.View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        u_id = request.session.get('user_id')
        p_list = []
        content = request.POST.get('d_content')
        picture = request.FILES.getlist('d_picture')
        print(picture)
        for i in picture:
            p_list.append('/picture/' + str(i))
            file = open(f'picture/{i.name}', 'wb')
            for j in i.chunks():
                file.write(j)
            file.close()
        DynamicStatus.objects.create(d_content=content, d_picture=str(p_list), user_id_id=u_id)
        return redirect('body:index')


def Thumpsup(request, a_id):
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')

    u = UserInfo.objects.get(id=u_id)
    dynamic = DynamicStatus.objects.get(id=a_id)
    # all_id = Thumps_up.objects.filter(article_id=a_id)
    if Thumps_up.objects.filter(u_id=u_id, article_id=a_id).exists():
        Thumps_up.objects.filter(u_id=u_id, article_id=a_id).delete()
        dynamic.d_num -= 1
        dynamic.save()
    else:
        Thumps_up.objects.create(u_id=u_id, article_id=a_id)
        dynamic.d_num += 1
        dynamic.save()

    return render(request, 'index.html', {'u': u, "head_info": head_info, "info": info})


def thumps_up2(request):
    data = {}
    u_id = request.session.get('user_id')
    u = UserInfo.objects.get(id=u_id)
    username = u.user_name
    a_id = request.POST.get('object_id')
    dynamic = DynamicStatus.objects.get(id=a_id)
    # all_id = Thumps_up.objects.filter(article_id=a_id)
    if Thumps_up.objects.filter(u_id=u_id, article_id=a_id).exists():
        Thumps_up.objects.filter(u_id=u_id, article_id=a_id).delete()
        dynamic.d_num -= 1
        dynamic.save()
    else:
        Thumps_up.objects.create(u_id=u_id, article_id=a_id)
        dynamic.d_num += 1
        dynamic.save()
    data['status'] = 'SUCCESS'
    data['d_num'] = dynamic.d_num
    data['username'] = username
    data['a_id'] = a_id
    return JsonResponse(data)


def t_up(request):
    pass

def Love_article2(request):
    data = {}
    u_id = request.session.get('user_id')
    a_id = request.POST.get('object_id')
    dynamic = DynamicStatus.objects.get(id=a_id)
    if love.objects.filter(u_id=u_id, U_Article_id=a_id).exists():
        love.objects.filter(u_id=u_id, U_Article_id=a_id).delete()
        dynamic.d_like -= 1
        dynamic.save()
    else:
        love.objects.create(u_id=u_id, U_Article_id=a_id)
        dynamic.d_like += 1
        dynamic.save()
    data['status'] = 'SUCCESS'
    data['d_like'] = dynamic.d_like
    data['object_id'] = a_id
    return JsonResponse(data)

def move_text1(request):
    data = {}
    u_id = request.session.get('user_id')  # 转发的用户Id
    a_id = request.POST.get('hidd11')
    new_content = request.POST.get('move_content')
    b_id = DynamicStatus.objects.get(id=a_id).user_id_id
    dynamic = DynamicStatus.objects.get(id=a_id)
    Move_text.objects.create(d_user=b_id, d_z_user_id=u_id)
    DynamicStatus.objects.create(d_content=dynamic.d_content, d_picture=dynamic.d_picture, new_content=new_content, user_id_id=u_id)
    dynamic.d_move += 1
    dynamic.save()
    data['iii'] = a_id
    data['status'] = 'SUCCESS'
    return JsonResponse(data)


def dynamic_state(request):
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)

    # 好友文章信息传递
    info = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render(request, "dynamic_state.html", {"head_info": head_info,
                                                  "info": info, })


def music(request):
    '''

    :param request:
    :return:
        音乐页面
    '''
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)

    # 上传音频传递
    info = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render(request, "music.html", {"head_info": head_info,
                                          "info": info})

# def photo_album(request):
#     '''
#
#     :param request:
#     :return:
#         相册页面
#     '''
#     u_id = request.session.get('user_id')
#     head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
#     return render(request,"photo_album.html",{"head_info":head_info})


def personal(request):
    '''

    :param request:
    :return:
        个人档页面
    '''
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)

    # 上传音频传递
    info = [1]
    return render(request, "personal.html", {"head_info": head_info,
                                             "info": info})


def chat(request):
    '''

    :param request:
    :return:
        聊天页面
    '''
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    return render(request, "chat.html", {"head_info": head_info})


def Commnets(request):
    data = {}
    u_id = request.session.get('user_id')
    text = request.POST.get('comm_content')
    aId = request.POST.get('hidd')
    dyns = DynamicStatus.objects.get(id=aId)
    Comment.objects.create(c_content=text, c_b_dynamic_id=dyns.id, user_id=u_id)
    comment=Comment.objects.get(c_content=text, c_b_dynamic_id=dyns.id, user_id=u_id)
    c_id=comment.id
    c_date=comment.comment_time
    c_user=comment.user.user_name
    data['c_date']=c_date.strftime('%m-%d %H:%M:%S')
    data['c_user']=c_user
    data['c_id']=c_id
    data['status'] = 'SUCCESS'
    data['u_id'] = u_id
    data['text'] = text
    data['aid'] = aId
    return JsonResponse(data)

@csrf_exempt
def indexs(request,us_id):
    '''
    头部信息加载
    :param us_id: 访客id
    :return:
    hh 用户状态
    1. 打开个人主页  未签到
    2. 打开个人主页  已签到
    3. 打开他人主页  未关注
    4. 打开他人主页  已关注
    '''
    u_id = request.session.get('user_id')
    if not u_id:
        return HttpResponse('请登录后查看')

    head_info = models.levelsystem.objects.select_related('userid').get(userid=us_id)

    is_sign = models.levelsystem.objects.filter(sign=time.strftime("%Y-%m-%d"), userid=u_id)
    # hh类别判断

    if u_id == us_id:
        info = DynamicStatus.objects.all().order_by('-d_time')
        if is_sign:
            hh = 2
        else:
            hh = 1
        return render(request, "index.html", {"head_info": head_info,
                                              'hh': hh,
                                              "info": info})
    else:
        try:
            models.AttentionPerson.objects.get(a_user=u_id, a_b_user_id=us_id)
            hh = 4
        except AttentionPerson.DoesNotExist:
            hh = 3
    info = DynamicStatus.objects.filter(user_id_id=us_id).order_by('-d_time')
    return render(request, "index.html", {"head_info": head_info,
                                          'hh': hh,
                                          "info": info})

@csrf_exempt
def qiandao(request):
    u_id = request.POST.get('us_id')
    info = models.levelsystem.objects.get(userid=u_id)
    info.signnumber += 1
    if info.signnumber % 20 == 0:
        level = models.UserInfo.objects.get(id=u_id)
        level.user_one_level += 1
        level.save()
    info.save()
    return JsonResponse({'hh':2})

@csrf_exempt
def guanzhu(request):
    id = request.session.get('user_id')
    u_id = request.POST.get('us_id')
    u_id = models.UserInfo.objects.get(id=u_id)
    models.AttentionPerson.objects.create(a_b_user=u_id,a_user=id)
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    data = {'user_id': head_info.userid.id, 'img': head_info.userimg,
            'grade': head_info.userid.user_one_level,
            'sgrade': head_info.userid.user_member_level, 'user_name': head_info.userid.user_name,
            'user_sign': head_info.userid.user_sign, 'signnumber': head_info.signnumber}
    data['hh'] = 4
    return JsonResponse(data)

@csrf_exempt
def noguanzhu(request):
    id = request.session.get('user_id')
    u_id = request.POST.get('us_id')
    u_id = models.UserInfo.objects.get(id=u_id)
    models.AttentionPerson.objects.get(a_b_user=u_id,a_user=id).delete()
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    data = {'user_id': head_info.userid.id, 'img': head_info.userimg,
            'grade': head_info.userid.user_one_level,
            'sgrade': head_info.userid.user_member_level, 'user_name': head_info.userid.user_name,
            'user_sign': head_info.userid.user_sign, 'signnumber': head_info.signnumber}
    data['hh'] = 3
    return JsonResponse(data)

def Comments_2(request):
    data = {}
    u_id = request.session.get('user_id') # 当前写回复的用户
    new_text = request.POST.get('reply_1') # 回复的内容
    c_id = request.POST.get('reply_2') # 当前要被回复的评论的Id
    c_id_1 = request.POST.get('reply_2_1') # 所有回复的腹肌评论，也就是最初的以及评论
    u_id1 = Comment.objects.get(id=c_id).user_id # 要回复的人的Id
    Comment.objects.create(c_content=new_text, c_b_commentID_id=c_id, reply_to_id=u_id1, user_id=u_id, root_id=c_id_1)
    comm = Comment.objects.get(c_content=new_text, c_b_commentID_id=c_id, reply_to_id=u_id1, user_id=u_id, root_id=c_id_1)
    data['c_id'] = c_id
    data['user1'] = comm.user.user_name
    data['c_time'] = comm.comment_time.strftime('%m-%d %H:%M:%S')
    data['reply_name'] = comm.reply_to.user_name
    data['text'] = comm.c_content
    data['c_id_1'] = c_id_1
    return JsonResponse(data)