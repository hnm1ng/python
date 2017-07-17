#coding:utf-8
import time
from socket import *
myhost=''
myport=99
sockobj=socket(AF_INET,SOCK_STREAM)
sockobj.bind((myhost,myport))
sockobj.listen(99)
while True:
    connection,address=sockobj.accept()
    print( "connect by", address)
    data = connection.recv(1024)
    print( "data:  ",data)
    connection.send(b"success;key=abcdefghi;klmnopqrst_")
    connection.send(b"/data/swwd=111&snsd=222&snsy=333&snpm2.5=444&snco2=555&gzqd=666&ydgl=777&ydl=888&")
    connection.close()
    #print( "close")
