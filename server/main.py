# код на python
# код сервера (в том числе web socket)
# код для версии python 3.10.3 (проверено)
import socket
print("Steel (Alive);")

# загрузка файлов
# info: для atom пути относительно репозитория
indexFile = open("site/index.html")
mainPage = str(indexFile.read())
indexFile.close()
# print(mainPage) # main page

# maybe this http header need....
# Content-Length:{len(mainPage)}
# http header
headders = f"HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n"
print(headders)

# network socket for http
httpSock = socket.socket()
httpSock.bind(('', 80)) # try 127.0.0.1 in browser
httpSock.listen()

while True:
    print(f"wait connection....")
    conn, addr = httpSock.accept() # hook http request
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    print("request:" + str(data))
    print(f"answer:{headders}{mainPage}");
    conn.sendall(f"{headders}{mainPage}".encode('utf-8'))
    conn.close() # free mem
# for i in range(1,10):
#     print("loading" + "."*i)
#     pass
