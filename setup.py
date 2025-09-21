#!/usr/bin/env python3
import os

def banner():
    os.system('clear')
    os.system('figlet -f slant "ST-IP" | lolcat')
    print(" ┏━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" ┃ ST-IP Dependency Installer ┃")
    print(" ┗━━━━━━━━━━━━━━━━━━━━━━┛\n")

def install_deps():
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install python python-pip ruby figlet toilet git wget curl clang -y")
    os.system("pip install --upgrade pip")
    os.system("pip install requests colorama ipwhois python-dotenv geopy termcolor pyfiglet")
    os.system("gem install lolcat")
    print("\n✅ Dependencies installed successfully!\n")

def main():
    banner()
    choice = input("Do you want to install dependencies? (y/n): ").lower()
    if choice == "y":
        install_deps()
    else:
        print("Installation canceled.")

if __name__ == "__main__":
    main()
