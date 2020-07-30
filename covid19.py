import requests
from bs4 import BeautifulSoup

def get_corona_summary():
    url="http://ncov.mohw.go.kr/"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'lxml')
    corona=soup.select("ul.liveNum>li>span.num")
    covid19=soup.select("ul.liveNum>li>strong.tit")

    for x in range(0, len(corona)):
        print(covid19[x].text + ":" + corona[x].text)

if __name__=="__main__":
    get_corona_summary()
