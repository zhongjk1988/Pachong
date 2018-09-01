import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
import os  #导入os模块
import urllib.request

class BeautifulPicture():

    def __init__(self):  #类的初始化操作
        #使用这个会影响保存的图片
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  #给请求指定一个请求头来模拟chrome浏览器

    ##保存图片 tag是图片类型
    def save_img(self, url, name,tag): 
        
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        if img != 200:
            file_name = name + tag
            print('开始保存图片')
            f = open(file_name, 'ab')
            f.write(img.content)
            print(file_name,'图片保存成功！')
            f.close()
        else:
            print('图片网络请求失败...')
        '''
        file_name = name + tag
        urllib.request.urlretrieve(url,file_name)
        '''
    def save_description(self,path,contents):
        #以追加的方式打开如果文件不存在创建文件
        fd = open(path,'a',encoding='utf-8') 
        fd.write(contents)
    #    fd.writelines(contents)      #写入列表内容  
        fd.flush()
        fd.close()  
    def request(self, url):  #返回网页的response
        r = 200
        try:
            # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
            r = requests.get(url)  
        except Exception as e:
            r = 200
            print("网络请求失败:",e)
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')
    def get_pic(self,web_url,folder_path):
        print('开始网页get请求')
        r = self.request(web_url)
        if r != 200:
            print('开始获取所有a标签')
            screen = 0
            icon_num = 0
            #获取网页中的class为NIc6yf的所有button标签获得截图
            button_a = BeautifulSoup(r.text, 'lxml').find_all('button', class_='NIc6yf')  
            print('开始创建文件夹')
            self.mkdir(folder_path)  #创建文件夹
            print('开始切换文件夹')
            os.chdir(folder_path)   #切换路径至上面创建的文件夹
            #保存截图
            for a in button_a: #循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
                #img_str = a['itemprop'] #a标签中完整的style字符串
                a = str(a).split("src=")[1]
                a = str(a).split(" ")[0]
                #去掉头尾的双引号
                a = str(a).replace(r'"',"")
                screenName = "screen"+str(screen)
                self.save_img(a, screenName,".jpg")
                screen += 1
            #保存icon
            all_icon = BeautifulSoup(r.text, 'lxml').find_all('div', class_='dQrBL')
            for icon in all_icon: #循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
                icon = str(icon).split("src=")[1]
                icon = str(icon).split(" ")[0]
                icon = str(icon).replace(r'"',"")
                icon_name = "icon"+str(icon_num)
                self.save_img(icon, icon_name,".png") #调用save_img方法来保存图片
                icon_num += 1
            content = BeautifulSoup(r.text, 'lxml').find_all('meta',itemprop='description')
            self.save_description(folder_path+"\\"+"description.txt",str(content))
            '''
            if r"content='" in str(content) and r"' itemprop" in str(content):
                content = str(content).split(r"content='")[1]
                content = str(content).split(r"' itemprop")[0]
                self.save_description(folder_path+"\\"+"description.txt",str(content))
            '''



'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器
web_url = 'https://play.google.com/store/apps/details?id=com.cityracing.speeddrifting&hl=en_US'
r = 200
try:
    r = requests.get(web_url,headers=headers) #像目标url地址发送get请求，返回一个response对象
    #print(r.text)
except Exception as e:
     print("网络请求失败:",e)

if r != 200:
    all_a = BeautifulSoup(r.text, 'lxml').find_all('button', class_='NIc6yf')
    for a in all_a: #循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
        #img_str = a['itemprop'] #a标签中完整的style字符串
        a = str(a).split("src=")[1]
        a = str(a).split(" ")[0]
        #print(a)
    all_icon = BeautifulSoup(r.text, 'lxml').find_all('div', class_='dQrBL')
    for icon in all_icon: #循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
        #img_str = a['itemprop'] #a标签中完整的style字符串
        icon = str(icon).split("src=")[1]
        icon = str(icon).split(" ")[0]
        #print(icon)
    content = BeautifulSoup(r.text, 'lxml').find_all('meta',itemprop='description')
    content = str(content).split(r"content='")[1]
    content = str(content).split(r"' itemprop")[0]
    print(content)
else:
    print("网络请求失败")
'''