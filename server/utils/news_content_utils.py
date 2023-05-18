content={}
def theHindu(contentSoup):
    description=""
    contentTitle=contentSoup.find('h1',{'class':'title'})   
    contentSubTitle=contentSoup.find('h3',{'class':'sub-title'})
    contentImage=contentSoup.find('source')['srcset']
    contentDescription=contentSoup.find('div',{'class':'articlebodycontent'})
    contentDescriptionPara=contentDescription.findChildren('p')
    for p in contentDescription:
        description=description+p.text.strip()+'\n'
        
    content['title']=contentTitle.text.strip()
    content['sub_title']=contentSubTitle.text.strip()
    content['img_url']=contentImage
    content['description']=description
    return content

def bussinessToday(contentSoup):
    description=""
    contentTitle=contentSoup.find('div',{'class':'story-heading'})   
    contentSubTitle=contentSoup.find('div',{'class':'sab-head-tranlate-sec'})
    contentDivImage=contentSoup.find('div',{'class':'main-img'})
    contentImage=contentDivImage.findChild('img')
    # contentDecsDiv=contentSoup.find('story-with-main-sec')
    contenteDecsDiv=contentSoup.find('div',{'class':'story-with-main-sec'})
    contentDescDivChild=contenteDecsDiv.find('div')
    contentDescPara=contentDescDivChild.findChildren('p')
    for p in contentDescPara:
        description=description+p.text.strip()
        
    content['title']=contentTitle.text.strip()
    content['sub_title']=contentSubTitle.text.strip()
    content['img_url']=contentImage['data-src']
    content['description']=description
    return content

def economictimes(contentSoup):
    description=""
    contentTitle=contentSoup.find('h1',{'class':'artTitle'})   
    contentSubTitle=contentSoup.find('h2',{'class':'artSyn'})
    contentDescription=contentSoup.find('div',{'class','artText'})
    contentImage=contentSoup.find('div',{'class':'artImg'}).findChild('figure').findChild('img')
    # print(contentSubTitle)
    content['title']=contentTitle.text.strip()
    content['sub_title']=contentSubTitle.text.strip()
    content['description']=contentDescription.text.strip()
    content['img_url']=contentImage['src']
    return content