from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def test_server():
    # 1. 创建一个套接字对象, 并指定使用哪种传输服务
    # family=AF_INET    -   IPv4地址
    # family=AF_INET6   -   IPv6地址
    # type=SOCK_STREAM  -   TCP套接字
    # type=SOCK_DGRAM   -   UDP套接字
    # type=SOCK_RAW     -   原始套接字
    
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. 绑定IP地址和端口号
    server.bind(('127.0.0.1', 6789))
    # 3. 开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print("服务器启动开始监听")
    while True:
        # 4. 通过循环接收客户端的连接并做出相应的处理
        # accpet方法是一个阻塞方法, 如果没有客户端连接到服务器代码不会向下执行
        # accpet方法返回一个元组其中的第一各元素是客户端对象
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        # 5. 发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6. 断开连接
        client.close()


def main():
    test_server()


if __name__ == "__main__":
    main()


