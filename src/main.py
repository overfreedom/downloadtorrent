#!/usr/bin/python
#-*-coding:utf-8-*-
from pip._vendor.requests.api import request
from tool import openURL_Post
import tkinter
if __name__ == '__main__':
#     print('in main')
#     from urllib.request import urlretrieve 
#     from urllib.request import urlopen
#     import urllib.request
#     from bs4 import BeautifulSoup
#     url=r'http://www.baidu.com'
# #     html = urlopen(url)
# #     print(html.read())
# #     bs = BeautifulSoup(html,'html.parser')
# #     print(bs)
# #     imageLocation = bs.find('link',{'rel':'shortcut icon'})['href']
# #     print(imageLocation)
# #     urlretrieve(url+imageLocation,'cc.ico')
#     proxy ={'http:':'42.159.251.84:41795'}
#     p = urllib.request.ProxyHandler(proxy)
#     opener = urllib.request.build_opener(p)
#     urllib.request.install_opener(opener)
#     html =urllib.request.urlopen(url,timeout=500)
#     bs = BeautifulSoup(html,'html.parser')
#     print(bs)

    import requests
    from bs4 import BeautifulSoup
    from tool import openURL_Post
#     rurl = 'http://share.dmhy.com'
    rurl = 'http://9moe.com/login.php'
#     rurl = 'http://baidu.com'
    #请求头
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
#         'Host': "www.zhihu.com",
#         'Origin': "http://www.zhihu.com",
        'Pragma': "no-cache",
    #         'Referer': "http://www.zhihu.com/",
        'X-Requested-With': "XMLHttpRequest"
    }
    data = {'pwuser':'','pwpwd':'','cktime':'31536000','jumpurl':'index.php','step':'2'}
    session =requests.Session()
    s = session.post(rurl,data=data, headers=headers)
    print(s.text)
    
    print(s.cookies.get_dict())
    
#     bs = openURL_Post(rurl,data=data,headers=headers)
 
#     print(bs)

    
    
    