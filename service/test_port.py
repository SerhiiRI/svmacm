import socket, errno

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(("127.0.0.1", 8777))
except socket.error as e:
    if e.errno == errno.EADDRINUSE:
        s.close()
        print(1)
        exit()
s.close()
print(0)



