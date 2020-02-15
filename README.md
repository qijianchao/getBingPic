# getBingPic
自动获取bing每日壁纸，可以获取1920x1080和1920x1200两种格式。  
调用的核心是找到必应图片的网络地址，这个可以通过网络搜索快速找到解决方法： 我们可以访问这个链接：http://cn.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1 获得一个XML文件，里面包含了图片的地址。你可以试着直接访问该网址，可以得到xml格式的报文。  
主要包含url、urlbase、startdate、enddate等信息，默认给的url是1920x1080格式的，可以通过urlbase自行拼装其他尺寸的图片，不过最大格式也就是1920x1200了。  
这个方法比网上很多直接抓取bing的首页的方式要稳定很多，也更方便，本人已经使用了两年左右了，一直很稳定。  
需要注意的是，需要自行设置并建立savePath，在savePath下面还需要手动设置1920x1080和1920x1200两个文件夹，未做异常检查，图片会以startdate为文件名存放，同时在savepath文件夹会自动生成picNotes.txt，记录每天的文件信息（url，copyright等）。  
注：这个链接中的idx值为0表示当天的日期，1表示昨天，依次类推，经测试最多可以取数字7，再大也等同7  
n值表示以idx为基准取多长时间的图片，最大n值经测试为8天，可以自行尝试  
举例说明http://cn.bing.com/HPImageArchive.aspx?format=xml&idx=1&n=8 如果当前日期为2020年2月15日，表示取2月7日至2月14日的8张图片信息  