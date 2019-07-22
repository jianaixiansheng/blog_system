import socket
from body.models import *
def tcp_server():
    """主要功能是将用户的手机号和IP端口绑定在一起写入数据库中"""
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定本地的IP
    tcp_server.bind(('',8899))
    print('服务器启动成功')

    # 将套接字变为被动
    tcp_server.listen(128)

    print('等待客户端连接')

    # 等待客户端连接
    new_conn,info=tcp_server.accept()

    print(info[0],info[1])
    #获取客户端传来的信息
    tel = new_conn.recv(1024).decode('utf-8')
    print('tel',tel)
    # 将获取到的已经登陆的用户的IP和端口写入数据库
    try:
        if UserInfo.objects.get(user_numbers=tel):
            a = UserInfo.objects.get(user_numbers=tel)

            a.user_IP=info[0]
            a.user_PORT=info[1]
            a.save()
        else:
            UserInfo.objects.create(user_numbers=tel,user_IP=info[0],user_PORT=info[1])
    except:
        UserInfo.objects.create(user_numbers=tel, user_IP=info[0], user_PORT=info[1])


