import requests
from bs4 import BeautifulSoup

def get_corona_summary():
    url="http://ncov.mohw.go.kr/"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'lxml')
    corona=soup.select("ul.liveNum>li>span.num")
    covid19=soup.select("ul.liveNum>li>strong.tit")

    results={
        "확진환자":int(corona[0].text.replace(',','').replace('(누적)','')),
        "환자":int(corona[1].text.replace(',',''),
        "치료자":int(corona[2].text.replace(',',''),
        "사망":int(corona[3].text.replace(',',''),
    }

    return results
    

if __name__=="__main__":
    get_corona_summary()
