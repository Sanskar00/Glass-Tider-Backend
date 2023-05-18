import requests
from bs4 import BeautifulSoup

def theHindu():
    theHinduArray=[]
    hinduUrl="https://www.thehindu.com/business/industry"
    hinduR=requests.get(hinduUrl)
    hinduHtmlContent=hinduR.content
    theHindusoup=BeautifulSoup(hinduHtmlContent,'html.parser')
    hindutitlediv=theHindusoup.findAll('div',{'class':'right-content'})
    for h3 in hindutitlediv:
        title=h3.text.strip()
        url=""
        imageUrl=""
        parentImage=h3.parent
        succChildImage=parentImage.findChildren('img')
        for img in succChildImage:
            imageUrl=img['data-src-template']
        for a in h3.findChildren('a',{'class':''}):
            url=a.get('href')
        hindudict={"title":title,"url":url,'imageUrl':imageUrl}
        theHinduArray.append(hindudict)
    return theHinduArray[0:10]
    
def econmicTimes():
    econmicTimesArray=[]
    etUrl="https://economictimes.indiatimes.com/prime"
    etR=requests.get(etUrl)
    etHtmlContent=etR.content
    etSoup=BeautifulSoup(etHtmlContent,'html.parser')
    etA=etSoup.findAll('a',{'class':'banner'})
    for i in range(0,5):
        imgTag=etA[i].findChildren('img')
        for j in imgTag:
            imageUrl=j['src']
            title=j['title']
        url='https://economictimes.indiatimes.com'+etA[i].get('href')
        etdict={'title':title,'url':url,'imageUrl':imageUrl}
        econmicTimesArray.append(etdict)
    
    print("economicTimesArray : ",len(econmicTimesArray))
    return econmicTimesArray

def bussinessToday():
    bussinessTodayArray=[]
    btUrl="https://www.businesstoday.in/entrepreneurship"
    btR=requests.get(btUrl)
    btHtmlContent=btR.content
    btSoup=BeautifulSoup(btHtmlContent,'html.parser')
    btLi=btSoup.findAll('li',{'class':'trd_tch_li'})
    print(len(btLi))
    for li in btLi:
    
        images=li.findChildren('img')
        atags=li.findChildren('a')
        imageUrl=''
        title=''

        for img in images:
            imageUrl=img['data-src']
            
        
        for a in atags:
            url=a.get('href')
            title=a.text.strip()
        btdict={'title':title,'url':url,'imageUrl':imageUrl}
        bussinessTodayArray.append(btdict)
    print("bussinessTodayArray : ",len(bussinessTodayArray))
    return bussinessTodayArray
