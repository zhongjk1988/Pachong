# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import os, sys
import re
import FileUtilty
import PachongGoogle

class get_apk_pakageName():

    #类的初始化操作
    def __init__(self,pathName,aapt_path):  
        self.path = pathName
        self.aapt_path = aapt_path

    #获取apk的包名
    def getAppBaseInfo(self,parm_apk_path):  
        print(parm_apk_path)
        packagename = ""
        get_info_command = "%s dump badging %s" % (self.aapt_path, parm_apk_path)   #使用命令获取版本信息  aapt命令介绍可以相关博客
        output = os.popen(get_info_command).read()  #执行命令，并将结果以字符串方式返回
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output) #通过正则匹配，获取包名，版本号，版本名称

        if not match:
            print (output)
        else:
            packagename = match.group(1)
        return packagename

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        else:
            print(path, '文件夹已经存在了，不再创建')

    def logic(self):
        file_name = 0
        apk_info = {}
        postfix = [".apk"]  # 设置要保存的文件格式
        apk_path_list =  FileUtilty.all_path(self.path,postfix)
        #遍历apk并为每个apk创建一个目录
        for apk_path in apk_path_list:
           dst = self.path+"\\"+str(file_name)
           self.mkdir(dst)
           apk_name = os.path.basename(apk_path)
           os.rename(apk_path, dst+"\\"+str(file_name)+".apk")
           file_name += 1
        #重新获取apk的路径,并获得apk的包名 将包名和对应的apk的目录保存到apk_info字典里面
        apk_path_list =  FileUtilty.all_path(self.path,postfix)
        for apk_path in apk_path_list:
            pakageName = self.getAppBaseInfo(apk_path)
            apk_info[pakageName] = os.path.dirname(apk_path)
        return apk_info



if __name__=='__main__':
    GOOGLE_PATH = "https://play.google.com/store/apps/details?id="
    zh_CH = "&amp&hl=zh_CH"
    PATH = r"F:\games"
    path = os.path.abspath(os.path.dirname(__file__)) + "\\"
    aapt_path = path + "tools\\aapt.exe"  #解析工具aapt.exe地址
    apk_path = PATH
    getapkname = get_apk_pakageName(apk_path,aapt_path)
    apk_info =  getapkname.logic()
    beautifulPicture =  PachongGoogle.BeautifulPicture()
    for key,path in apk_info.items():
        if key !="":
            url = GOOGLE_PATH+key+zh_CH
            beautifulPicture.get_pic(url,path)

    #最后改图片大小
    #索引所有的图片
    postfix = [".jpg",".png"]  # 设置要保存的文件格式
    image_path_list =  FileUtilty.all_path(PATH,postfix)
    #遍历图片并修改大小
    for image_path in image_path_list:
        try:
            FileUtilty.change_imaeg_size(image_path)
        finally:
            pass
   # getAppBaseInfo(aapt_path, apk_path)

   #be =  BeautifulPicture()
   #be.get_pic('https://play.google.com/store/apps/details?id=com.avokiddo.games.thinkrolls_kings_and_queens','F:\\games\\0')

