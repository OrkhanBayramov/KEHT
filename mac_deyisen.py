# Şəbəkə interfeysinin Fiziki Ünvanını dəyişmək üçün Azərbaycan dilində intefeysi olan alət.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.kht.az
# !/usr/bin/env python

import subprocess
import re
import random
import sys


def printbanner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKERS ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az\n")


printbanner()

# Təsadüfi MAC ünvanı yarat
def təsadüfi_mac_ünvanı_yarat():
    mac = [0x00, 0x16, 0x3e] + [random.randint(0x00, 0xff) for _ in range(3)]
    return ':'.join(['%02x' % x for x in mac])

# Quraşdırılmış şəbəkə interfeyslərinin siyahısını əldə et ("lo" interfeysini götürməklə)
def mövcud_interfeyslər():
    ip_nəticəsi = subprocess.check_output(["ip", "link"]).decode("utf-8")
    interfeyslər = re.findall(r"\d+: (\w+):", ip_nəticəsi)
    return [interfeys for interfeys in interfeyslər if interfeys != "lo"]

# Interfeysin MAC ünvanını dəyişdir
def mac_ünvanını_dəyişdir(interfeys, yeni_mac):
    try:
        # Şəbəkə interfeysini söndür
        subprocess.call(["ip", "link", "set", "dev", interfeys, "down"])

        # MAC ünvanını dəyişdir
        subprocess.call(["ip", "link", "set", "dev", interfeys, "address", yeni_mac])

        # Şəbəkə interfeysini işə sal
        subprocess.call(["ip", "link", "set", "dev", interfeys, "up"])
        
        return True
    except Exception as e:
        return str(e)

def əsas():
    # Mövcud şəbəkə interfeyslərinin siyahısını göstər
    print("Mövcud şəbəkə interfeysləri:")
    interfeyslər = mövcud_interfeyslər()
    for i, interfeys in enumerate(interfeyslər, 1):
        print(f"{i}. {interfeys}")

    # Çıxış üçün Ctrl+C düyməsinə basmağınızı göstərmək üçün mesaj əlavə edin
    print("Çıxmaq üçün Ctrl+C düyməsinə basın")

    # İstifadəçiyə bir interfeys seçməsini təklif edin
    try:
        seçim = int(input("MAC ünvanını dəyişdirmək üçün interfeys nömrəsini daxil edin: ")) - 1
        if 0 <= seçim < len(interfeyslər):
            interfeys = interfeyslər[seçim]
        else:
            print("Yanlış seçim. Çıxış edilir.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nSkriptdən çıxılır")
        sys.exit(1)
    finally:
        sys.stdin = open('/dev/tty')

    # MAC ünvanı növünü yeniləmək üçün istifadəçi tərəfinə yenidən soruşun ("Təsadüfi" və ya "İstənilən" növü)
    print("MAC ünvanı növünü seçin:")
    print("1. Təsadüfi")
    print("2. Öz istənilən")
    mac_növü = input("Seçiminiz nömrəsini daxil edin (1 və ya 2): ")

    if mac_növü == "1":
        # Təsadüfi bir MAC ünvanı yarat
        yeni_mac_ünvanı = təsadüfi_mac_ünvanı_yarat()
    elif mac_növü == "2":
        # İstifadəçidən bir MAC ünvanı soruşun
        yeni_mac_ünvanı = input("Yeni MAC ünvanını daxil edin (məsələn, 00:11:22:33:44:55): ")
    else:
        print("Yanlış seçim. Çıxış edilir.")
        sys.exit(1)

    # MAC ünvanını dəyişdir
    nəticə = mac_ünvanını_dəyişdir(interfeys, yeni_mac_ünvanı)

    if nəticə is True:
        print(f"{interfeys} üçün MAC ünvanı {yeni_mac_ünvanı} olaraq dəyişdirildi")
    else:
        print(f"MAC ünvanını dəyişdirmək uğursuz oldu: {nəticə}")

if __name__ == "__main__":
    əsas()
