# Azərbaycan dilində intefeysi olan alət.
# NetMask avtomatik əldə edilir.
# Şəbəkədə Marşrutlaşdırıcının (routerin) İP ünvanını,
# Həmçinin Şəbəkədə olan digər qurğuların İP və MAC ünvanı qısa zamanda görüntülənir.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.kht.az
# !/usr/bin/env python

import subprocess
import netifaces
import scapy.all as scapy
import requests

def printbanner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKERS ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az\n")

def find_router_ip():  # Şəbəkə routerinin ip ünvanının təyin edilməsi.
    gw = netifaces.gateways()
    return gw["default"][netifaces.AF_INET][0]

def find_netmask():  # Şəbəkəyə çıxış interfeysinin və şəbəkə maskasının təyini.
    gw_device = netifaces.gateways()["default"]
    adapter = gw_device[netifaces.AF_INET][1]
    gw_netmask = netifaces.ifaddresses(adapter)
    netmask = gw_netmask[netifaces.AF_INET][0]["netmask"]
    from netaddr import IPAddress
    return IPAddress(netmask).netmask_bits()

def scan(ip):  # Şəbəkəyə qoşulmuş bütün qurğuların ip və mac ünvanlarının tapılması.
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(result_list):
    print("İP ünvan\t  MAC ünvan\t\t  İstehsalçı\n------------------------------------------------------")
    for client in result_list:
        vendor_mac = client["mac"]
        url = "https://api.macvendors.com/"
        response = requests.get(url + vendor_mac)
        vendor_name = response.content.decode()
        print(client["ip"] + "\t" + client["mac"] + "\t" + vendor_name)

try:
    while True:
        printbanner()
        print("-------Şəbəkə analiz olunur!----- Çıxış CTRL + C ------")
        ip = find_router_ip() + ("/") + str(find_netmask())
        scan_result = scan(ip)
        print_result(scan_result)
        print("\nRouter IP:", find_router_ip(), "Şəbəkə Maskası:", find_netmask())
        break
except KeyboardInterrupt:
    print("\n [+] CTRL + C .... Proses dayandırıldı!")

