from btbtttarget import BtbttTarget

if __name__ == '__main__':
    btTarget = BtbttTarget()
    btTarget.surl ='http://www.btbtt.co/'
    btTarget.rurl ='http://www.btbtt.co/thread-index-fid-981-tid-4283546-page-1-scrollbottom-1.htm' 
    bs = btTarget.getBS(btTarget.rurl,headers=btTarget.headers)
    btTarget.regex = btTarget.regexCompile('.+dmhy.+超时空要塞_Delta.+1080P.+')
    btTarget.listUrls(bs)
    for key in btTarget.list.keys():
        print(key)
        print(btTarget.list[key])
        print()
    btTarget.downTorrent()
            