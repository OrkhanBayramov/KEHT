# Azərbaycan dilində intefeysi olan alət.
# NetMask avtomatik əldə edilir.
# Şəbəkədə Marşrutlaşdırıcının (routerin) İP ünvanını,
# Həmçinin Şəbəkədə olan digər qurğuların İP və MAC ünvanı qısa zamanda görüntülənir.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.kht.az
#!/usr/bin/env python

import subprocess
import netifaces
import scapy.all as scapy
import requests

def print_banner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKERS ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az\n")

def check_and_install_libraries():
    required_libraries = ["netifaces", "scapy", "requests"]
    missing_libraries = []

    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            missing_libraries.append(lib)

    if missing_libraries:
        for lib in missing_libraries:
            subprocess.call(["pip", "install", lib])
        print("Installed the required libraries: " + ", ".join(missing_libraries))
    else:
        print("All required libraries are already installed.")

def find_router_ip():
    try:
        gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
        return gateway
    except Exception:
        return None

def find_netmask(ip):
    try:
        mask = ip.split('/')
        return mask[1]
    except Exception:
        return "24"  # Set a default network mask (e.g., /24)

def scan(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        clients_list = []
        for element in answered_list:
            clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(clients_dict)
        return clients_list
    except Exception:
        return None

def print_result(result_list):
    print("IP Ünvan\tMAC Ünvan\tİstehsalçı")
    print("-------------------------------")
    for client in result_list:
        ip = client["ip"]
        mac = client["mac"]
        vendor_name = get_vendor_name(mac)
        print(f"{ip}\t{mac}\t{vendor_name}")

def get_vendor_name(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return "Not Found"
    except Exception:
        return "Error"

if __name__ == "__main__":
    check_and_install_libraries()
    
    try:
        print_banner()
        print("------- Şəbəkə analiz olunur! ------- Çıxış: CTRL + C -------")
        
        router_ip = find_router_ip()
        if router_ip:
            network_ip = router_ip + "/" + find_netmask(router_ip)
            scan_result = scan(network_ip)
            if scan_result:
                print_result(scan_result)
                print("\nRouter IP:", router_ip, "Şəbəkə Maskası:", find_netmask(router_ip))
            else:
                print("No devices found on the network.")
        else:
            print("Router not found.")
    except KeyboardInterrupt:
        print("\n[+] CTRL + C .... Proses dayandırıldı!")
