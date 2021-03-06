from graia.broadcast.entities.event import BaseEvent
from graia.broadcast.entities.dispatcher import BaseDispatcher
from graia.broadcast.interfaces.dispatcher import DispatcherInterface
from graia.broadcast import Broadcast
from graia.broadcast.entities.decorater import Decorater
from graia.broadcast.builtin.decoraters import Depend, Middleware
from graia.broadcast.interfaces.decorater import DecoraterInterface
from graia.broadcast.exceptions import PropagationCancelled
from graia.application.event.messages import GroupMessage
from graia.application.message.chain import MessageChain
from graia.application.friend import Friend
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication as Mirai
from Callable import funs
from typing import Optional
from Fetcher import *
from Utils import *
from GLOBAL import irori
import os
import random
import asyncio
import time
import copy
import datetime


class Routiner7(BaseEvent):
    class Dispatcher(BaseDispatcher):
        @staticmethod
        def catch(interface: DispatcherInterface):
            pass

class Routiner0(BaseEvent):
    class Dispatcher(BaseDispatcher):
        @staticmethod
        def catch(interface: DispatcherInterface):
            pass

class Routiner17(BaseEvent):
    class Dispatcher(BaseDispatcher):
        @staticmethod
        def catch(interface: DispatcherInterface):
            pass

class RoutinerIma(BaseEvent):
    class Dispatcher(BaseDispatcher):
        @staticmethod
        def catch(interface: DispatcherInterface):
            pass

@irori.receiver(RoutinerIma)
async def CFLoopRoutiner():
    if not os.path.exists('CF/'): os.mkdir('CF/')
    if any([_ for _ in os.listdir('CF/') if _[-4:]!='.png']):
        j = fetchCodeForcesContests()
        for _ in os.listdir('CF/'):
            try:
                if _[-4:]!='.png':
                    print(f'EXECUTING{_}')
                    CFNoticeManager(j,gp=int(_))
            except:
                print('CF爬虫挂了！', traceback.format_exc())

@irori.receiver(RoutinerIma)
async def ATLoopRoutiner():
    if not os.path.exists('AtCoder/'): os.mkdir('AtCoder/')
    if any([_ for _ in os.listdir('AtCoder/') if _[-4:]!='.png']):
        j = fetchAtCoderContests()
        for _ in os.listdir('AtCoder/'):
            try:
                if _[-4:]!='.png':
                    OTNoticeManager(j['upcoming'],gp=int(_))
            except:
                print('AT爬虫挂了！', traceback.format_exc())

@irori.receiver(RoutinerIma)
async def NCLoopRoutiner():
    if not os.path.exists('NowCoder/'): os.mkdir('NowCoder/')
    if any([_ for _ in os.listdir('NowCoder/') if _[-4:]!='.png']):
        j = fetchNowCoderContests()
        for _ in os.listdir('NowCoder/'):
            try:
                if _[-4:]!='.png':
                    OTNoticeManager(j,gp=int(_))
            except:
                print('NC爬虫挂了！', traceback.format_exc())

def refreshCreditCmds():
    print('重置可用信用点命令...')
    ctr = random.randint(3, 9)
    fs = random.sample(funs.keys(), k=ctr)
    op = random.choices(GLOBAL.credit_operators, GLOBAL.credit_operators_weight, k=ctr)
    vl = random.choices(range(1,5), k=ctr)
    GLOBAL.credit_cmds = {k:v for k, *v in zip(fs, op, vl)}
    print(GLOBAL.credit_cmds)

@irori.receiver(Routiner0)
async def CreditCommandRefresher():
    refreshCreditCmds()
    if not os.path.exists('credits/sub/'): os.mkdir('credits/sub/')
    for _ in os.listdir('credits/sub/'):
        try:
            cmds = list(GLOBAL.credit_cmds.keys())
            pattern = f'今天使用{",".join(cmds)}这些命令会有惊喜哦（'
            asyncio.ensure_future(msgDistributer(msg=pattern,typ='P',player=_))
        except:
            print('信用点推送挂了！',traceback.format_exc())

