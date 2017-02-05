
if __name__ == '__main__':
    print('in main')
    from urllib.request import urlretrieve 
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    html = urlopen(r'http://baidu.com')
    print(html.read())
#     bs = BeautifulSoup(html.read(),'html.parser')
#     print(bs)
#     imageLocation = bs.find('link',{'rel':'shortcut icon'})['href']
#     print(imageLocation)
    
    
    