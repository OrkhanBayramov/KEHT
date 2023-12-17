import socket
import subprocess
import psutil
from prettytable import PrettyTable

# Azərbaycan dilində intefeysi olan alət.
# Şəbəkə interfeysləri ekrana verilir.
# Seçilmiş şəbəkə interfeysi ip və mac ünvanı əldə edilir.
# Seçilmiş şəbəkə interfeysinin istifadə etdiyi port nömrələri və proseslər ekrana çap edilir.
# Hazırladı Orxan Bayramov.
# Yazılım dili Python 3
# 2021-ci il https://www.kht.az
#!/usr/bin/env python

def print_banner():
    subprocess.call(["clear"])
    print("██   ██ ██   ██  █████   ██████   █████  ███    ██    AZERBAIJAN")
    print("██  ██  ██   ██ ██   ██ ██       ██   ██ ████   ██      ETHICAL ")
    print("█████   ███████ ███████ ██   ███ ███████ ██ ██  ██      HACKERS ")
    print("██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██       TEAM")
    print("██   ██ ██   ██ ██   ██  ██████  ██   ██ ██   ████  https://kht.az\n")

def check_install_psutil():
    try:
        import psutil
    except ImportError:
        print("psutil library not found. Installing...")
        try:
            subprocess.check_call(["pip", "install", "psutil"])
            print("psutil library installed successfully.")
        except Exception as e:
            print(f"Error installing psutil: {e}")
            exit()

def get_network_interfaces():
    check_install_psutil()

    interfaces = psutil.net_if_addrs()

    print_banner()

    print("Mövcud Şəbəkə İnterfeysləri:")
    table_interfaces = PrettyTable(["Nömrə", "Interfeys"])
    for i, interface in enumerate(interfaces.keys(), start=1):
        table_interfaces.add_row([i, interface])
    print(table_interfaces)

    try:
        selected_index = int(input("\nİncələmək istədiyiniz interfeysin nömrəsini daxil edin: "))
        selected_interface = list(interfaces.keys())[selected_index - 1]
    except (ValueError, IndexError):
        print("\nXəta: Düzgün bir nömrə daxil etmədiniz və ya interfeys mövcud deyil.")
        return

    print(f"\n'{selected_interface}' interfeysi üçün Ətraflı Məlumatlar:")
    addresses = interfaces[selected_interface]
    table_details = PrettyTable(["Məlumat Növü", "Qiymət"])
    for address in addresses:
        if address.family == socket.AF_INET:
            table_details.add_row(["IP v4", address.address])
        elif address.family == socket.AF_INET6:
            table_details.add_row(["IP v6", address.address])
        elif address.family == psutil.AF_LINK:
            table_details.add_row(["MAC", address.address])
    print(table_details)

    find_network_devices(selected_interface)

def find_network_devices(interface):
    try:
        # Filter TCP connections
        tcp_connections = [conn for conn in psutil.net_connections("inet") if conn.family == socket.AF_INET]

        interface_addresses = [addr.address for addr in psutil.net_if_addrs()[interface] if addr.family == socket.AF_INET]

        print(f"\n'{interface}' interfeysi ilə əlaqəli prosesləri:")
        show_process_for_port(interface_addresses, tcp_connections)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print("Proses məlumatı əldə etmək mümkün deyil.")

def show_process_for_port(interface_addresses, tcp_connections):
    processes = []
    for process in tcp_connections:
        if process.laddr.ip in interface_addresses:
            processes.append(process)

    if processes:
        table_processes = PrettyTable(["IP", "Port", "Process", "PID"])
        for process in processes:
            try:
                process_info = psutil.Process(process.pid)
                table_processes.add_row([process.laddr.ip, process.laddr.port, process_info.name(), process.pid])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                table_processes.add_row([process.laddr.ip, process.laddr.port, "N/A", process.pid])

        print(table_processes)
    else:
        print("Bu interfeys ilə əlaqəli heç bir proses tapılmadı.")

if __name__ == "__main__":
    get_network_interfaces()

