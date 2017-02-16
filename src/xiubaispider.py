'''
Created on 2017年2月9日

@author: Administrator
'''
import requests 
from bs4 import BeautifulSoup
from time import sleep
import tool

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        'Upgrade-Insecure-Requests': "1",
        'Cache-Control':'max-age=0',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }          
def run():
    rurl ='http://www.qiushibaike.com'    
    bs = tool.openURL_Get(rurl,headers=headers)     
    printTarget(bs)
    for i in range(5):        
        bs = getNext(bs)
        printTarget(bs)        
   

def printTarget(bs):
    targets=bs.findAll('div',{'class':'content'})
    for t in targets:
        print(t.get_text())        
    

def getNext(bs):
    result =bs.find('span',{'class':'next'}).find_parent('li').a['href']
    rurl ='http://www.qiushibaike.com'+result
    bs = tool.openURL_Get(rurl, headers=headers)
    print(rurl)
    sleep(2)
    return bs
    

if __name__ =='__main__':  
    run()