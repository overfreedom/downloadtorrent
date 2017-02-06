#encoding=utf-8
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
    rurl = ''
        
    r= requests.get('http://www.baidu.com')
    r.encoding='utf-8'
    bs =BeautifulSoup(r.text,'html.parser') 
    print(bs.find('title'))
    