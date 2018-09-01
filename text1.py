import requests #导入requests库
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器
web_url = 'https://play.google.com/store/apps/details?id=com.cityracing.speeddrifting&hl=en_US'
r = requests.get(web_url,headers=headers) #像目标url地址发送get请求，返回一个response对象
all_a = BeautifulSoup(r.text, 'lxml').find_all('button', class_='NIc6yf')
for a in all_a: #循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
    #img_str = a['itemprop'] #a标签中完整的style字符串
    a = str(a).split("src=")[1]
    a = str(a).split(" ")[0]
    print(a)

