from django.shortcuts import render, HttpResponse, redirect
from .models import *
from body import models
from django import views
import cv2
import os
from .pinyin import PINYIN


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

        # 在之前配好的静态文件目录static/media/Login 下 新建一个空文件
        # 然后我们循环把上传的图片写入到新建文件当中

        fname = 'picture/' + f1.name

        with open(f"{fname}", 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        # --------------------------------------------------------
        #  此处cv2模块的方法报黄属于正常现象
        try:
            cover_path = fname
            im1 = cv2.imread(cover_path)
            im2 = cv2.resize(im1, (192, 250), )  # 为图片重新指定尺寸
            cv2.imwrite(cover_path, im2)
        except cv2.error as e:
            os.unlink(fname)
            return HttpResponse(f"{f1.name}不符合图片修正规则{e}")
        # --------------------------------------------------------

        clean_one = PhotoAlbum.objects.filter(image_type=image_type, user_fk_id=u_id).first()
        if clean_one:
            clean_one.user_image = '/picture/' + f1.name
            clean_one.save()
        else:
            PhotoAlbum.objects.get_or_create(user_image='/picture/' + f1.name, image_type=image_type,
                                             user_fk_id=u_id)  # 模型类型
        image_type = PINYIN(image_type)
        os.mkdir(f"picture/{u_id}_{image_type}")
        return redirect('albums:photo_album',0)


class upload_graph(views.View):
    def get(self, request, album_id):
        return render(request, 'upload_graph.html', {"album_id": album_id})

    def post(self, request, album_id):
        u_id = request.session.get("user_id")
        f1 = request.FILES.getlist('picture')
        obj = PhotoAlbum.objects.filter(id=album_id).first()
        image_type = PINYIN(obj.image_type)
        # 利用模型类　将图片要存放的路径存到数据库中

        # 在之前配好的静态文件目录static/media/Login 下 新建一个空文件
        # 然后我们循环把上传的图片写入到新建文件当中

        for i in f1:
            fname = f'picture/{u_id}_{image_type}/' + i.name

            with open(f"{fname}", 'wb') as pic:
                for c in i.chunks():
                    pic.write(c)
            # --------------------------------------------------------
            #  此处cv2模块的方法报黄属于正常现象
            try:
                fname = f'picture/{u_id}_{image_type}/' + i.name
                cover_path = fname
                im1 = cv2.imread(cover_path)
                im2 = cv2.resize(im1, (230, 300), )  # 为图片重新指定尺寸
                cv2.imwrite(cover_path, im2)
            except cv2.error:
                os.unlink(fname)
                return HttpResponse(f"{i.name}不符合图片修正规则")
            # --------------------------------------------------------

            role, created = PhotoGraph.objects.get_or_create(
                user_image_url=f'/picture/{u_id}_{image_type}/' + i.name)  # 模型类型
            role.I_A.add(album_id)
        return redirect('albums:photo_graph', album_id,0)

def photo_album(request,is_delete):
    '''
    :param request:
    :return:
        相册展示页面
    '''
    request.session["user_id"] = 1
    u_id = request.session.get("user_id")
    head_info = models.levelsystem.objects.select_related('userid').get(userid=u_id)
    if is_delete == 0:
        album_objs = PhotoAlbum.objects.filter(user_fk_id=u_id, isDelete=0)
    else:
        album_objs = PhotoAlbum.objects.filter(user_fk_id=u_id, isDelete=1)
    return render(request, "photo_album.html", {"album_objs": album_objs,"head_info":head_info,"is_delete":is_delete})


def photo_graph(request, album_id,is_delete):
    '''
    :param request:
    :return:
        图片展示页面
    '''
    print("*"*100)
    print(album_id,is_delete)
    album_obj = PhotoAlbum.objects.filter(id=album_id).first()
    if is_delete == 0:
        graph_objs = album_obj.photograph_set.filter(isDelete=0)
    else:
        graph_objs = album_obj.photograph_set.filter(isDelete=1)
    return render(request, "photo_graph.html", {"graph_objs": graph_objs, "album_id": album_id,"is_delete":is_delete})

# 对图片进行逻辑删除
def delete_graph(request,album_id,graph_id):
    obj = PhotoGraph.objects.filter(id=graph_id).first()
    obj.isDelete = 1
    obj.save()
    return redirect('albums:photo_graph',album_id,0)

# 对相册进行逻辑删除
def delete_album(request,album_id):
    obj = PhotoAlbum.objects.filter(id=album_id).first()
    obj.isDelete = 1
    obj.save()
    return redirect("albums:photo_album",0)

