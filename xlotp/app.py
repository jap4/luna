# -*- coding: utf-8 -*-
import os
import sys
import platform
import time
from xlpy import *
import base64

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[1;32m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[36m'
GR = '\x1b[37m'



def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)
def lodprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0/90)

luna=(gt+"""
#       #     # #     #  ##### 
#       #     # ##    # #     # 
#       #     # # #   # #     # 
#       #     # #  #  # #######    
#       #     # #   # # #     # 
#       #     # #     # #     # 
 #####   #####  #     # #     #   
===============================
""")
l="entenono jo.."

def main_menu():
    clear()
    slowprints(luna)
    print(p+
        "   Tembak Xl Mode Otp" +
        "\nPilih Salah Satu:"
        "\n  [1] Menu Beli Paket" + 
        "\n  [2] Minta Otp Code" +
        "\n  [3] Menu utama"
    )
    choice = str(input(" ex:1👉 "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    lodprint(l)
    clear()
    print(luna)
    print(p+"Menu Beli Paket Xl")
    msisdn = str(input("Masukan No 62xx 👉 "))
    clear()
    print(luna)
    po = str(input(p+"Masukan Kode Otp 👉 "))
    clear()
    print(luna)
    print (p+" 1.Xtra Kuota 30GB Rp. 11.9k")
    print (p+" 2.Xtra 3GB 30day 22.9k")
    print (p+" 3.Xtra 5GB 30day 32.9k")
    print (p+" 4.Xtra 9GB 30day 52.9k")
    print (p+" 5.Hotdisk 3gb/1bln 30k")
    print (p+" 6.Hotdisk 6gb/1bln 50k")
    print (p+" 7.Nusantara 700mb 10k")
    print (p+" 8.Fb unli free/hr")
    print (p+" 9.Xtra 10GB 30day 59k")
    print (p+" 10.Waze & Chat, Rp500,1hr")
    print (p+" 11.Waze & Chat, Rp1k,3hr")
    print (p+" 12.Waze & Chat, Rp2.5k,7hr")
    print (p+" 13.Internet Unli Rp. 500/Hr")
    print (p+" 14.Sms rp.1/Hr")
    print (p+" 15.Free Tlp 3 Hr")
    print (p+" 16.X-life 2gb/bln 1thn, 60k")
    print (p+" 17.ComLite 3GB/30hr, 19.9k")
    print (p+" 18.ComLite 3.5GB/30Hr, 22.9k")
    print (p+" 19.Free Xtragram 5GB, 3hr")
    print (p+" 20.Paket Vivo V9 RP 9K/30Hr")
    print (p+" 21.XTRA YouTube 12bln, 1GB")
    print (p+" 22.WA BAYAR 500/Hari")
    print (p+" 23.Yutub Khus RP.1k/15GB/30Hr")
    print (p+" 24.Manual service id")
    pkt = str(input("Pilih Sesuai duitmu >> "))
    
    if pkt == '1':
        i = '8110671'
    elif pkt == '2':
        i = '8211010'
    elif pkt == '3':
        i = '8211011'
    elif pkt == '4':
        i = '8211012'
    elif pkt == '5':
        i = '8211108'
    elif pkt == '6':
        i = '8211109'
    elif pkt == '7':
        i = '8211170'
    elif pkt == '8':
        i = '8110529'
    elif pkt == '9':
        i = '8211183'
    elif pkt == '10':
        i = '8211369'
    elif pkt == '11':
        i = '8211370'
    elif pkt == '12':
        i = '8211371'
    elif pkt == '13':
        i = '8110528'
    elif pkt == '14':
        i = '1210026'
    elif pkt == '15':
        i = '8110490'
    elif pkt == '16':
        i = '8211034'
    elif pkt == '17':
        i = '8210882'
    elif pkt == '18':
        i = '8211121'
    elif pkt == '19':
        i = '8110624'
    elif pkt == '20':
        i = '8110619'
    elif pkt == '21':
        i = '8210949'
    elif pkt == '22':
        i = '8110531'
    elif pkt == '23':
        i = '8110649'
    elif pkt == '24':
        i = str(input("Service ID Paket👉"))
    else:
        print("Pilihan gak tercantum")
    lodprint(l)
    serviceid = i
    xl = XL(msisdn)
    r = xl.loginWithOTP(po)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
        decision = str(input(p+"Ulangi Proses [Y/N]? 👉 "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
        
def menu_2():
    lodprint(l)
    clear()
    print(luna)
    print(p+"Minta Kode Otp")
    msisdn = str(input("Masukan Nomor 62xx👉"))
    lodprint(l)
    xl = XL(msisdn)
    print(xl.reqOTP()['message'])
    decision = str(input(p+"Ulangi Proses[Y/N]? 👉 "))
    menu_actions['main']() if(decision in ['N','n']) else menu_2()

def menu_4():
    clear()
    print(".::Password Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    xl = XL(msisdn)
    print(xl.reqPassword()['message'])
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['3']()
    return

def menu_3():
     lodprint(l)
     os.system('cd ..;python x.py')


def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
