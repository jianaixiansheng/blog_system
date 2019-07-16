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



class publish(views.View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        u_id = request.session.get('user_id')
        p_list=[]
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


def Thumpsup(request, a_id):
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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

    return render(request, 'index.html', {'u': u,
                                          "head_info": head_info,
                                        "info": info,
                                        "heat": heat,
                                        "guest": guest,
                                        # 'all_id': all_id
                                          })


def t_up(request):
    pass



def Love_article(request, a_id):
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)

    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    u = UserInfo.objects.get(id=u_id)
    dynamic = DynamicStatus.objects.get(id=a_id)
    if love.objects.filter(u_id=u_id, U_Article_id=a_id).exists():
        love.objects.filter(u_id=u_id, U_Article_id=a_id).delete()
        dynamic.d_like -= 1
        dynamic.save()
    else:
        love.objects.create(u_id=u_id, U_Article_id=a_id)
        dynamic.d_like += 1
        dynamic.save()

    return render(request, 'index.html', {'u': u,
                                          "head_info": head_info,
                                        "info": info,
                                        "heat": heat,
                                        "guest": guest})



def exit(request):
    pass





def move_text(request, a_id):
    u_id = request.session.get('user_id')  # 转发的用户Id
    # 首页文章信息传递
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)

    info = DynamicStatus.objects.all().order_by('-d_time')
    heat = [1, 2, 3, 4]
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_content = request.POST.get('move_content')
    b_id = DynamicStatus.objects.get(id=a_id).user_id_id
    dynamic = DynamicStatus.objects.get(id=a_id)
    Move_text.objects.create(d_user=b_id, d_z_user_id=u_id)
    DynamicStatus.objects.create(d_content=dynamic.d_content, d_picture=dynamic.d_picture, new_content=new_content,
                                 user_id_id=u_id)
    dynamic.d_move += 1
    dynamic.save()

    Move_text.objects.create(d_z_user_id=u_id, d_user=b_id)
    DynamicStatus.objects.create(d_content=dynamic.d_content, d_picture=dynamic.d_picture, user_id_id=u_id, new_content=new_content)

    return render(request, 'index.html', {"head_info": head_info,
                                          "info": info,
                                          "heat": heat,
                                          "guest": guest,
                                          "dynamic": dynamic,
                                          # 'd_id': d_id
                                          })




def dynamic_state(request):
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)

    # 好友文章信息传递
    info = [1,2,3,4,5,6,7,8,9,10]

    # 热度信息传递
    heat = [1,2,3,4]

    # 最近访客信息传递
    guest= [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

    return render(request,"dynamic_state.html",{"head_info":head_info,
                                        "info":info,
                                        "heat":heat,
                                        "guest":guest})

def music(request):
    '''

    :param request:
    :return:
        音乐页面
    '''
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)

    # 上传音频传递
    info = [1,2,3,4,5,6,7,8,9,10]

    # 热度信息传递
    heat = [1,2,3,4]

    # 最近访客信息传递
    guest= [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

    return render(request,"music.html",{"head_info":head_info,
                                        "info":info,
                                        "heat":heat,
                                        "guest":guest})

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
    heat = [1,2,3,4]

    # 最近访客信息传递
    guest= [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
    return render(request,"personal.html",{"head_info":head_info,
                                        "info":info,
                                        "heat":heat,
                                        "guest":guest})

def chat(request):
    '''

    :param request:
    :return:
        聊天页面
    '''
    u_id = request.session.get('user_id')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    return render(request,"chat.html",{"head_info":head_info})




def Commnets(request):
    data ={}
    u_id = request.session.get('user_id')
    text = request.POST.get('comm_content')
    aId = request.POST.get('hidd')
    dyns = DynamicStatus.objects.get(id=aId)
    u = dyns.user_id_id  # 被评论的用户Id
    Comment.objects.create(c_content=text, c_b_user_id=u, c_user=u_id, c_b_dynamic_id=aId)
    data['status'] = 'SUCCESS'
    data['u_id'] = u_id
    data['text'] = text
    data['aid'] = aId
    return JsonResponse(data)

