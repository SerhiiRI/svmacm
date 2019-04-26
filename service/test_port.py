import socket, errno

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(("127.0.0.1", 8777))
except socket.error as e:
    if e.errno == errno.EADDRINUSE:
        print("port is used by other program")
    else:
        print(e)

print("[+] Port is active")        
s.close()


