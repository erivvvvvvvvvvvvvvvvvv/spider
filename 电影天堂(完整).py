

import requests
import re
import csv

url = 'https://www.dyttcn.com/'

resp1 = requests.get(url)
resp1.encoding='gb2312'
resp1.close()


reg1 = re.compile(r'<div class="co_content222">.*?<ul>(?P<href>.*?)</ul>', re.S)    # 第一步，获取主页面总的数据
reg2 = re.compile(r"<li><a href='(?P<child_href>.*?)'", re.S)    # 第二步，从主页数据中获取进入连接
reg3 = re.compile(r'◎片　　名　(?P<name>.*?)</p>'
                  r'.*?◎豆瓣链接　(?P<url_1>.*?)</p>'
                  r'.*?<tbody>.*?<a href="(?P<url_2>.*?)">'               
                  , re.S)    # 第三步，进入页面获取数据
"""
r'.*?◎豆瓣链接　(?P<url_1></p>'
                  r'.*?<tbody>.*?<a href="(?P<url_2>">'
"""
child_href_list = []
obj1 = reg1.finditer(resp1.text)
for iterm in obj1:
    # print(iterm.group('href'))
    obj2 = reg2.finditer(iterm.group('href'))
    for iterm2 in obj2:
        # print(iterm2.group('child_href'))
        child_href = url + iterm2.group('child_href').strip('/')
        # print(child_href)
        child_href_list.append(child_href)

# print(child_href_list)


num = 0
# 写入文件
with open('move.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    for url in child_href_list:
        resp = requests.get(url)
        resp.close()
        resp.encoding='gb2312'
        obj = reg3.finditer(resp.text)
        for iterm in obj:
            if num==0:
                writer.writerow(['电影名字','豆瓣链接','迅雷链接'])
            writer.writerow([iterm.group('name'), iterm.group('url_1'), iterm.group('url_2')])
            print(f'正在打印第{num+1}部电影')
            num+=1
f.close()
print('打印完毕')
