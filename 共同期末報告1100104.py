 # -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:15:47 2020

@author: cis-user
"""
import csv
import time
import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

# w=str='請輸入目的地:'
# a=int('')
# destination-id=1366745&q-台北市
# destination-id=1728696&q-新北市
# destination-id=1636762&q-基隆
# destination-id=1726032&q-桃園
# destination-id=1636763&q-新竹
# destination-id=1636764&q-苗栗
# destination-id=1725831&q-雲林
# destination-id=1639034&q-嘉義
# destination-id=1638509&q-台南
# destination-id=1634719&q-高雄
# destination-id=1639080&q-屏東
# destination-id=1639068&q-花蓮
# destination-id=1727507&q-台東
# a = str(1366745)
# b = str(1728696)

t = input("請輸入目的地:")
m = input("請輸入住期月份:")
d = input("請輸入住日期:")
n = input("請輸離開日期:")
y ="2021"
r = input("請輸入房間數:")
p = input("請輸入成人人數:")
c= input("請輸入兒童人數:")
l= input("請輸入兒童年齡"+"兒童年齡請小於17歲:")

dict_1 = {'台北':str(1366745),'新北':str(1728696),'基隆':str(1636762),'桃園':str(1726032),'新竹':str(1636763),'苗栗':str(1636764),'台中':str(1636668),'彰化':str(1639030),'南投':str(1639030),
'雲林':str(1725831),'嘉義':str(1639034),'台南':str(1638509),'高雄':str(1634719),'屏東':str(1639080),'花蓮':str(1639068),'台東':str(1727507)}

a = str("https://tw.hotels.com/search.do?destination-id="+(dict_1.get(str(t)))+"&q-check-in="+(y)+"-"+(m)+"-"+(d)+"&q-check-out="+(y)+"-"+(m)+"-"+(n)+"&q-rooms="+(r)+"&q-room-0-adults="+(p)+"&q-room-0-children="+(c)+"&q-room-0-child-0-age="+(l)+"&sort-order=BEST_SELLER")


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver =webdriver.Chrome(chrome_options=options)
# driver.get("https://tw.hotels.com/search.do?resolved-location=CITY%3A1366745%3AUNKNOWN%3AUNKNOWN&f-distance=2.0&f-lid=11129943&destination-id=1366745&q-destination=%E5%8F%B0%E5%8C%97,%20%E5%8F%B0%E7%81%A3&q-check-in=2021-01-01&q-check-out=2021-01-03&q-rooms=2&q-room-0-adults=1&q-room-0-children=1&q-room-0-child-0-age=8&q-room-1-adults=1&q-room-1-children=2&q-room-1-child-0-age=12&q-room-1-child-1-age=8&sort-order=PRICE")
driver.get(a)

page=0
with open('Hotels1.com.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(("旅館名稱","價格","星級","地址",['連結']))
   
   
       

    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("article > section > div > h3 > a ")
    search_price=sp.select(" article > section > aside > div.price")
    search_star=sp.select("article > section > div > div > div.additional-details.resp-module > span")
    search_add=sp.select("article > section > div > address > span")
    search_link=sp.select("article > section > div > h3 > a ")
    # search_c=sp.select("div.part_list_2 > h3 > a")

    for i in range(len(search_name)):
       
        print(search_name[i].text,end=' ')
        print(search_price[i].text,end=' ')
        print(search_star[i].text,end=' ')
        print(search_add[i].text,end=' ')
        print(search_link[i].get('href'))
        writer.writerow([search_name[i].text,search_price[i].text,search_star[i].text,search_add[i].text,'https://tw.hotels.com/'+search_link[i].get('href')])
        headers = {
               "Authorization": "Bearer " + "PCqwBI55qsWWugMeDWEPrJ4DMjp6xdx699Jyiih1Ghz",
               "Content-Type": "application/x-www-form-urlencoded"
           }
        message1=(search_name[i].text)
        message2=(search_price[i].text)
        message3=(search_star[i].text)
        message4=(search_add[i].text)
        message5=('https://tw.hotels.com/'+search_link[i].get('href'))
        
        
        params = {"message":'\n'+'[名稱]:'+message1+'\n'+"[價格]:"+message2+'\n'+"[星級]:"+message3+'\n'+"[地址]:"+message4+'\n'+'[連結]:'+message5 } 
        r = requests.post("https://notify-api.line.me/api/notify",]
                          headers=headers, params=params)
        print(r.status_code)  #20
# driver.close() #關閉瀏覽器
