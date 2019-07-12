from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django import views
from . import models
import os

# Create your views here.
def index(request):

    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)
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
        p_list=[]
        content = request.POST.get('d_content')
        picture = request.FILES.getlist('d_picture')
        for i in picture:
            p_list.append('/picture/' + str(i))
            file = open(f'picture/{i.name}', 'wb')
            for j in i.chunks():
                file.write(j)
            file.close()
        DynamicStatus.objects.create(d_content=content, d_picture=str(p_list), user_id_id=2)
        return redirect('body:index')


def Thumpsup(request, a_id):
    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)

    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    u = UserInfo.objects.get(id=4)
    dynamic = DynamicStatus.objects.get(id=a_id)
    if Thumps_up.objects.filter(u_id=1, article_id=a_id).exists():
        Thumps_up.objects.filter(u_id=1, article_id=a_id).delete()
        dynamic.d_num -= 1
        dynamic.save()
    else:
        Thumps_up.objects.create(u_id=1, article_id=a_id)
        dynamic.d_num += 1
        dynamic.save()

    return render(request, 'index.html', {'u': u,
                                          "head_info": head_info,
                                        "info": info,
                                        "heat": heat,
                                        "guest": guest})


def Love_article(request, a_id):
    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)

    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    u = UserInfo.objects.get(id=4)
    dynamic = DynamicStatus.objects.get(id=a_id)
    if love.objects.filter(u_id=1, U_Article_id=a_id).exists():
        love.objects.filter(u_id=1, U_Article_id=a_id).delete()
        dynamic.d_like -= 1
        dynamic.save()
    else:
        love.objects.create(u_id=1, U_Article_id=a_id)
        dynamic.d_like += 1
        dynamic.save()

    return render(request, 'index.html', {'u': u,
                                          "head_info": head_info,
                                        "info": info,
                                        "heat": heat,
                                        "guest": guest})



def move_text(request, a_id):
    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)

    # 首页文章信息传递
    info = DynamicStatus.objects.all().order_by('-d_time')

    # 热度信息传递
    heat = [1, 2, 3, 4]

    # 最近访客信息传递
    guest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # uid = request.session.get('u_id')
    # d_id = request.POST.get('zhuan')
    dynamic = DynamicStatus.objects.get(id=a_id)
    d_user_id = dynamic.user_id_id # 被转发的用户Id
    print('d_user_id在这儿', d_user_id)
    u_id = UserInfo.objects.get(id=1).id # 转发的用户Id
    new_content = request.POST.get('move_content')

    Move_text.objects.create(d_z_user_id=u_id, d_user=d_user_id)
    DynamicStatus.objects.create(d_content=dynamic.d_content, d_picture=dynamic.d_picture, user_id_id=u_id, new_content=new_content)

    return render(request, 'index.html', {"head_info": head_info,
                                          "info": info,
                                          "heat": heat,
                                          "guest": guest,
                                          "dynamic": dynamic,
                                          # 'd_id': d_id
                                          })




def dynamic_state(request):
    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)

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
    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)

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

def photo_album(request):
    '''

    :param request:
    :return:
        相册页面
    '''
    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)
    return render(request,"photo_album.html",{"head_info":head_info})

def personal(request):
    '''

    :param request:
    :return:
        个人档页面
    '''
    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)

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
    userid = request.session.get('userid')
    head_info = models.levelsystem.objects.select_related('userid').get(userid=userid)
    return render(request,"chat.html",{"head_info":head_info})






