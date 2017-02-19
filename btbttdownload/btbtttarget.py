import re
from kisssubdown.target import Target
import bs4
from urllib.request import urlretrieve
class BtbttTarget(Target):
    def listUrls(self, bs):        
        for td in bs.findAll('a',{'rel':'nofollow','target':'_blank'}): 
            if re.search(self.regex,td.text):
                self.list[td.text]={}
                self.list[td.text]['url']=td['href']
    
    def downTorrent(self):
        for key in self.list.keys():
            self.curl =self.surl + self.list[key]['url']
            bs = self.getBS(self.curl)
            for dt in bs.findAll('dt'):
                if '下载地址' in dt.text :
                    for downloadURL in dt.next_siblings:
                        if downloadURL and type(downloadURL) == bs4.element.Tag:
                            print(downloadURL.a['href'])
                            urlretrieve(downloadURL.a['href'],key+'.torrent')
                            break