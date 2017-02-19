'''
Created on 2017年2月19日

@author: overfreedom
'''
from kisssubdown.target import Target

    
if __name__ == '__main__':
    target = Target()
    target.rurl = 'http://www.kisssub.org'
    target.surl = 'http://www.kisssub.org/search.php'

    target.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0'
        }

    target.searchName = '超时空要塞_Delta'
    target.params = {'keyword':'超时空要塞_Delta'}
#          [dmhy][Macross_Delta][超时空要塞_Delta][24][1080P_简繁中][BS11高清源]    
    target.list ={}
    target.regex = target.regexCompile('.+dmhy.+超时空要塞_Delta.+1080P.+')
    
#     target.listUrls(target.getBS(target.surl,headers = target.headers,params=target.params))

    
#     bs =target.getBS(target.surl,headers = target.headers,params=target.params)
# [dmhy][Macross_Delta][超时空要塞_Delta][03][1080P_简繁中][BS11高清源]
#     print(target.list)


#     for key in target.list.keys():
#         print(key)
#         print(target.list[key])
#         print()
#     print(target.list.__len__())
    
    bs = target.getBS('http://www.kisssub.org/search.php?keyword=%E8%B6%85%E6%97%B6%E7%A9%BA%E8%A6%81%E5%A1%9E_Delta&page=5',headers=target.headers)
    target.getPageConten(bs)
    
    
    
#     target.listUrls(bs)
#     target.getNextPage(bs)