import platform
import requests
import socket
import subprocess
import time
from colorama import Fore, init
from prettytable import PrettyTable
import speedtest

init(autoreset=True)


def get_connection_type():
    system = platform.system()
    if system == "Windows":
        try:
            output = subprocess.check_output(
                "netsh wlan show interfaces",
                shell=True,
                text=True,
                errors="ignore",
            )
            if "SSID" in output:
                return "Wi-Fi"
            return "Ethernet (cable)"
        except Exception:
            return "Unable to determine"
    elif system == "Linux":
        try:
            output = subprocess.check_output(
                "nmcli device status", shell=True, text=True, errors="ignore"
            )
            if "wifi" in output and "connected" in output:
                return "Wi-Fi"
            return "Ethernet (cable)"
        except Exception:
            return "Unable to determine"
    return "Unable to determine"


def get_provider_info():
    try:
        resp = requests.get("https://ipinfo.io/json", timeout=5).json()
        return resp.get("org", "Unknown"), resp.get("ip", "Unknown")
    except Exception:
        return "Unknown", "Unknown"


def get_local_ip():
    try:
        # Improved way to get local IP (excluding 127.0.0.1)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Unknown"


def test_speed():
    try:
        st = speedtest.Speedtest(secure=True)
        st.get_best_server()
        download = st.download() / 1024 / 1024
        upload = st.upload() / 1024 / 1024
        ping = st.results.ping
        return round(download, 2), round(upload, 2), round(ping, 2)
    except Exception as e:
        return "Error", "Error", "Error"


def test_packet_loss():
    host = "8.8.8.8"
    param = "-n" if platform.system().lower() == "windows" else "-c"
    count = "10"
    try:
        output = subprocess.check_output(
            f"ping {param} {count} {host}",
            shell=True,
            text=True,
            errors="ignore",
        )
        for line in output.splitlines():
            if "%" in line:
                return line.strip()
        return "Unable to determine"
    except Exception:
        return "Error checking packet loss"


def main():
    print(Fore.CYAN + "🔍 Checking network...\n")

    conn_type = get_connection_type()
    provider, public_ip = get_provider_info()
    local_ip = get_local_ip()
    download, upload, ping = test_speed()
    packet_loss = test_packet_loss()

    table = PrettyTable()
    table.field_names = ["Parameter", "Value"]
    table.add_row(["Connection Type", conn_type])
    table.add_row(["Provider", provider])
    table.add_row(["Public IP", public_ip])
    table.add_row(["Local IP", local_ip])
    table.add_row(
        ["Download Speed", f"{download} Mbps" if download != "Error" else download]
    )
    table.add_row(
        ["Upload Speed", f"{upload} Mbps" if upload != "Error" else upload]
    )
    table.add_row(["Ping", f"{ping} ms" if ping != "Error" else ping])
    table.add_row(["Packet Loss", packet_loss])

    print(Fore.GREEN + str(table))


if __name__ == "__main__":
    while True:
        main()
        print("\nRefreshing in 10 seconds...\n")
        for i in range(10, 0, -1):
            print(f"{i}...", end=" ", flush=True)
            time.sleep(1)
        print("\n")