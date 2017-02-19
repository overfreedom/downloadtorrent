import re, bs4
from bs4 import BeautifulSoup    
import requests
class Target:    
    rurl = ''
    end = False
    curl = ''
    list = {}
    first = True    
    def listUrls(self, bs):
#         for tr in bs.find('tbody',{'id':'data_list','class':'tbody'}).findAll('tr'):
#             for td in tr.findAll('td'):                                
# #                 if 'style' in td.attrs and td.attrs['style'] == 'text-align:left;':
# #                     if re.search(self.regex, td.a.text):
# #                         print(td.a.text+'url ='+td.a['href'])
# #
#                 print(td.find_next_sibling())
        self.bs = bs
        while(not self.end):                                        
            self.getPageConten(bs)
            if not self.end:
                self.curl = self.rurl + self.getNextPage(self.bs)
                print(self.curl)
                self.bs = self.getBS(self.curl, headers=self.headers)
                self.getPageConten(self.bs)
            
    def getBS(self, url, **args):
            html = requests.get(url, **args)
#     print(html.url)
            return BeautifulSoup(html.text, 'html.parser')
        
    def regexCompile(self, regex):    
        return re.compile(regex)

    def getNextPage(self, bs):
        if bs.find('a', {'class':'nextprev'}):
                if self.first :
                    l = bs.findAll('a', {'class':'nextprev'})
                    self.first = False                
                    return l.pop(l.__len__()-1)['href']
                else:
                    l = bs.findAll('a', {'class':'nextprev'})
                    if l.__len__()<2:
                        self.end = True
                        return ''
                    return l.pop(l.__len__()-1)['href']
                    
#                 return l.get(len(l)-1)


#             return bs.find('div', {'class':'pages clear'}).next_siblings[l-1]
        else:
            self.end = True

    def getPageConten(self, bs):
        for tr in bs.find('tbody', {'id':'data_list', 'class':'tbody'}).tr.next_siblings:
            print(tr)                 ##TODO 这里next——siblings不包含自身，所以要在之前再验证一下第一个tr是否我们需要的目标         
            if tr and type(tr) == bs4.element.Tag:
                
                title = ''
                url = ''                
                size = ''
                
                for td in tr.find('td').next_siblings:
    #                 print(td,type(td))
                    if td and type(td) == bs4.element.Tag:
                        if 'style' in td.attrs and td.attrs['style'] == 'text-align:left;':
                            if re.search(self.regex, td.a.text):
    #                         self.list.append({td.a.text:{'url':td.a['href']}})
                                title = td.a.text.strip()
                                url = td.a['href']
                                self.list[title] = {}
                                self.list[title]['url'] = url
                                print(title)
                                continue
                  
                        if title != '':
                                             
                            size = td.text                        
                            self.list[title]['size'] = size
                            break
