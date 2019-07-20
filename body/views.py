from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.http import JsonResponse
from django import views
from body.forms import *
import os
from . import models

# Create your views here.
def index(request):
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render(request, "index.html", {"head_info": head_info,
                                          "info": info,
                                          "heat": heat,
                                          "guest": guest})



class publish1(views.View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        u_id = request.session.get('user_id')
        p_list = []
        content = request.POST.get('d_content')
        picture = request.FILES.getlist('d_picture')
        for i in picture:
            p_list.append('/picture/' + str(i))
            file = open(f'picture/{i.name}', 'wb')
            for j in i.chunks():
                file.write(j)
            file.close()
        DynamicStatus.objects.create(d_content=content, d_picture=str(p_list), user_id_id=u_id)
        return redirect('body:index')



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

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render(request, "dynamic_state.html", {"head_info": head_info,
                                                  "info": info,
                                                  "heat": heat,
                                                  "guest": guest})


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

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render(request, "music.html", {"head_info": head_info,
                                          "info": info,
                                          "heat": heat,
                                          "guest": guest})

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

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(request, "personal.html", {"head_info": head_info,
                                             "info": info,
                                             "heat": heat,
                                             "guest": guest})


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
    data['c_date']=c_date.strftime('%H:%M:%S')
    data['c_user']=c_user
    data['c_id']=c_id
    data['status'] = 'SUCCESS'
    data['u_id'] = u_id
    data['text'] = text
    data['aid'] = aId
    return JsonResponse(data)

def indexs(request, us_id):
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    hh = ''
    if us_id:
        head_info = models.levelsystem.objects.select_related('userid').get(userid=us_id)
        if u_id == us_id:
            hh = False
        else:
            exist = False
            try:
                exist = models.AttentionPerson.objects.get(a_user=u_id, a_b_user=us_id)
            except AttentionPerson.DoesNotExist:
                if exist:
                    hh = False
                else:
                    hh = True

    else:
        hh = False
    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render(request, "index.html", {"head_info": head_info,
                                          'hh': hh,
                                          "info": info,
                                          "heat": heat,
                                          "guest": guest})


def attention(request, us_id):
    u_id = request.session.get('user_id')
    us_ids = models.UserInfo.objects.get(id=us_id)
    models.AttentionPerson.objects.create(a_user=u_id, a_b_user=us_ids)
    return redirect('body:indexs',us_id,permanent=True)

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
    data['c_time'] = comm.comment_time.strftime('%H:%M:%S')
    data['reply_name'] = comm.reply_to.user_name
    data['text'] = comm.c_content
    data['c_id_1'] = c_id_1
    return JsonResponse(data)
