#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 5:05 PM
# @Author  : huangt
# @File    : zf_oxy.py
# @Software: PyCharm
import datetime
import sys
import time
import hashlib
import requests

from py12306.config import Config


class ZFProxyUtil:
    @staticmethod
    def getProxySign():
        orderno = Config.zf_order_no()
        secret = Config.zf_secret()

        _version = sys.version_info

        is_python3 = (_version[0] == 3)


        timestamp = str(int(time.time()))  # 计算时间戳
        string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

        if is_python3:
            string = string.encode()

        md5_string = hashlib.md5(string).hexdigest()  # 计算sign
        sign = md5_string.upper()  # 转换成大写
        auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
        headers = {"Proxy-Authorization": auth}
        return headers

    @staticmethod
    def getProxy():

        ip = "forward.xdaili.cn"
        port = "80"

        ip_port = ip + ":" + port
        proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}

        return proxy

    @staticmethod
    def proxyResponse():
        orderno = "ZF2018389801ujxzjF"
        secret = "ef49c2c2765d4115be9c474f377b6e9c"

        _version = sys.version_info

        is_python3 = (_version[0] == 3)

        ip = "forward.xdaili.cn"
        port = "80"

        ip_port = ip + ":" + port

        timestamp = str(int(time.time()))  # 计算时间戳
        string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

        if is_python3:
            string = string.encode()

        md5_string = hashlib.md5(string).hexdigest()  # 计算sign
        sign = md5_string.upper()  # 转换成大写
        # print(sign)
        auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
        headers = {"Proxy-Authorization": auth}

        # print(auth)
        proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
        r = requests.get("https://www.tianyancha.com/company/2602017365", headers=headers, proxies=proxy, verify=False,
                         allow_redirects=False)

        return r.content
        # print(r.status_code)
        # print(r.content)
        # print(r.status_code)
        # if r.status_code == 302 or r.status_code == 301:
        #     loc = r.headers['Location']
        #     url_f = "https://www.tianyancha.com" + loc
        #     print(loc)
        #     r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
        #     print(r.status_code)
        #     print(r.text)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    text = ZFProxyUtil.proxyResponse()
    print(text)
    end_time = datetime.datetime.now()
    print("耗时:%s" % (end_time - start_time))
