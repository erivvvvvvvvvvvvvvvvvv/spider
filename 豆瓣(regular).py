"""
一次爬虫的小练习，爬取豆瓣电影排行榜
"""
import requests
import re
import csv

for num in range(0, 250, 25):
    url = f'https://movie.douban.com/top250?start={num}&filter='
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }
    response = requests.get(url, headers=headers)

    reg = re.compile(r'<span class="title">(?P<电影>.*?)</span>'
                     r'.*?<p class="">.*?导演: (?P<导演>.*?) '
                     r'.*?<span class="rating_num" property="v:average">(?P<评分>.*?)</span>', re.S)
    
    result = re.finditer(reg, response.text)
    # for iterm in result:
    #     print(iterm.group('电影'), iterm.group('导演'), iterm.group('评分'))

    with open('douban.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if num==0:
            writer.writerow(['电影', '导演', '评分'])
        for iterm in result:
            writer.writerow([iterm.group('电影'), iterm.group('导演'), iterm.group('评分')])
        print(f'第{num+1}页写入成功！')
    f.close()
print('爬取完成')
response.close()


