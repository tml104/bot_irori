py_mirai_version = 4 # 在这里改版本号哦！3或者4


app = None
CFRenderFlag=set()
ddlQueuerGlobal = {}
CFNoticeQueueGlobal={}
OTNoticeQueueGlobal={}
QuickCalls = {}
proxy = {}
DEKnowledge = {}

cfgs={}

randomStrLength = 4
webPngLimit = int(1e6)
CaLimit = 1e13
CbLimit = 1e5
revTag = chr(8238)
pingCtr = 0
sudo_su = {}

AVGHost = ''
AVGPort = 0

AtCoderHeaders = {
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"zh-CN,zh;q=0.9",
	"cache-control":"no-cache",
	"dnt":"1",
	"pragma":"no-cache",
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

moeGirlHeaders={
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"accept-language":"zh-CN,zh;q=0.9",
	"dnt":"1",
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

OIWikiHeaders ={
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"accept-language": "zh-CN,zh;q=0.9",
	"cache-control": "max-age=0",
	"dnt": "1",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


恶臭字典 = {
	114514: "114514",
	58596: "114*514",
	49654: "11*4514",
	45804: "11451*4",
	23256: "114*51*4",
	22616: "11*4*514",
	19844: "11*451*4",
	16030: "1145*14",
	14515: "1+14514",
	14514: "1*14514",
	14513: "-1+14514",
	11455: "11451+4",
	11447: "11451-4",
	9028: "(1+1)*4514",
	8976: "11*4*51*4",
	7980: "114*5*14",
	7710: "(1+14)*514",
	7197: "1+14*514",
	7196: "1*14*514",
	7195: "-1+14*514",
	6930: "11*45*14",
	6682: "(1-14)*-514",
	6270: "114*(51+4)",
	5818: "114*51+4",
	5810: "114*51-4",
	5808: "(1+1451)*4",
	5805: "1+1451*4",
	5804: "1*1451*4",
	5803: "-1+1451*4",
	5800: "(1-1451)*-4",
	5725: "1145*(1+4)",
	5698: "11*(4+514)",
	5610: "-11*(4-514)",
	5358: "114*(51-4)",
	5005: "11*(451+4)",
	4965: "11*451+4",
	4957: "11*451-4",
	4917: "11*(451-4)",
	4584: "(1145+1)*4",
	4580: "1145*1*4",
	4576: "(1145-1)*4",
	4525: "11+4514",
	4516: "1+1+4514",
	4515: "1+1*4514",
	4514: "1-1+4514",
	4513: "-1*1+4514",
	4512: "-1-1+4514",
	4503: "-11+4514",
	4112: "(1+1)*4*514",
	3608: "(1+1)*451*4",
	3598: "(11-4)*514",
	3435: "-1145*(1-4)",
	3080: "11*4*5*14",
	3060: "(11+4)*51*4",
	2857: "1+14*51*4",
	2856: "1*14*51*4",
	2855: "-1+14*51*4",
	2850: "114*5*(1+4)",
	2736: "114*(5+1)*4",
	2652: "(1-14)*51*-4",
	2570: "1*(1+4)*514",
	2475: "11*45*(1+4)",
	2420: "11*4*(51+4)",
	2280: "114*5*1*4",
	2248: "11*4*51+4",
	2240: "11*4*51-4",
	2166: "114*(5+14)",
	2068: "11*4*(51-4)",
	2067: "11+4*514",
	2058: "1+1+4*514",
	2057: "1/1+4*514",
	2056: "1/1*4*514",
	2055: "-1/1+4*514",
	2054: "-1-1+4*514",
	2045: "-11+4*514",
	2044: "(1+145)*14",
	2031: "1+145*14",
	2030: "1*145*14",
	2029: "-1+145*14",
	2024: "11*(45+1)*4",
	2016: "-(1-145)*14",
	1980: "11*45*1*4",
	1936: "11*(45-1)*4",
	1848: "(11+451)*4",
	1824: "114*(5-1)*4",
	1815: "11+451*4",
	1808: "1*(1+451)*4",
	1806: "1+1+451*4",
	1805: "1+1*451*4",
	1804: "1-1+451*4",
	1803: "1*-1+451*4",
	1802: "-1-1+451*4",
	1800: "1*-(1-451)*4",
	1793: "-11+451*4",
	1760: "-(11-451)*4",
	1710: "114*-5*(1-4)",
	1666: "(114+5)*14",
	1632: "(1+1)*4*51*4",
	1542: "1*-(1-4)*514",
	1526: "(114-5)*14",
	1485: "11*-45*(1-4)",
	1456: "1+1451+4",
	1455: "1*1451+4",
	1454: "-1+1451+4",
	1448: "1+1451-4",
	1447: "1*1451-4",
	1446: "-1+1451-4",
	1428: "(11-4)*51*4",
	1386: "11*(4+5)*14",
	1260: "(1+1)*45*14",
	1159: "1145+14",
	1150: "1145+1+4",
	1149: "1145+1*4",
	1148: "1145-1+4",
	1142: "1145+1-4",
	1141: "1145-1*4",
	1140: "(1145-1)-4",
	1131: "1145-14",
	1100: "11*4*5*(1+4)",
	1056: "11*4*(5+1)*4",
	1050: "(11+4)*5*14",
	1036: "(1+1)*(4+514)",
	1026: "114*-(5-14)",
	1020: "1*(1+4)*51*4",
	981: "1+14*5*14",
	980: "1*14*5*14",
	979: "-1+14*5*14",
	910: "-(1-14)*5*14",
	906: "(1+1)*451+4",
	898: "(1+1)*451-4",
	894: "(1+1)*(451-4)",
	880: "11*4*5*1*4",
	836: "11*4*(5+14)",
	827: "11+4*51*4",
	825: "(11+4)*(51+4)",
	818: "1+1+4*51*4",
	817: "1*1+4*51*4",
	816: "1*1*4*51*4",
	815: "-1+1*4*51*4",
	814: "-1-1+4*51*4",
	805: "-11+4*51*4",
	784: "(11+45)*14",
	771: "1+14*(51+4)",
	770: "1*14*(51+4)",
	769: "(11+4)*51+4",
	761: "(1+14)*51-4",
	730: "(1+145)*(1+4)",
	726: "1+145*(1+4)",
	725: "1*145*(1+4)",
	724: "-1-145*-(1+4)",
	720: "(1-145)*-(1+4)",
	719: "1+14*51+4",
	718: "1*14*51+4",
	717: "-1-14*-51+4",
	715: "(1-14)*-(51+4)",
	711: "1+14*51-4",
	710: "1*14*51-4",
	709: "-1+14*51-4",
	705: "(1+14)*(51-4)",
	704: "11*4*(5-1)*4",
	688: "114*(5+1)+4",
	680: "114*(5+1)-4",
	667: "-(1-14)*51+4",
	660: "(114+51)*4",
	659: "1+14*(51-4)",
	658: "1*14*(51-4)",
	657: "-1+14*(51-4)",
	649: "11*(45+14)",
	644: "1*(1+45)*14",
	641: "11+45*14",
	632: "1+1+45*14",
	631: "1*1+45*14",
	630: "1*1*45*14",
	629: "1*-1+45*14",
	628: "114+514",
	619: "-11+45*14",
	616: "1*-(1-45)*14",
	612: "-1*(1-4)*51*4",
	611: "(1-14)*-(51-4)",
	609: "11*(4+51)+4",
	601: "11*(4+51)-4",
	595: "(114+5)*(1+4)",
	584: "114*5+14",
	581: "1+145*1*4",
	580: "1*145/1*4",
	579: "-1+145*1*4",
	576: "1*(145-1)*4",
	575: "114*5+1+4",
	574: "114*5/1+4",
	573: "114*5-1+4",
	567: "114*5+1-4",
	566: "114*5*1-4",
	565: "114*5-1-4",
	561: "11/4*51*4",
	560: "(1+1)*4*5*14",
	558: "11*4+514",
	556: "114*5-14",
	545: "(114-5)*(1+4)",
	529: "1+14+514",
	528: "1*14+514",
	527: "-1+14+514",
	522: "(1+1)*4+514",
	521: "11-4+514",
	520: "1+1+4+514",
	519: "1+1*4+514",
	518: "1-1+4+514",
	517: "-1+1*4+514",
	516: "-1-1+4+514",
	514: "(1-1)/4+514",
	513: "-11*(4-51)-4",
	512: "1+1-4+514",
	511: "1*1-4+514",
	510: "1-1-4+514",
	509: "11*45+14",
	508: "-1-1-4+514",
	507: "-11+4+514",
	506: "-(1+1)*4+514",
	502: "11*(45+1)-4",
	501: "1-14+514",
	500: "11*45+1+4",
	499: "11*45*1+4",
	498: "11*45-1+4",
	495: "11*(4+5)*(1+4)",
	492: "11*45+1-4",
	491: "11*45-1*4",
	490: "11*45-1-4",
	488: "11*(45-1)+4",
	481: "11*45-14",
	480: "11*(45-1)-4",
	476: "(114+5)/1*4",
	470: "-11*4+514",
	466: "11+451+4",
	460: "114*(5-1)+4",
	458: "11+451-4",
	457: "1+1+451+4",
	456: "1*1+451+4",
	455: "1-1+451+4",
	454: "-1+1*451+4",
	453: "-1-1+451+4",
	452: "114*(5-1)-4",
	450: "(1+1)*45*(1+4)",
	449: "1+1+451-4",
	448: "1+1*451-4",
	447: "1/1*451-4",
	446: "1*-1+451-4",
	445: "-1-1+451-4",
	444: "-11+451+4",
	440: "(1+1)*4*(51+4)",
	438: "(1+145)*-(1-4)",
	436: "-11+451-4",
	435: "-1*145*(1-4)",
	434: "-1-145*(1-4)",
	432: "(1-145)*(1-4)",
	412: "(1+1)*4*51+4",
	404: "(1+1)*4*51-4",
	400: "-114+514",
	396: "11*4*-(5-14)",
	385: "(11-4)*(51+4)",
	376: "(1+1)*4*(51-4)",
	375: "(1+14)*5*(1+4)",
	368: "(1+1)*(45+1)*4",
	363: "(1+1451)/4",
	361: "(11-4)*51+4",
	360: "(1+1)*45*1*4",
	357: "(114+5)*-(1-4)",
	353: "(11-4)*51-4",
	352: "(1+1)*(45-1)*4",
	351: "1+14*-5*-(1+4)",
	350: "1*(1+4)*5*14",
	349: "-1+14*5*(1+4)",
	341: "11*(45-14)",
	337: "1-14*-(5+1)*4",
	336: "1*14*(5+1)*4",
	335: "-1+14*(5+1)*4",
	329: "(11-4)*(51-4)",
	327: "-(114-5)*(1-4)",
	325: "-(1-14)*5*(1+4)",
	318: "114+51*4",
	312: "(1-14)*-(5+1)*4",
	300: "(11+4)*5/1*4",
	297: "-11*(4+5)*(1-4)",
	291: "11+4*5*14",
	286: "(1145-1)/4",
	285: "(11+4)*(5+14)",
	282: "1+1+4*5*14",
	281: "1+14*5/1*4",
	280: "1-1+4*5*14",
	279: "1*-1+4*5*14",
	278: "-1-1+4*5*14",
	275: "1*(1+4)*(51+4)",
	270: "(1+1)*45*-(1-4)",
	269: "-11+4*5*14",
	268: "11*4*(5+1)+4",
	267: "1+14*(5+14)",
	266: "1*14*(5+14)",
	265: "-1+14*(5+14)",
	260: "1*(14+51)*4",
	259: "1*(1+4)*51+4",
	257: "(1+1)/4*514",
	252: "(114-51)*4",
	251: "1*-(1+4)*-51-4",
	248: "11*4+51*4",
	247: "-(1-14)*(5+14)",
	240: "(11+4)*(5-1)*4",
	236: "11+45*(1+4)",
	235: "1*(1+4)*(51-4)",
	234: "11*4*5+14",
	231: "11+4*(51+4)",
	230: "1*(1+45)*(1+4)",
	229: "1145/(1+4)",
	227: "1+1+45*(1+4)",
	226: "1*1+45*(1+4)",
	225: "11*4*5+1+4",
	224: "11*4*5/1+4",
	223: "11*4*5-1+4",
	222: "1+1+4*(51+4)",
	221: "1/1+4*(51+4)",
	220: "1*1*(4+51)*4",
	219: "1+14+51*4",
	218: "1*14+51*4",
	217: "11*4*5+1-4",
	216: "11*4*5-1*4",
	215: "11*4*5-1-4",
	214: "-11+45*(1+4)",
	212: "(1+1)*4+51*4",
	211: "11-4+51*4",
	210: "1+1+4+51*4",
	209: "1+1*4*51+4",
	208: "1*1*4+51*4",
	207: "-1+1*4*51+4",
	206: "11*4*5-14",
	204: "(1-1)/4+51*4",
	202: "1+1-4+51*4",
	201: "1/1-4+51*4",
	200: "1/1*4*51-4",
	199: "1*-1+4*51-4",
	198: "-1-1+4*51-4",
	197: "-11+4+51*4",
	196: "-(1+1)*4+51*4",
	195: "(1-14)*5*(1-4)",
	192: "(1+1)*4*(5+1)*4",
	191: "1-14+51*4",
	190: "1*-14+51*4",
	189: "-11-4+51*4",
	188: "1-1-(4-51)*4",
	187: "1/-1+4*(51-4)",
	186: "1+1+(45+1)*4",
	185: "1-1*-(45+1)*4",
	184: "114+5*14",
	183: "-1+1*(45+1)*4",
	182: "1+1+45/1*4",
	181: "1+1*45*1*4",
	180: "1*1*45*1*4",
	179: "-1/1+45*1*4",
	178: "-1-1+45*1*4",
	177: "1+1*(45-1)*4",
	176: "1*1*(45-1)*4",
	175: "-1+1*(45-1)*4",
	174: "-1-1+(45-1)*4",
	172: "11*4*(5-1)-4",
	171: "114*(5+1)/4",
	170: "(11-45)*-(1+4)",
	169: "114+51+4",
	168: "(11+45)*-(1-4)",
	165: "11*-45/(1-4)",
	161: "114+51-4",
	160: "1+145+14",
	159: "1*145+14",
	158: "-1+145+14",
	157: "1*(1-4)*-51+4",
	154: "11*(4-5)*-14",
	152: "(1+1)*4*(5+14)",
	151: "1+145+1+4",
	150: "1+145*1+4",
	149: "1*145*1+4",
	148: "1*145-1+4",
	147: "-1+145-1+4",
	146: "11+45*-(1-4)",
	143: "1+145+1-4",
	142: "1+145*1-4",
	141: "1+145-1-4",
	140: "1*145-1-4",
	139: "-1+145-1-4",
	138: "-1*(1+45)*(1-4)",
	137: "1+1-45*(1-4)",
	136: "1*1-45*(1-4)",
	135: "-1/1*45*(1-4)",
	134: "114+5/1*4",
	133: "114+5+14",
	132: "1+145-14",
	131: "1*145-14",
	130: "-1+145-14",
	129: "114+5*-(1-4)",
	128: "1+1+(4+5)*14",
	127: "1-14*(5-14)",
	126: "1*(14-5)*14",
	125: "-1-14*(5-14)",
	124: "114+5+1+4",
	123: "114-5+14",
	122: "114+5-1+4",
	121: "11*(45-1)/4",
	120: "-(1+1)*4*5*(1-4)",
	118: "(1+1)*(45+14)",
	117: "(1-14)*(5-14)",
	116: "114+5+1-4",
	115: "114+5*1-4",
	114: "11*4+5*14",
	113: "114-5/1+4",
	112: "114-5-1+4",
	111: "11+4*5*(1+4)",
	110: "-(11-451)/4",
	107: "11-4*-(5+1)*4",
	106: "114-5+1-4",
	105: "114+5-14",
	104: "114-5-1-4",
	103: "11*(4+5)+1*4",
	102: "11*(4+5)-1+4",
	101: "1+1*4*5*(1+4)",
	100: "1*(1+4)*5*1*4",
	99: "11*4+51+4",
	98: "1+1+4*(5+1)*4",
	97: "1+1*4*(5+1)*4",
	96: "11*(4+5)+1-4",
	95: "114-5-14",
	94: "114-5/1*4",
	93: "(1+1)*45-1+4",
	92: "(1+1)*(45-1)+4",
	91: "11*4+51-4",
	90: "-114+51*4",
	89: "(1+14)*5+14",
	88: "1*14*(5+1)+4",
	87: "11+4*(5+14)",
	86: "(1+1)*45*1-4",
	85: "1+14+5*14",
	84: "1*14+5*14",
	83: "-1+14+5*14",
	82: "1+1+4*5/1*4",
	81: "1/1+4*5*1*4",
	80: "1-1+4*5*1*4",
	79: "1*-1+4*5/1*4",
	78: "(1+1)*4+5*14",
	77: "11-4+5*14",
	76: "1+1+4+5*14",
	75: "1+14*5*1+4",
	74: "1/1*4+5*14",
	73: "1*14*5-1+4",
	72: "-1-1+4+5*14",
	71: "(1+14)*5-1*4",
	70: "11+45+14",
	69: "1*14+51+4",
	68: "1+1-4+5*14",
	67: "1-1*4+5*14",
	66: "1*14*5-1*4",
	65: "1*14*5-1-4",
	64: "11*4+5*1*4",
	63: "11*4+5+14",
	62: "1+14+51-4",
	61: "1+1+45+14",
	60: "11+45*1+4",
	59: "114-51-4",
	58: "-1+1*45+14",
	57: "1+14*5-14",
	56: "1*14*5-14",
	55: "-1+14*5-14",
	54: "11-4+51-4",
	53: "11+45+1-4",
	52: "11+45/1-4",
	51: "11+45-1-4",
	50: "1+1*45/1+4",
	49: "1*1*45/1+4",
	48: "-11+45+14",
	47: "1/-1+45-1+4",
	46: "11*4+5+1-4",
	45: "11+4*5+14",
	44: "114-5*14",
	43: "1+1*45+1-4",
	42: "11+45-14",
	41: "1/1*45*1-4",
	40: "-11+4*51/4",
	39: "-11+45+1+4",
	38: "-11+45*1+4",
	37: "-11+45-1+4",
	36: "11+4*5+1+4",
	35: "11*4+5-14",
	34: "1-14+51-4",
	33: "1+1+45-14",
	32: "1*1+45-14",
	31: "1/1*45-14",
	30: "1*-1+45-14",
	29: "-11+45-1-4",
	28: "11+4*5+1-4",
	27: "11+4*5/1-4",
	26: "11-4+5+14",
	25: "11*4-5-14",
	24: "1+14-5+14",
	23: "1*14-5+14",
	22: "1*14+5-1+4",
	21: "-1-1+4+5+14",
	20: "-11+45-14",
	19: "1+1+4*5+1-4",
	18: "1+1+4*5*1-4",
	17: "11+4*5-14",
	16: "11-4-5+14",
	15: "1+14-5+1+4",
	14: "11+4-5/1+4",
	13: "1*14-5/1+4",
	12: "-11+4+5+14",
	11: "11*-4+51+4",
	10: "-11/4+51/4",
	9: "11-4+5+1-4",
	8: "11-4+5/1-4",
	7: "11-4+5-1-4",
	6: "1-14+5+14",
	5: "11-4*5+14",
	4: "-11-4+5+14",
	3: "11*-4+51-4",
	2: "-11+4-5+14",
	1: "11/(45-1)*4",
	0: "(1-1)*4514",
	"d": "11-4-5+1-4"
	}

QQFaces = {
    "unknown": 0xff,
    "jingya": 0,
    "piezui": 1,
    "se": 2,
    "fadai": 3,
    "deyi": 4,
    "liulei": 5,
    "haixiu": 6,
    "bizui": 7,
    "shui": 8,
    "daku": 9,
    "ganga": 10,
    "fanu": 11,
    "tiaopi": 12,
    "ciya": 13,
    "weixiao": 14,
    "nanguo": 15,
    "ku": 16,
    "zhuakuang": 18,
    "tu": 19,
    "touxiao": 20,
    "keai": 21,
    "baiyan": 22,
    "aoman": 23,
    "ji_e": 24,
    "kun": 25,
    "jingkong": 26,
    "liuhan": 27,
    "hanxiao": 28,
    "dabing": 29,
    "fendou": 30,
    "zhouma": 31,
    "yiwen": 32,
    "yun": 34,
    "zhemo": 35,
    "shuai": 36,
    "kulou": 37,
    "qiaoda": 38,
    "zaijian": 39,
    "fadou": 41,
    "aiqing": 42,
    "tiaotiao": 43,
    "zhutou": 46,
    "yongbao": 49,
    "dan_gao": 53,
    "shandian": 54,
    "zhadan": 55,
    "dao": 56,
    "zuqiu": 57,
    "bianbian": 59,
    "kafei": 60,
    "fan": 61,
    "meigui": 63,
    "diaoxie": 64,
    "aixin": 66,
    "xinsui": 67,
    "liwu": 69,
    "taiyang": 74,
    "yueliang": 75,
    "qiang": 76,
    "ruo": 77,
    "woshou": 78,
    "shengli": 79,
    "feiwen": 85,
    "naohuo": 86,
    "xigua": 89,
    "lenghan": 96,
    "cahan": 97,
    "koubi": 98,
    "guzhang": 99,
    "qiudale": 100,
    "huaixiao": 101,
    "zuohengheng": 102,
    "youhengheng": 103,
    "haqian": 104,
    "bishi": 105,
    "weiqu": 106,
    "kuaikule": 107,
    "yinxian": 108,
    "qinqin": 109,
    "xia": 110,
    "kelian": 111,
    "caidao": 112,
    "pijiu": 113,
    "lanqiu": 114,
    "pingpang": 115,
    "shiai": 116,
    "piaochong": 117,
    "baoquan": 118,
    "gouyin": 119,
    "quantou": 120,
    "chajin": 121,
    "aini": 122,
    "bu": 123,
    "hao": 124,
    "zhuanquan": 125,
    "ketou": 126,
    "huitou": 127,
    "tiaosheng": 128,
    "huishou": 129,
    "jidong": 130,
    "jiewu": 131,
    "xianwen": 132,
    "zuotaiji": 133,
    "youtaiji": 134,
    "shuangxi": 136,
    "bianpao": 137,
    "denglong": 138,
    "facai": 139,
    "K_ge": 140,
    "gouwu": 141,
    "youjian": 142,
    "shuai_qi": 143,
    "hecai": 144,
    "qidao": 145,
    "baojin": 146,
    "bangbangtang": 147,
    "he_nai": 148,
    "xiamian": 149,
    "xiangjiao": 150,
    "feiji": 151,
    "kaiche": 152,
    "gaotiezuochetou": 153,
    "chexiang": 154,
    "gaotieyouchetou": 155,
    "duoyun": 156,
    "xiayu": 157,
    "chaopiao": 158,
    "xiongmao": 159,
    "dengpao": 160,
    "fengche": 161,
    "naozhong": 162,
    "dasan": 163,
    "caiqiu": 164,
    "zuanjie": 165,
    "shafa": 166,
    "zhijin": 167,
    "yao": 168,
    "shouqiang": 169,
    "qingwa": 170,
    "cha": 171,
    "zhayan": 172,
    "leibeng": 173,
    "wunai": 174,
    "maimeng": 175,
    "xiaojiujie": 176,
    "penxue": 177,
    "xieyanxiao": 178,
    "dog": 179,
    "jinxi": 180,
    "saorao": 181,
    "xiaoku": 182,
    "wozuimei": 183,
    "hexie": 184,
    "yangtuo": 185,
    "banli": 186,
    "youling": 187,
    "dan": 188,
    "mofang": 189,
    "juhua": 190,
    "feizao": 191,
    "hongbao": 192,
    "daxiao": 193,
    "bukaixin": 194,
    "zhenjing": 195,
    "ganga": 196,
    "lenmo": 197,
    "ye": 198,
    "haobang": 199,
    "baituo": 200,
    "dianzan": 201,
    "wuliao": 202,
    "tuolian": 203,
    "chi": 204,
    "songhua": 205,
    "haipa": 206,
    "huachi": 207,
    "xiaoyang": 208,
    "unknown2": 209,#暂时不知道
    "biaolei": 210,
    "wobukan": 211,
    "tuosai": 212,
    "unknown3": 213,#暂时不知道
    #214-247表情在电脑版qq9.2.3无法显示
    "bobo": 214,
    "hulian": 215,
    "paitou": 216,
    "cheyiche": 217,
    "tianyitian": 218,
    "cengyiceng": 219,
    "zhaozhatian": 220,
    "dingguagua": 221,
    "baobao": 222,
    "baoji": 223,
    "kaiqiang": 224,
    "liaoyiliao": 225,
    "paizhuo": 226,
    "paishou": 227,
    "gongxi": 228,
    "ganbei": 229,
    "chaofeng": 230,
    "hen": 231,
    "foxi": 232,
    "jingdai": 234,
    "chandou": 235,
    "jiaotou": 236,
    "toukan": 237,
    "shanlian": 238,
    "yuanliang": 239,
    "penlian": 240,
    "shengrikuaile": 241,
    "touzhuangji": 242,
    "shuaitou": 243,
    "renggou": 244,
    "jiayoubisheng": 245,
    "jiayoubaobao": 246,
    "kouzhaohuti": 247,
    #248-255未定义
    "jinya": 256,
    "piezei": 257,
    "se": 258,
    "fadai": 259,
    "deyi": 260,
    "liulei": 261,
    "haixiu": 262,
    "bizui": 263,
    "shui": 264,
    "daku": 265,
    "ganga": 266,
    "falu": 267,
    "tiaopi": 268,
    "ziya": 269,
    "weixiao": 270,
    "nanguo": 271,
    "ku": 272,
    "unknown4": 273,#暂时不知道,qq安卓版本8.2.8.4440不显示
    "zhuakuang": 274,
    "tu": 275,
    "touxiao": 276,
    "keai": 277,
    "baiyan": 278,
    "aoman": 279,
    "jie": 280,
    "kun": 281,
    "jingkong": 282,
    "liuhan": 283,
    "hanxiao": 284,
    "dabing": 285,
    "fendou": 286,
    "zhouma": 287,
    "yiwen": 288,
    "xu": 289,
    "yun": 290,
    "zhemo": 291,
    "shuai": 292,
    "kulou": 293,
    "qiaoda": 294,
    "zaijian": 295,
    "unknown5": 296,#安卓版本无显示
    "dadou": 297,
    "aiqing": 298,
    "tiaotiao": 299,
    "unknown6": 300,#暂时不知道
    "unknown7": 301,#暂时不知道
    "zhutou": 302,
    "mao": 303,
    "unknown8": 304,#暂时不知道
    "baobao": 305,
    "meiyuanfuhao": 306,
    "dengpao": 307,#安卓版本不显示
    "gaijiaobei": 308,#安卓版本不显示
    "dangao": 309,
    "shandian": 310,
    "zhadan": 311,
    "shiai": 321,
    "aixin": 322,
    "xinsui": 323,
    "zhuozi": 324,#安卓qq不显示
    "liwu": 325,
}

恶臭键值 = sorted(list(这 for 这 in 恶臭字典.keys() if 这!='d'))

subscribes = ('S','sub','subscribe','订阅','推送','push')
unsubscribes = ('unsubscribe','cancel','td','TD','reset','stop','黙れ', '闭嘴', 'damare', 'E', 'yamero', '停')

lengthLim = 500
enable_this = {0}
compressFontSize = 18

class SessionConfigures():
	restrict_cmd = set()
	allow_cmd = set()
	compress_threshold = 500
	enable_this = True
	font_size = 18
	quick_calls = {}
	super_users = set()
	print_exception = False
	def __init__(self,player):
		self.compress_threshold = lengthLim
		self.font_size = compressFontSize
		if -player in enable_this:self.enable_this=False
		elif player in enable_this:self.enable_this=True
		elif 0 in enable_this:self.enable_this=True
		else:self.enable_this=False

	def infos(self):
		return f"""
restrict_cmd:{self.restrict_cmd}
allow_cmd:{self.allow_cmd}
compress_threshold:{self.compress_threshold}
enable_this:{self.enable_this}
font_size:{self.font_size}
quick_calls:{list(self.quick_calls.items())}
super_users:{self.super_users}
print_exception:{self.print_exception}
"""