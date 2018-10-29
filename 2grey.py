from socket import *
from PIL import Image
import os
from time import time

host = "127.0.0.1"
port = 4096
cloudHost = "127.0.0.1"     # Change this to Cloud IP
cloudPort = 4097
buf = 1024
addr = (host, port)
cloudAddr = (cloudHost, cloudPort)
imgIn = 'img.jpg'
imgOut = 'greyImg.jpg'
timeOut = 0.05

def sendFile(fName, addr):
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(fName, addr)
    f = open(fName, "rb")
    data = f.read(buf)
    while data:
        if(s.sendto(data, addr)):
            data = f.read(buf)
    f.close()
    s.close()

def handle():
    while True:
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(addr)

        data, address = s.recvfrom(buf)
        f = open(data, 'wb')

        data, address = s.recvfrom(buf)
        print "startTime: ", time()

        try:
            while(data):
                f.write(data)
                s.settimeout(timeOut)
                data, address = s.recvfrom(buf)
        except timeout:
            f.close()
            s.close()
        
        # Greyscale
        grayImg = Image.open(imgIn).convert('L')
        grayImg.save(imgOut)
        # Send denatured image to Cloud
        sendFile(imgOut, cloudAddr)
        print "endTime: ", time()

        # record request
        fileSize = os.path.getsize(imgIn)
        print address, fileSize


if __name__ == '__main__':
    handle()

