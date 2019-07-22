from django.shortcuts import render,HttpResponse,reverse,redirect
from django.views import View
from django.db.models import Max,Avg,F,Q,Min,Count,Sum
import TCP_CLIENT as cli
import TCP_SERVER as ser
# from UDP import *
import UDP
import socket
import threading
from body.models import *
from django.http import JsonResponse
# Create your views here.




def index(request):
    tel = request.session.get('user_numbers')
    # tel = tel, jude = 0
    # a = UserInfo.objects.filter(~Q(user_numbers=tel) & ~Q(user_jude=0))
    a = request.session.get('user_id')
    print('我是当前登陆用户的ID',a)
    b = AttentionPerson.objects.select_related('a_b_user').filter(a_user=a)
    img3 = []
    for i in b:
        img2 = levelsystem.objects.get(userid=i.a_b_user.id)
        img3.append(img2)
    # 获取到当前登陆用户的对象
    user = UserInfo.objects.get(id=a)
    print('我是当前登陆用户的名字',user.user_name)
    img = levelsystem.objects.get(userid=a)
    print('我是聊天这里的',b)
    return render(request,'index1.html',{"a":b,"b":"哈哈","user":user,"img":img,"all":img3})
    # return render(request,'end_chat.html',{"a":b,"b":"哈哈"})


def info(request,IP,PORT,name):
    """把选择的人的IP和PORT存到session中"""

    request.session['IP']=IP
    request.session['PORT']=PORT
    #选择的聊天人的名字
    request.session['chat_user_name']=name
    return redirect(reverse('chat:halo'))

def halo(request):
    if request.method == "GET":
        username = request.session.get('chat_user_name')
        return render(request,'chat_1.html',{"user":username})
    else:
        meg = request.POST.get('xinxi')
        # 获取到自己的端口
        tel = request.session.get('user_numbers')
        port = UserInfo.objects.get(user_numbers=tel)
        print(port.user_name)
        print('我是发送的消息',meg)
        IP = request.session.get('IP')
        PORT = request.session.get('PORT')

        UDP.main(IP=IP,PORT=PORT,msg=meg,ME_PORT=port.user_PORT)
        print('789')
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('---------')
        # 绑定本地信息
        udp.bind((port.user_IP, port.user_PORT))
        print('==========')
        res = UDP.res_msg(udp)
        print('我接收的消息',res)
        return render(request,'chat_1.html',{"a":res})
# def cancel(request):
#     tel = request.session.get('user_id')
#     a = UserInfo.objects.get(tel=tel)
#     a.jude=0
#     a.save()
#     request.session.flush()
#     return redirect(reverse('index'))


# def po(request,udp):
#     """发送消息"""
#     if request.method == "GET":
#         return render(request,'chat_1.html')
#     else:
#         meg = request.POST.get('xinxi')
#         # 获取发送消息的人的IP和PORT
#         IP = request.session.get('IP')
#         PORT = request.session.get('PORT')
#         send_msg(udp=udp,IP=IP,PORT=PORT,msg=meg)
#         return render(request,'chat_1.html',{"a":meg})
#
#
# def rev(request,udp):
#     a = res_msg(udp)
#     return render(request,'chat_1.html',{"b":a.decode('utg-8')})
#
#
# def main(request):
#     """需要传入对方的IP和端口"""
#     # 创建套接字
#     udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # 绑定本地信息
#     udp.bind(("", 7890))
#     t1 =threading.Thread(target=rev,args=(udp,))
#     t2 =threading.Thread(target=po,args=(udp,))
#     t1.start()
#     t2.start()
#     return render(request,'chat_1.html')

# class tian(View):
#     def get(self,request):
#
#         return render(request, 'chat_1.html')
#     def post(self,request):
#
#         meg = request.POST.get('xinxi')
#         # 获取发送消息的人的IP和PORT
#         IP = request.session.get('IP')
#         PORT = request.session.get('PORT')
#         """需要传入对方的IP和端口"""
#         # 创建套接字
#         udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         socket.setdefaulttimeout(1)
#         # request.session['udp']=udp
#         # 绑定本地信息
#         # 获取我的端口
#         tel = request.session.get('tel')
#         a = Chat.objects.get(tel=tel)
#         b = a.PORT
#         udp.bind(("", b))
#
#         while True:
#             # 发送消息
#             udp.sendto(meg.encode('utf-8'), (IP, PORT))
#             print(12343654)
#             # 接收消息
#             data = udp.recvfrom(1024)
#             data = data[0].decode('gbk')
#             print(6743213)
#             return render(request, 'chat_1.html', {"b": data,"a":meg})
