from selenium import webdriver
import csv
import requests
from bs4 import BeautifulSoup
import time,datetime
import sys
from selenium.webdriver.support.ui import Select


url="https://www.ettoday.net/news/news-list.htm"

options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)
now = datetime.datetime.now()

page=0
with open('90020.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('日期','分類','連結'))
    writer.writerow(['標題'])
    

    for i in range(5):
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_h3=sp.select("div.part_list_2 > h3 > a")#標題跟網址用
        search_a=sp.select("div.part_list_2 > h3 > span")#時間
        search_b=sp.select("div.part_list_2 > h3 > em")#分類
                       
        for i in range(1):  
            print(page)
            print(search_a[i].text,end=' ')
            print(search_b[i].text,end=' ')
            print(search_h3[i].text,end=' ')
            print(search_h3[i].get('href'))
            
            writer.writerow([search_a[i].text,search_b[i].text,search_h3[i].get('href')])
            writer.writerow([search_h3[i].text])
           

        delta = datetime.timedelta(days=1)
        now= now-delta
        n_days1=now.strftime('%Y%m%d')
        a=n_days1[-2:]
        
        a=int(a)#避免7號變成07號
        a=str(a)
        
        b=n_days1[-4:-2]
        
        b=int(b)#避免7月變成07月
        b=str(b)
        #自動化抓取日期
        driver.find_element_by_id("selD").click()
        Select(driver.find_element_by_id("selD")).select_by_visible_text(b)
        time.sleep(2)
        driver.find_element_by_id("selM").click()
        driver.find_element_by_id("selD").click()
        time.sleep(2) # 必須加入等待，否則會有誤動作
        Select(driver.find_element_by_id("selD")).select_by_visible_text(a)
        driver.find_element_by_id("selD").click()
        time.sleep(2)
        driver.find_element_by_id("button").click()
        time.sleep(2)  # 必須加入等待，否則會有誤動作
    
driver.close()               #關閉瀏覽器


sys.exit