"""
重新写的一个爬取网易云歌曲排行榜的工具
"""

import requests
import re 
import csv

url = "https://music.163.com/discover/toplist?id=3778678"

headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

response = requests.get(url, headers=headers)

reg = re.compile(r'"album":.*?"name":"(?P<歌曲>.*?)"'
                 r'.*?"artists":.*?"name":"(?P<歌手>.*?)"')

reg2 = re.compile(r'"album":{"id":.*?,"name":"(?P<专辑>.*?)".*?"name":"(?P<歌手>.*?)".*?"status":0,"name":"(?P<歌曲>.*?)"')

result = re.finditer(reg2, response.text)

response.close()

j=0
with open("wangyiyun_top.csv","w",encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    if j==0:
        writer.writerow(['名次','歌曲','歌手','专辑'])
    for iterm in result:
        j+=1
        writer.writerow([f'第{j}名',iterm.group('歌曲'),iterm.group('歌手'),iterm.group('专辑')])
f.close
print('over')

