import requests
from bs4 import BeautifulSoup
import time
import csv
i = 1
file = open('manga.csv','w',encoding='UTF-8_sig')
file.write('სათაური,ნახვები')
sia=[]
for i in range(6):
    url=f'https://mangakakalot.com/manga_list?type=topview&category=all&state=all&page={i+1}'
    time.sleep(15)
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    section = soup.find('div',{'class': 'truyen-list'})
# print(section)
    mangalist = section.find_all('div',{'list-truyen-item-wrap'})
# print(mangalist)
    for each in mangalist:
        info = each.find('h3')
        info2 = each.find('div')
        title = info.a.text
        print(title)
        views = info2.span.text
        print(views)
        file.write(title + ',' + views + '\n')

