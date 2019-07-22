import socket
def client(tel):
    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 要连接服务器，就必须知道服务器的端口和IP
    server_ip = '172.16.42.203'
    server_port = int(8899)
    server_connent = tcp_client.connect((server_ip,server_port))

    tcp_client.send(tel.encode('utf-8'))

