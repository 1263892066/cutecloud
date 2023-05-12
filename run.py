#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import httpx

CUTECLOUD_EMAIL = os.getenv('PORTABLEAPPK_USER')
CUTECLOUD_PASSWD = os.getenv('PORTABLEAPPK_PASSWD')

base_url = "https://www.cutecloud.net"

with httpx.Client(base_url=base_url, verify='cacert.pem') as client:
    headers = {"Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"", "Accept": "*/*", 
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", 
               "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", 
               "Origin": base_url, "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", 
               "Referer": f"{base_url}/auth/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    data = {"email": CUTECLOUD_EMAIL, "passwd": CUTECLOUD_PASSWD}
    rj1 = client.post("/auth/login",data=data,headers=headers).json()
    print(rj1)
    if rj1['ret'] == 1:
        rj2 = client.post("/user/checkin",headers=headers).json()
        print(rj2)



