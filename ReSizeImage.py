# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import os, sys
import re
import FileUtilty

def main():
    postfix = [".jpg",".png"]  # 设置要保存的文件格式
    image_path_list =  FileUtilty.all_path(r"F:\新建文件夹\待上\外\20180829",postfix)

    for image_path in image_path_list:
        print(image_path)
        FileUtilty.change_imaeg_size(image_path)
if __name__ == "__main__":
    main()
    input('press enter key to exit') 
