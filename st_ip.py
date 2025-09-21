#!/usr/bin/env python3
import subprocess
import requests
import time

# Colores ANSI
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
MAX_WIDTH = 40

# Banner y menú
def banner_panel():
    banner_text = '''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                                                                                                                                                  ┃                  ST-IP INFO                      ┃
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃            Welcome to ST-IP Tool v2.0            ┃
┃       Your personal IP & Network tracker         ┃
┃                  Coded by: satan                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Options:
 1. Enter IP info
 2. Exit
 3. Update tool
 '''
    subprocess.run(f'echo "{banner_text}" | lolcat', shell=True, check=True)
    time.sleep(0.2)  # pequeño delay para lolcat renderice todo

#  Colorea valores
def color_value(val):
    if val in [None, "", "N/A"]:
        val_str = "N/A ❌"
        return f"{RED}{val_str}{RESET}".ljust(MAX_WIDTH)
    else:
        val_str = str(val) + " ✅"
        if len(val_str) > MAX_WIDTH:
            val_str = val_str[:MAX_WIDTH-3] + "..."
        return f"{GREEN}{val_str}{RESET}".ljust(MAX_WIDTH)

# Obtiene info de la IP
def obtener_info_ip(ip):
    info = {}
    try:
        ipinfo_data = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5).json()
        ip_api_data = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        ipdata_data = requests.get(f"https://api.ipdata.co/{ip}?api-key=test", timeout=5).json()
        ipwhois_data = requests.get(f"https://ipwhois.app/json/{ip}", timeout=5).json()
        loc = ipinfo_data.get('loc', '')
        latitude, longitude = loc.split(",") if loc else ('N/A','N/A')

        info.update({
            "IP": ipinfo_data.get("ip","N/A"),
            "Hostname": ipinfo_data.get("hostname","N/A"),
            "ISP": ip_api_data.get("isp","N/A"),
            "Organization": ip_api_data.get("org","N/A"),
            "ASN": ip_api_data.get("as","N/A"),
            "City": ip_api_data.get("city","N/A"),
            "Region": ip_api_data.get("regionName","N/A"),
            "Country": ip_api_data.get("country","N/A"),
            "Postal Code": ip_api_data.get("zip","N/A"),
            "Timezone": ipinfo_data.get("timezone","N/A"),
            "Latitude": latitude,
            "Longitude": longitude,
        "Google Maps": f"https://www.google.com/maps/search/?api=1&query={loc}" if loc else "N/A",
            "Proxy": ip_api_data.get('proxy','N/A'),
            "VPN": ipdata_data.get('is_vpn','N/A'),
            "TOR": ipdata_data.get('is_tor','N/A'),
            "Threat Level": ipdata_data.get("threat_level","N/A"),
            "Language": ipwhois_data.get("language","N/A"),
            "Currency": ipwhois_data.get("currency","N/A"),
            "Country Code": ipwhois_data.get("country_code","N/A"),
            "Network": ipwhois_data.get("network","N/A"),
            "Reverse Hostname": ipwhois_data.get("reverse","N/A")
        })
    except Exception as e:
        info["Error"] = f"Failed to retrieve info: {e}"
    return info

# Panel de info original (tal como lo tenías)
def info_panel_slow(ip, info_dict):
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"┃{'ST-IP INFO'.center(50)}┃")
    print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
    for k, v in info_dict.items():
        line = f"┃ {k.ljust(18)}: {color_value(v)} ┃"
        print(line)
        time.sleep(0.08)
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

# Actualización simple
def update_tool():
    print("[*] Updating ST-IP tool...")
    time.sleep(1)
    print("[*] Tool updated!")
    input("Press Enter to return to menu...")

# Menú principal
def main():
    while True:
        banner_panel()
        opcion = input("Select an option (1-3): ").strip()
        if opcion == "1":
            ip = input("💀 Enter the public IP: ").strip()
            if not ip:
               print("No IP entered. Returning.")
               continue
            info = obtener_info_ip(ip)
            info_panel_slow(ip, info)
            input("Press Enter to return to menu...")
        elif opcion == "2":
            print("Exiting... 🔥")
            break
        elif opcion == "3":
            update_tool()
        else:
            print("Invalid option. Try again.")
            input("Press Enter to continue")
if __name__ == "__main__":
    main()
