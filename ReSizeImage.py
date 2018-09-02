# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import os, sys
import re
import FileUtilty

def main():
    postfix = [".jpg",".png"]  # 设置要保存的文件格式
    image_path_list =  FileUtilty.all_path("E:\games",postfix)

    for image_path in image_path_list:
        print(image_path)
        FileUtilty.change_imaeg_size(image_path)
if __name__ == "__main__":
    main()
    input('press enter key to exit') 
