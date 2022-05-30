#!/usr/bin/env python
# coding: utf-8

# In[23]:


# yahoo電影每週新片

import requests

from bs4 import BeautifulSoup
 
url = 'https://movies.yahoo.com.tw/movie_thisweek.html'  # yahoo奇摩電影本週新片網址

response = requests.get(url)  # 取得網址
 
soup = BeautifulSoup(response.text, 'lxml')  # 解析網頁的內容並擷取我們所需的資料

info_items = soup.find_all('div', 'release_info')

for item in info_items:  # 透過for迴圈一筆筆將資料寫入檔案中
        
        # strip()為刪除多餘空白
        name = item.find('div', 'release_movie_name').a.text.strip()
        english_name = item.find('div', 'en').a.text.strip()
        release_time = item.find('div', 'release_movie_time').text.split('：')[-1].strip()
        level = item.find('div', 'leveltext').span.text.strip()
        
        print('{}({}) 上映日：{} 期待度：{}'.format(name, english_name, release_time, level))
        

    


# In[36]:


# 家常菜食譜資料

import csv

import requests

from bs4 import BeautifulSoup

url = "https://icook.tw/search/%E5%AE%B6%E5%B8%B8%E8%8F%9C/"  # icook網址

response = requests.get(url)  # 取得網址

soup = BeautifulSoup(recipe.text,'lxml')   # 解析網頁的內容並擷取我們所需的資料

info_items = soup.find_all('div','browse-recipe-content')


with open("食譜1.csv","w",encoding="UTF-8",newline="") as csv_file:

    csv_writer=csv.writer(csv_file)

    csv_writer.writerow(["菜名","食材"])  # 建立writer物件，就可以使用writerow的方法寫入檔案，先寫入欄位標題


    for item in info_items:  # 透過for迴圈一筆筆將菜單的資料寫入檔案中
        
        # strip()為刪除多餘空白    
        name = item.find("h2","browse-recipe-name").text.strip()  # 菜色名稱
        
        ingredient = item.find("p","browse-recipe-content-ingredient").text.strip()  # 食材      

        csv_writer.writerow([name,ingredient])
        
        print('名字：{} 食材：{}'.format(name, ingredient))
        


# In[38]:


# 天氣預報

import requests

url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-EA28D19F-8911-4F13-8FED-5A51E19CD73A&downloadType=WEB&format=JSON'

data = requests.get(url)   # 取得JSON檔案的內容為文字

data_json = data.json()    # 轉換成JSON格式

location = data_json['cwbopendata']['dataset']['location']   # 取出location的內容

for i in location:
    print(f'{i}')
    
import requests

#url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-EA28D19F-8911-4F13-8FED-5A51E19CD73A&downloadType=WEB&format=JSON'
data = requests.get(url)   # 取得JSON檔案的內容為文字
data_json = data.json()    # 轉換成JSON格式
location = data_json['cwbopendata']['dataset']['location']   


for i in location:  # 透過for迴圈一筆筆將天氣資料寫入檔案中
    
    city = i['locationName']    # 縣市名稱
    wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 未來8小時天氣現象
    maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
    mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
    pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
    
    print(f'{city} 未來8小時 {wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')
    
    


# In[ ]:




