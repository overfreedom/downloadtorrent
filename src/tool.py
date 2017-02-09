#!/usr/bin/python
#-*-coding:utf-8-*-


from bs4 import BeautifulSoup
import requests
"""
    打开一个链接 返回该链接的beautifsoup对象
     要求传入一个requests 和一个链接   
"""
def openURL_Post(url,**args):
    reponse = requests.post(url,**args)
    return BeautifulSoup(reponse.content,'html.parser')

def openURL_Get(url,**args):
    reponse = requests.get(url,**args)
    return BeautifulSoup(reponse.text,'html.parser')