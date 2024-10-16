import requests
import re

# url = 'https://www.biqooge.com/0_1/1.html'
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
# }

# reg = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(?P<内容>.*?)<br />', re.S)

# response = requests.get(url, headers=headers)
# response.encoding = 'gbk'  

# result = re.finditer(reg, response.text)
# response.close()

# with open("output.txt","w",encoding='gbk',newline='') as f:
#     for iterm in result:
#         f.write(iterm.group('内容')+'\n')
# f.close
# print('over')
j=4
for i in range(5468860,5468878,3):
    url = f'https://www.biqooge.com/8_8885/{i}.html'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    reg = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(?P<内容>.*?)<br />', re.S)

    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'  
    
    response.close()

    result = re.finditer(reg, response.text)
    response.close()

    with open("output.txt","a",encoding='gbk',newline='') as f:
        f.write(f'第{j+1}章\n')
        print(f'在打印第{j+1}章')
        j+=1
        for iterm in result:
            print(iterm.group('内容'))
            f.write(iterm.group('内容')+'\n')

print('over')
f.close