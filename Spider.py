from mirai import Mirai, Plain, MessageChain, Friend, Face, MessageChain,Group,Image,Member,At
from mirai.face import QQFaces
from bs4 import BeautifulSoup
from PIL import ImageFont,ImageDraw
from PIL import Image as PImage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import asyncio
import requests
import json5
import json
import numpy
import random
import os
import base64
import qrcode
import io
import string
import math
import urllib
import copy
import ctypes
import functools
import traceback
import http.client
import statistics
import csv
import hashlib
import zlib
import time
import datetime
import urllib
import mido
import GLOBAL
from Utils import *


def 没救了(*attrs,**kwargs):
    r = requests.get(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{tnow().strftime("%m-%d-%Y")}.csv',proxies=GLOBAL.proxy)
    if r.status_code==404:
        print('没有今天的')
        r = requests.get(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{(tnow()-datetime.timedelta(days=1)).strftime("%m-%d-%Y")}.csv',proxies=GLOBAL.proxy)
    if r.status_code==404:
        print('没有昨天的')
        r = requests.get(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{(tnow()-datetime.timedelta(days=2)).strftime("%m-%d-%Y")}.csv',proxies=GLOBAL.proxy)
        print(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{(tnow()-datetime.timedelta(days=1)).strftime("%m-%d-%Y")}.csv')
        #print(r.text)
    if r.status_code!=200:
        return [Plain('别看了，没救了')]
    c = csv.reader(io.StringIO(r.text))
    s = []
    d = {}
    for i in c:
        if i[0]=='FIPS':
            t=[]
            #t.append('国家或地区')
            #t.append('更具体一点')
            t.append('累计')
            t.append('死亡')
            t.append('治愈')
            t.append('患者')
            s.append('\t\t\t'.join(t))
        else:
            it = d.setdefault(i[3],[0,0,0,0])
            it[0]+=int(i[-7])
            it[1]+=int(i[-6])
            it[2]+=int(i[-5])
            it[3]+=int(i[-4])
    for k,v in sorted(d.items(),key=lambda x: x[1][0],reverse=True):
        #s.append(f'{k}\t{v[0]}\t{v[1]}\t{v[2]}\t{v[3]}')
        s.append("""{0}:\n{1:{5}<10.10}{2:{5}<10.10}{3:{5}<10.10}{4:{5}<10.10}""".format(k,str(v[0]),str(v[1]),str(v[2]),str(v[3]),chr(8214)))
        #s.append("""{0:_<30.30}{1:_<37.37}{2:_<10.10}{3:_<10.10}{4:_<10.10}{5:_<10.10}""".format(i[3],i[2],i[-5],i[-4],i[-3],i[-2]))

    return [Plain('\n\n'.join(s))]

def 爬一言(*attrs,**kwargs):
    dst = ' '.join(attrs)
    for _ in ('f','sl','nm','cao','你妈','屌','mmp','傻逼','妈逼','操'):
        if _ in dst.lower():
            tmp = requests.get('https://nmsl.shadiao.GLOBAL.app/api.php?lang=zh_cn')
            return [Plain(text=tmp.text)]

    tmp = requests.get('https://v1.hitokoto.cn')
    j = json.loads(tmp.text)
    return [Plain(text=j['hitokoto'])]

def 爬OIWiki(*attrs,**kwargs):
    lnk = 'https://oi-wiki.org/'
    if len(attrs):
        query = ' '.join(attrs)
        plnk = 'https://search.oi-wiki.org:8443/?s=' + query
        j = json.loads(requests.get(plnk).text)
        ostr = [Plain(text='找到了%d个类似的东西\n'%len(j))]
        if len(j):
            c = j[0]
            ostr.append(Plain(text='直接把%s扔给你了\n'%c['title']))
            suflnk = c['url']
            # print(c)
            # print(suflnk)
        else:
            ostr.append(Plain(text='无结果'))
            return ostr
    else:
        ostr = []
        if random.choice([True,False]):
            r = requests.get(lnk, headers=GLOBAL.OIWikiHeaders)
            r.encoding = 'utf-8'

            s = BeautifulSoup(r.text, 'html.parser')
            res = s.find('nav', attrs={'data-md-component': 'tabs'})

            hdir = random.choice(res('a')[2:-2])
            subRes = s.find('label',string=hdir.string,attrs={'class':'md-nav__link'})

            hd2 = random.choice(list(subRes.next_siblings)[1]('li',attrs={'class':'md-nav__item'}))
            suflnk = hd2.a['href']
        else:
            lnk = 'https://ctf-wiki.github.io/ctf-wiki/'
            r = requests.get(lnk, headers=GLOBAL.OIWikiHeaders)
            r.encoding = 'utf-8'

            s = BeautifulSoup(r.text, 'html.parser')
            res = s.find('nav', attrs={'data-md-component': 'tabs'})

            hdir = random.choice(res('a')[1:])
            subRes = [i for i in s('label',attrs={'class':'md-nav__link','for':re.compile('nav-[0-9]*$')}) if hdir.string.strip() in i.text][0]

            hd2 = random.choice(list(subRes.next_siblings)[1]('li',attrs={'class':'md-nav__item'}))
            suflnk = hd2.a['href']

    url=lnk+suflnk
    print(url)

    save_fn=randstr(GLOBAL.randomStrLength)+"tmpLearn"+str(kwargs['gp'].id)+'.png'
    ostr += renderHtml(url,save_fn)
    
    asyncio.ensure_future(rmTmpFile(save_fn),loop=None)
    ostr.append(Image.fromFileSystem(save_fn))
    return ostr

def 爬萌娘(*attrs,**kwargs):
    lnk = 'https://zh.moegirl.org/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2'
    if len(attrs):
        keyWord = ' '.join(attrs)
        r = requests.get('https://zh.moegirl.org/index.php?title=Special:搜索&go=前往&search='+keyWord,headers=GLOBAL.moeGirlHeaders)
        r.encoding = 'utf-8'
        s = BeautifulSoup(r.text, 'html.parser')
        res = s.find('ul', attrs={'class': 'mw-search-results'})
        if res is None:
            if len(r.history):
                lnk = r.url
            else:
                tlnk = 'https://zh.moegirl.org/' + keyWord
                if requests.get(tlnk).status_code == 404:
                    return [Plain(text=random.choice(['这不萌娘','在萌娘找不到这玩意']))]
                else:
                    lnk = tlnk
        else:
            lnk = 'https://zh.moegirl.org'+res.find('a')['href']
    save_fn=randstr(GLOBAL.randomStrLength)+"tmpMoe"+str(kwargs['mem'].id)+'.png'
    l = renderHtml(lnk,save_fn)
    asyncio.ensure_future(rmTmpFile(save_fn),loop=None)
    return l+[Image.fromFileSystem(save_fn)]

def 爬OEIS(*attrs,**kwargs):
    if attrs:
        for i in attrs[0].split(','):
            if not i.isdigit():
                return [Plain('输入格式需为半角逗号分隔的整数')]
            else:
                r = requests.get(f'http://oeis.org/search?fmt=data&q={attrs[0]}')
                s = BeautifulSoup(r.text,'html.parser')
                resp = []
                for i in s('table',attrs={'cellpadding':'0','cellspacing':'0','border':'0','width':'100%'}):
                    try:
                        #print(i)
                        t1 = Plain('oeis.org'+i.tr.td.a['href']+'\n')
                        t2 = Plain('$$$'.join(list(i.next_sibling.next_sibling.tt.strings))+'\n\n')
                        resp.append(t1)
                        resp.append(t2)
                    except:
                        pass
                return resp
    else:
        return [Plain('输入格式需为半角逗号分隔的整数')]

def 爬CF(*attrs,**kwargs):
    try:
        gp = kwargs['gp'].id
    except:
        gp = kwargs['gp']
    fn = f"CF/{gp}"
    
    CFNoticeQueue = GLOBAL.CFNoticeQueueGlobal.setdefault(gp,{})
            
    if len(attrs):
        if attrs[0] in ('reset','stop','cancel'):
            try:
                os.remove(fn)
            except Exception as e:
                print(e)
            while CFNoticeQueue:
                i = CFNoticeQueue.popitem()
                print(i,'删除中->',i[1].cancel())
            return [Plain('取消本群的CodeForces比赛提醒服务')]
        elif attrs[0] in ('R','render'):
            with open(fn,'w') as fr:
                fr.write('R')
    else:
        with open(fn,'w') as fr:
            fr.write('Y')

    if os.path.exists(fn):

        CFdata = fetchCodeForcesContests()
        CFNoticeManager(CFdata,**kwargs)
        li = []
        for k,v in CFdata.items():

            if 'countdown' not in v:
                li.append(Plain(f'有正在进行的比赛：{v["title"]}\n\n'))
            else:
                li.append(Plain(v['title']+'  '))
                li.append(Plain(','.join(v['authors'])+'  '))
                li.append(Plain(v['routine'].strftime('%Y/%b/%d %H:%M')+'  '))
                li.append(Plain(v['length']+'  '))
                li.append(Plain(v['countdown']+'\n'))  
    return li

def 爬AtCoder(*attrs,**kwargs):
    try:
        gp = kwargs['gp'].id
    except:
        gp = kwargs['gp']
    fn = f"AtCoder/{gp}"
    
    ATNoticeQueue = GLOBAL.OTNoticeQueueGlobal.setdefault(gp,{})
            
    if len(attrs):
        if attrs[0] in ('reset','stop','cancel'):
            try:
                os.remove(fn)
            except Exception as e:
                print(e)
            while ATNoticeQueue:
                i = ATNoticeQueue.popitem()
                print(i,'删除中->',i[1].cancel())
            return [Plain('取消本群的AtCoder比赛提醒服务')]
    else:
        with open(fn,'w') as fr:
            fr.write('Y')
    li = []
    if os.path.exists(fn):

        ATData = fetchAtCoderContests()
        

        if ATData['running']:
            li.append(Plain('正在运行的比赛：\n'))
            for cont in ATData['running']:
                li.append(Plain(f"{cont['title']} {cont['ranking_range']} {cont['length']} {cont['begin'].strftime('%Y/%b/%d %H:%M')}\n"))
                
        li.append(Plain('将来的比赛：\n'))
        for cont in ATData['upcoming']:
            li.append(Plain(f"{cont['title']} {cont['ranking_range']} {cont['length']} {cont['begin'].strftime('%Y/%b/%d %H:%M')}\n"))
            cont['title'] = '【AT】'+cont['title']

        OTNoticeManager(ATData['upcoming'],**kwargs)
        li.append(Plain('已自动订阅AtCoder的比赛提醒服务，取消请使用#AT reset'))
    return li

def 爬LaTeX(*attrs,**kwargs):
    base = r'\dpi{150} \bg_white \large ' + ' '.join(attrs).replace('+','&plus;')
    r = requests.get('https://latex.vimsky.com/test.image.latex.php?fmt=png&dl=0&val='+urllib.parse.quote(urllib.parse.quote(base)))
    fn = f"tmpLaTeX{randstr(3)}.png"
    with open(fn,'wb') as f:
        f.write(r.content)
    asyncio.ensure_future(rmTmpFile(fn))
    return [Image.fromFileSystem(fn)]

def 爬牛客(*attrs,**kwargs):
    try:
        gp = kwargs['gp'].id
    except:
        gp = kwargs['gp']
    fn = f"NowCoder/{gp}"
    
    NCNoticeQueue = GLOBAL.OTNoticeQueueGlobal.setdefault(gp,{})
            
    if len(attrs):
        if attrs[0] in ('reset','stop','cancel'):
            try:
                os.remove(fn)
            except Exception as e:
                print(e)
            while NCNoticeQueue:
                i = NCNoticeQueue.popitem()
                print(i,'删除中->',i[1].cancel())
            return [Plain('取消本群的牛客比赛提醒服务')]
    else:
        with open(fn,'w') as fr:
            fr.write('Y')
    li = []
    if os.path.exists(fn):

        NCData = fetchNowCoderContests()
        for i in NCData:
            li.append(Plain(i['title']+'\n'))
            li.append(Plain(f"{i['begin']}"+'\t'))
            li.append(Plain(i['length']+'\n\n'))
            i['title'] = '【牛客】' + i['title']

        OTNoticeManager(NCData,**kwargs)
        
        li.append(Plain('已自动订阅牛客的比赛提醒服务，取消请使用#NC reset'))

    return li
        
def 爬歌(*attrs,**kwargs):
    keyword = urllib.parse.quote(''.join(attrs))

    lnk = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={keyword}&pn=1&rn=30'

    ses = requests.session()

    r = ses.get(f'http://kuwo.cn/search/list?key={keyword}')

    r = ses.get(lnk, headers={
    	'referer': f'http://www.kuwo.cn/search/list?key={keyword}',
    	'csrf': f"{ses.cookies.get('kw_token')}"
    })

    j = json.loads(r.text)
    mid = j['data']['list'][0]['musicrid']

    url = f'http://antiserver.kuwo.cn/anti.s?type=convert_url&format=mp3&response=url&rid=MUSIC_{mid}'
	r = requests.get(url,headers = {
		'user-agent': 'okhttp/3.10.0'
	})
	print(r.text)
    return [Plain(r.text)]

SpiderMap = {
    '#LaTeX':爬LaTeX,
    '#看看病':没救了,
    '#什么值得学':爬OIWiki,
    '#什么值得娘':爬萌娘,
    '#什么值得听':爬歌,
    '#oeis':爬OEIS,
    '#CF':爬CF,
    '#AT':爬AtCoder,
    '#牛客':爬牛客,
    '#肛道理':爬一言,
}

SpiderShort = {
    '#xx':'#什么值得学',
    '#moe':'#什么值得娘',
    '#什么值得d':'#什么值得娘',
    '#什么值得萌':'#什么值得娘',
    '#什么值得医':'#看看病',
    '#救命':'#看看病',
    '#NC':'#牛客',
    '#yy':'#肛道理',
    '#tex':'#LaTeX',
    '#uta':'#什么值得听',
    '#listen':'#什么值得听',
}

SpiderDescript = {
    '#LaTeX':'爬自https://latex.vimsky.com，我不会写LaTeX，炸了说一下我看看',
    '#肛道理':'请求一言app，加某些参数会黑化',
    '#什么值得学':'传参即在OI-Wiki搜索条目，不传参随便从OI或者CTFWiki爬点什么\n例:#什么值得学 后缀自动机【开发笔记：用此功能需要安装https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb，以及从http://npm.taobao.org/mirrors/chromedriver选择好对应版本放进/usr/bin里面，修完依赖启动记得传参--no-sandbox，还要把字体打包扔到/usr/share/fonts/truetype】\n==一条条渲染完了才会发送，老师傅们放过学生机吧TUT==',
    '#什么值得娘':'传参即在萌百爬取搜索结果，不传参即随便从萌娘爬点什么，例:#什么值得娘 リゼ・ヘルエスタ',
    '#oeis':'根据给定的逗号隔开的数列在OEIS寻找符合条件的数列，例:#oeis 1,1,4,5,1,4',
    '#看看病':'从jhu看板爬目前各个国家疫情的数据',
    '#CF':
"""
爬取CodeForces将要开始的比赛的时间表
可用参数:
    reset（取消提醒）
    render（提醒时渲染problems）
""",
    '#AT':
"""
爬取AtCoder将要开始的比赛的时间表
可用参数:
    reset（取消提醒）
""",
    '#牛客':
"""
爬取牛客将要开始的比赛的时间表
感谢@Kevin010304提供的爬虫
可用参数:
    reset（取消提醒）
""",
    '#什么值得听':'根据给定关键词从酷我爬歌（以后会更新更多平台的咕（危'
}