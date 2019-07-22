import socket
import threading
def res_msg(udp):

        data = udp.recvfrom(1024)
        # print(data[0].decode('gbk'))
        return data[0].decode('gbk')


def send_msg(udp, IP, PORT,msg):
    udp.sendto(msg.encode('gbk'), (IP, PORT))


def main(IP,PORT,msg,ME_PORT):
    """需要传入对方的IP和端口"""
    #创建套接字
    udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #绑定本地信息
    udp.bind(("",7890))
    #获取对方IP和PORT

    #创建多线程，进行消息的发送和接收
    # send_msg(udp,IP,PORT,msg)
    # res_msg(udp)
    t_send = threading.Thread(target=send_msg,args=(udp,IP,PORT,msg))
    t_rsv = threading.Thread(target=res_msg,args=(udp,))
    t_send.start()
    t_rsv.start()

if __name__ == "__main__":
    main(IP='172.16.42.203',PORT=58340,ME_PORT=7890,msg='我爱你')