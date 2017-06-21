#import time
#print(int(time.time() * 1000))

import requests
from lxml import html
import json
import time
import threading


def loginjwc(sno, password):
    s = requests.Session()
    # post login jwc
    login_url = 'http://sso.jwc.whut.edu.cn/Certification//login.do'
    login_headers = {
        'Accept': 'text/html,application/xhtml+xml,'
        'application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) '
        'Gecko/20100101 Firefox/49.0',
        'Upgrade-Insecure-Requests': '1',
    }
    login_data = {
        'systemId': '',
        'xmlmsg': '',
        'userName': sno,
        'password': password,
        'type': 'xs',
    }
    s.post(login_url, headers=login_headers, data=login_data)
    return s
    pass


def course(s):
    course_url = 'http://202.114.90.180/Course/'
    course_headers = {
        'Accept': 'text/html,application/xhtml+xml,'
        'application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) '
        'Gecko/20100101 Firefox/49.0',
        'Upgrade-Insecure-Requests': '1',
    }
    s.get(course_url, headers=course_headers)
    return s
    pass


def getcourse(s):
    url = "http://202.114.90.180/Course/gxkxkAdd.do"\
        "?xnxq=2017-2018-1"\
        "&kcdm=6010016000"\
        "&jxjhh=2015"\
        "&addid=526182328EE3546FE053FD02A8C00ACC"\
        "&gsdm="\
        "&keyinfo=5D236F4CB8BD3AC64E23F34391CEF719"\
        "&_=" + str(int(time.time() * 1000))
    headers = {
        "Host": "202.114.90.180",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive"
    }
    wanshe = s.get(url, headers=headers)
    print(wanshe.content)
    return s
    pass


loginsession = loginjwc(sno='', password='')
# class of 'bjmc'
session = course(loginsession)


def wanshe(session):
    for x in range(1, 20):
        # time.sleep(1)
        getcourse(session)
        pass
    pass


my_thread1 = threading.Thread(target=wanshe, args=(session,))
my_thread2 = threading.Thread(target=wanshe, args=(session,))
my_thread3 = threading.Thread(target=wanshe, args=(session,))
my_thread4 = threading.Thread(target=wanshe, args=(session,))
my_thread5 = threading.Thread(target=wanshe, args=(session,))


my_thread1.start()
# my_thread1.join()

my_thread2.start()
# my_thread2.join()

my_thread3.start()
# my_thread3.join()

my_thread4.start()

my_thread5.start()

#Dailymgt_kbcx(s=Dailymgt(s=loginsession), bjmc='信管1501')
# Examination_ksapCxList(Examination(s=loginsession))
# Examtime
# http://202.114.90.172:8080/Examination/ksapList.do
