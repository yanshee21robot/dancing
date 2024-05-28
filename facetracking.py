#!/usr/bin/python
#coding=utf-8
from socket import *
import multiprocessing as mp
import os
import time
import threading


################################
#   Version = " 1.3 "          #
#   Date  = " 2017/10/25 "     #
#   Author = " Sanson Li "     #
################################

os.putenv('SDL_FBDEV', '/dev/fb0')

#HOST = '192.168.1.106'
HOST = '127.0.0.1'
PORT = 20001
ADDR = (HOST, PORT)  
udpCliSock = socket(AF_INET, SOCK_DGRAM)

### Helper Functions ###########################

def head_led_turn_on():
    #link = str("{\"cmd\":\"connect\",\"account\":\"test123456\",\"port\":9002}")
    #udpCliSock.sendto(link, ADDR)
    
    data = str("{\"cmd\":\"set\",\"type\":\"led\",\"para\":{\"type\":\"camera\",\"mode\":\"on\",\"color\":\"red\"}}")
    udpCliSock.sendto(data ,ADDR)
    print(data)

def head_led_turn_off():
    #link = str("{\"cmd\":\"connect\",\"account\":\"test123456\",\"port\":9002}")
    #udpCliSock.sendto(link, ADDR)
    
    data = str("{\"cmd\":\"set\",\"type\":\"led\",\"para\":{\"type\":\"camera\",\"mode\":\"on\",\"color\":\"blue\"}}")
    udpCliSock.sendto(data ,ADDR)
    print(data)
    
def tts_speak(content):

    #time.sleep(1)
    link = str("{\"cmd\":\"connect\",\"account\":\"test123456\",\"port\":9002}")
    udpCliSock.sendto(link, ADDR)
    
    data = str("{\"cmd\":\"voice\",\"type\":\"tts\",\"data\":\"")
    end = str("\"}")
    
    udpCliSock.sendto(data+content+end ,ADDR)
    #print(data +content+end)
    
def headangle(angle, ADDR):
    #link = str("{\"cmd\":\"link\",\"account\":\"test123456\",\"port\":9002}")
    #udpCliSock.sendto(link, ADDR) 
    data = str("{\"cmd\":\"servo\",\"type\":\"write\",\"time\":35,\"angle\":\"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    #data = str("{\"cmd\":\"servo\",\"type\":\"write\",\"angle\":\"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    angle_hex = str(hex(angle))
    #print"angel_hex = %s" %(angle_hex)
    end = str("\"}")

    if(angle<16):
        hexdate=(data+"0"+angle_hex[-1]+end)
        udpCliSock.sendto(hexdate ,ADDR)
        #print(hexdate)
    else:
        udpCliSock.sendto(data + angle_hex[2] + angle_hex[3] + end ,ADDR)
        #print(data + angle_hex[2] + angle_hex[3] + end)
	
### Main ######################################################################
if __name__ == '__main__':
    head_led_turn_on()
    headangle(90, ADDR)