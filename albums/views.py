from django.shortcuts import render, HttpResponse, redirect
from .models import *
from body import models
from django import views
import cv2


# Create your views here.
class upload_album(views.View):
    def get(self, request):
        # return render(request, 'upload_album.html')
        return render(request,'upload_album.html')
    def post(self, request):
        u_id = request.session.get("user_id")
        f1 = request.FILES.get('picture')
        image_type = request.POST.get("image_type")
        # 利用模型类　将图片要存放的路径存到数据库中

        PhotoAlbum.objects.get_or_create(user_image='/picture/' + f1.name, image_type=image_type,
                                         user_fk_id=u_id)  # 模型类型

        # 在之前配好的静态文件目录static/media/Login 下 新建一个空文件
        # 然后我们循环把上传的图片写入到新建文件当中

        fname = 'picture/' + f1.name

        with open(f"{fname}", 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        # --------------------------------------------------------
        #  此处cv2模块的方法报黄属于正常现象
        cover_path = fname
        im1 = cv2.imread(cover_path)
        im2 = cv2.resize(im1, (160,160), )  # 为图片重新指定尺寸
        cv2.imwrite(cover_path, im2)
        # --------------------------------------------------------
        return redirect('albums:photo_album')


class upload_graph(views.View):
    def get(self, request, album_id):
        return render(request, 'upload_graph.html', {"album_id": album_id})

    def post(self, request, album_id):

        f1 = request.FILES.getlist('picture')

        # 利用模型类　将图片要存放的路径存到数据库中
        for i in f1:
            role, created = PhotoGraph.objects.get_or_create(user_image_url='/picture/' + i.name)  # 模型类型
            role.I_A.add(album_id)
        # 在之前配好的静态文件目录static/media/Login 下 新建一个空文件
        # 然后我们循环把上传的图片写入到新建文件当中
        for i in f1:
            fname = 'picture/' + i.name

            with open(f"{fname}", 'wb') as pic:
                for c in i.chunks():
                    pic.write(c)
            # --------------------------------------------------------
            #  此处cv2模块的方法报黄属于正常现象
            cover_path = fname
            im1 = cv2.imread(cover_path)
            im2 = cv2.resize(im1, (230, 300), )  # 为图片重新指定尺寸
            cv2.imwrite(cover_path, im2)
            # --------------------------------------------------------
        return redirect('albums:photo_graph', album_id)


def photo_album(request):
    '''
    :param request:
    :return:
        相册展示页面
    '''
    request.session["user_id"] = 1
    u_id = request.session.get("user_id")
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    album_objs = PhotoAlbum.objects.filter(user_fk_id=u_id, isDelete=0)
    return render(request, "photo_album.html", {"album_objs": album_objs,"head_info":head_info})


def photo_graph(request, album_id):
    '''
    :param request:
    :return:
        图片展示页面
    '''
    album_obj = PhotoAlbum.objects.filter(id=album_id).first()
    graph_objs = album_obj.photograph_set.all()
    print(graph_objs)
    return render(request, "photo_graph.html", {"graph_objs": graph_objs, "album_id": album_id})
