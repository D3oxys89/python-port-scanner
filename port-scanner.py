import socket
from colorama import Fore
import os
from time import sleep

os.system('cls') #Limpando a tela.

# ─────────────────────────────

def load():
    print(Fore.LIGHTGREEN_EX + """
                                          ─

                                              ─ D 

                                          ─
    """)
    sleep(1)
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + """
                                          ──
    
                                              ─ D3

                                          ──
    """)
    sleep(1)
    os.system('cls')
    print(Fore.LIGHTCYAN_EX + """
                                          ───

                                              ─ D3o
    
                                          ────
    """)
    sleep(1)
    os.system('cls')
    print(Fore.LIGHTMAGENTA_EX + """
                                          ─────────

                                              ─ D3ox

                                          ─────────
    """)
    sleep(1)
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + """
                                          ───────────

                                              ─ D3oxys 
    
                                          ───────────
    """)
    sleep(1)
    os.system('cls')
    print(Fore.LIGHTWHITE_EX + """
                                          ───────────────────
    
                                              ─ D3oxys Port 

                                          ────────────────────
    """)
    sleep(1)
    os.system('cls')
    print(Fore.RED + """
                                          ───────────────────────────────

                                              ─ D3oxys Port Scanner! ─

                                         ────────────────────────────────
    """)

load()
sleep(2)
os.system('cls')
print(Fore.LIGHTCYAN_EX + "[*]" + Fore.RESET + " Welcome to Port Scanner.\n")
host = input(Fore.LIGHTCYAN_EX + "[*]" + Fore.RESET + " Please, give me a IP (Enter a number or it may make a fatal error later.): ") #Recebendo a entrada do IP.
print(Fore.LIGHTCYAN_EX + "\n[*]" + Fore.RESET + " The IP is: " + host) 
sleep(2)
os.system('cls')

# ─────────────────────────────

print(Fore.LIGHTCYAN_EX + "[*]" + Fore.RESET + " The IP is: " + host + "\n") 
ip = socket.gethostbyname(host) 

for porta in range(1 , 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        connect = s.connect_ex((ip , porta))

        if connect == 0:
            print(Fore.LIGHTGREEN_EX + "[*]" + " A porta: " + porta + "está aberta.")
        s.close()
