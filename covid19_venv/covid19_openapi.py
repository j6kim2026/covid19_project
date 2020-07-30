import requests
from pprint import pprint
from datetime import date, timedelta
import xmltodict
import json

def get_city_data():
    url="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params= {
        'serviceKey':'i9r3fo2QYiyVi9YInRRaIV5fNBT6z/Ni7UD5Hk+DSzXkOECxA4GQkSufKsTuGtUWffOVPh0k/vwyDdxm3xHebQ==', 
        'pageNo':'1', 
        'numOfRows':'30', 
        'startCreate_dt': '20200727', 
        'endCreateDt': '20200727'
    }

    res=requests.get(url, params=params)
    dict_data=xmltodict.parse(res.text)

    json_data=json.dumps(dict_data)
    dict_data=json.loads(json_data)
    pprint(dict_data)
    pprint(dict_data["response"]["body"]["items"]["item"][1])
    return dict_data

get_city_data()