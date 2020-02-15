#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__='qijianchao@163.com'
import urllib.request
import urllib.parse
import os
from xml.dom.minidom import parse
import xml.dom.minidom

#设置配置信息，包括 baseUrl,idx,n ，还包括 存放基本路径 savePath，picNotes文件全路径 
baseUrl = "https://cn.bing.com/HPImageArchive.aspx"
idx = "0"
n = "7"
bingUrl = baseUrl + '?idx=' + idx + '&n=' + n
savePath = "/Users/qjc/OneDrive/图片/Bing程序抓取"
#savePath = "/Users/qjc/Documents/PythonStudy"
picNotes = "picNotes.txt"

#通过url获取bing图片的xml信息，并解析xml信息，解析后逐个存放成1920x1080和1920x1200两种格式，并记录信息到picNotes文件中
page = urllib.request.urlopen(bingUrl)
html = page.read()
xmlStr = html.decode('utf-8')
print(xmlStr)
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parseString(xmlStr)
root = DOMTree.documentElement
images = root.getElementsByTagName('image')
images.reverse()
for image in images:
    startdate = image.getElementsByTagName('startdate')[0].firstChild.data
    print(startdate)
    fullstartdate = image.getElementsByTagName('fullstartdate')[0].firstChild.data
    print(fullstartdate)
    enddate = image.getElementsByTagName('enddate')[0].firstChild.data
    print(enddate)
    url = image.getElementsByTagName('url')[0].firstChild.data
    print(url)
    urlBase = image.getElementsByTagName('urlBase')[0].firstChild.data
    print(urlBase)
    copyright = image.getElementsByTagName('copyright')[0].firstChild.data
    print(copyright)
    # 判断1080文件是否已经存在，如果不存在执行下面的动作，否则continue
    if os.path.isfile(savePath + "/1920x1080/" + startdate + ".jpg"):
        continue
    else:
        # 将基本信息写入picNotes文件
        if not os.path.isfile(savePath + '/' + picNotes):
            picFile = open(savePath + '/' + picNotes,'w')
        else :
            picFile = open(savePath + '/' + picNotes,'r+')
            picFile.read() # 不加入这句文件指针会在开头，会覆盖文本信息
        picFile.write('\n开始日期：' + startdate)
        picFile.write('\n完整日期：' + fullstartdate)
        picFile.write('\n结束日期：' + enddate)
        picFile.write('\nURL：' + url)
        picFile.write('\n基础URL：' + urlBase)
        picFile.write('\n版权信息：' + copyright)
        picFile.write('\n')
        picFile.close()
        # 生成1920x1080分辨率的图片
        u = urllib.request.urlopen("https://cn.bing.com" + url)
        data = u.read()
        f = open(savePath + "/1920x1080/" + startdate + ".jpg", 'wb')
        f.write(data)
        f.close()
        # 接着是生成1920x1200分辨率的图片
        u = urllib.request.urlopen("https://cn.bing.com" + url.replace("1920x1080","1920x1200"))
        data = u.read()
        f = open(savePath + "/1920x1200/" + startdate + ".jpg", 'wb')
        f.write(data)
        f.close()
print("end")