refreshCreditCmds()

@irori.receiver(Routiner0)
async def JRRPclearRoutiner():
    try:
        GLOBAL.JRRP_map.clear()
        print('你昨天的人品已经被清除了——')
    except:
        traceback.print_exc()
        print('人品清除失败')

@irori.receiver(Routiner0)
async def WeatherSubscribeRoutiner():
    print('进入回环(天气预报')
    if not os.path.exists('weather/'): os.mkdir('weather/')

    for _ in os.listdir('weather/'):
        try:
            with open('weather/'+_,'r') as f:
                dt = datetime.datetime.now()
                ans = [f'今天是{dt.year}年{dt.month}月{dt.day}日，{youbi[dt.isoweekday()]}']

                try:
                    bs = BeautifulSoup(requests.get('https://wannianrili.51240.com/').text,'html.parser')
                    res = bs('div',attrs={'id':'jie_guo'})
                    ans.append('农历'+res[0].contents[0].contents[dt.day]('div',attrs={'class':"wnrl_k_you_id_wnrl_nongli"})[0].string)
                    ans.append(res[0].contents[dt.day]('span',string='节气')[0].nextSibling.string)
                except:
                    ans.append('我忘了今天农历几号了')
                    print(traceback.format_exc())

                if random.randint(0,3):
                    ans.append(random.choice(['还在盯着屏幕吗？','还不睡？等死吧','别摸了别摸了快点上床吧','白天再说.jpg','邀请你同床竞技']))

                for city in f.readlines():
                    if city.strip():
                        j = fetchWeather(city.strip())
                        ans += j[:3]
            asyncio.ensure_future(msgDistributer(msg='\n'.join(ans),typ='P',player=_))

        except:
            print('天气预报姬挂了！',traceback.format_exc())

@irori.receiver(Routiner0)
async def ChatClearer():
    print('聊天统计中...')
    for p, i in enumerate(sorted(GLOBAL.chat_log.items(), key=lambda x: len(x[1]))):
        k, v = i
        print('用户', k, f'增加信用点:{5-p}:', updateCredit(k, '+', 5-p))
    GLOBAL.chat_log = {}
    print('统计完毕，数据归零')

@irori.receiver(Routiner17)
async def SentenceSubscribeRoutiner():
    print('进入回环(每日一句')
    if not os.path.exists('sentence/'): os.mkdir('sentence/')
        # await asyncio.sleep(86400+5-(datetime.datetime.now().timestamp()+15*3600)%86400)
    for _ in os.listdir('sentence/'):
        try:
            d={}
            fetchSentences(d)
            if 'img' in d:
                asyncio.ensure_future(msgDistributer(msg=d['img'],typ='I',player=_))
            asyncio.ensure_future(msgDistributer(msg='\n'.join(d['plain']),typ='P',player=_))

        except:
            print('每日一句挂了！',traceback.format_exc())

def WaitFormula(s: str) -> float:
    u = datetime.datetime.strptime(s, '%H:%M')
    v = datetime.datetime(1900,1,1)
    wait = (u - v).total_seconds()
    delays = 1
    to_new_day = 86400 - (datetime.datetime.now().timestamp() + 8 * 3600) % 86400
    return to_new_day + wait + delays

def RoutinerLoop():
    async def R0():
        while True:
            await asyncio.sleep(WaitFormula('0:00'))
            irori.postEvent(Routiner0())
    async def R7():
        while True:
            await asyncio.sleep(WaitFormula('7:00'))
            irori.postEvent(Routiner7())
    async def R17():
        while True:
            await asyncio.sleep(WaitFormula('17:00'))
            irori.postEvent(Routiner17())
    async def RI():
        while True:
            await asyncio.sleep(86400)
            irori.postEvent(RoutinerIma())
    irori.postEvent(RoutinerIma())
    asyncio.ensure_future(R0())
    asyncio.ensure_future(R7())
    asyncio.ensure_future(R17())
    asyncio.ensure_future(RI())

# broadcast.postEvent(Routiner7())
