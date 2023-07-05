# Şəbəkə interfeysinin Fiziki Ünvanını dəyişmək üçün Azərbaycan dilində intefeysi olan alət.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.kht.az
# !/usr/bin/env python

import subprocess
import netifaces
import re


def printbanner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKERS ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az\n")


printbanner()


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] MAC ünvan tapılmadı.")


def search_interfaces():
    print(" [+]  Çıxış üçün 'CTRL + C'...")
    interface_list = netifaces.interfaces()
    interface_list.remove("lo")
    print(" [+]  Şəbəkə intefeysini seçin.\n")
    print(*interface_list, end="\n\n")

try:
    search_interfaces()
    interface = input(" [*] İnterfeys > ")
    new_mac = input(" [*] Yeni MAC > ")
    interface_mac = get_current_mac(interface)
    print("[ +]   ", interface, "əvvəlki ünvanı", str(interface_mac))
    change_mac(interface, new_mac)
    current_mac = get_current_mac(interface)
    if current_mac == new_mac:
        print(" [+]   Uğurla dəyişildi. Yeni MAC ", current_mac)
    else:
        print(" [-]   Uğursuz əməliyyat, root istifadəçi kimi başlat. 'sudo python3 mac_deyisen.py'")
except KeyboardInterrupt:
    print("\n [+] CTRL + C .... Proses dayandırıldı!")
