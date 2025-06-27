import requests
import json
from datetime import date

api_key = "a0b4f66866fd6b6a92486a7edc7dccb47925cb6d8c8748be5de9c31ec2ccb88b"

departure_id = "TPE,TSA"     #出發地(機場代碼是三個大寫的字母代碼)
arrival_id = "HND,NRT"       #目的地
outbound_date = "2025-06-28"       #去程日期
#return_date = "2024-09-30"         #回程日期
currency = "TWD"                   #貨幣單位
hl = "zh-tw"                       #語言
flight_type = 2                    #搜尋航班類別(1:往返，2:單程，3:多城市轉機)
stops = 1                          #飛行途中的經停次數(0:不設限，1:直達，2:轉機1次以下，3:轉機2次以下) 
#adults = 1                         #成人人數
#include_airlines = "JL"            #搜尋的航空公司(複數用','隔開)
url = f"https://serpapi.com/search.json?engine=google_flights&api_key={api_key}&departure_id={departure_id}&arrival_id={arrival_id}&outbound_date={outbound_date}&currency={currency}&hl={hl}&type={flight_type}&stops={stops}"

response = requests.get(url)
print(response)
data = response.json()

# print(response)
print(data)

file_name = "flight_ticket1_"+str(date.today())+".json"
obj=open(file_name,"w", encoding="utf-8")
json.dump(data,obj,ensure_ascii=False,indent=4)  #寫入json檔
print("寫入json成功")






