# Douban crawls to pick up the word cloud
## 准备工作
使用jieba包对爬取到的短评进行分词处理，方便统计各个词语出现的次数。之后需要使用WordCloud包统计关键词出现的次数并生成词云。参考https://www.jianshu.com/p/62f155eb6ac5 的教程完成了两个包的安装。
## 技术选型
python3
## 开发环境
### 操作系统：Windows 10
### 编程语言:  python
### 开发工具: Visual Studio Code
### 代码托管平台: GitHub
## 部署环境  
本机测试
## 代码结构描述
###  定义函数获取url页面
###  定义函数解析url界面
###  爬取短评并将其写入一个txt文件
###  结巴分词
###  设置词云 无效关键词过滤
###  运行调试    
##   调试结果
![image](https://user-images.githubusercontent.com/58458394/230824407-fc4d6cb1-f83c-468f-8c6b-e3fa437ce021.png)
##   数据分析
数据分析分为两部分：第一部分：每部电影关键词的单独分析，以确定电影的主题、与所有电影的对比分析。第二部分：10部电影的对比，以分析电影的共性与不同。
##   单独分析
ps:防止过多的废话，这里只放置词云
### 1.肖申克的救赎 ![image](https://user-images.githubusercontent.com/58458394/230825229-8157c9c6-bab1-42a0-8f7a-f43ebc865329.png)
### 2.霸王别姬   ![image](https://user-images.githubusercontent.com/58458394/230825269-dc1726d1-1078-459c-996e-1b432e3cd519.png)
### 3.这个杀手不太冷  ![image](https://user-images.githubusercontent.com/58458394/230825299-72b7a51a-15db-4d28-8a94-d5bda64d10c0.png)
### 4.阿甘正传 ![image](https://user-images.githubusercontent.com/58458394/230825331-497be245-96ec-4464-9eef-2ec28d109176.png)
### 5.美丽人生  ![image](https://user-images.githubusercontent.com/58458394/230825349-ca946595-7b7c-4725-b6bb-64818a7ed677.png)
### 6.泰坦尼克号   ![image](https://user-images.githubusercontent.com/58458394/230825383-8b121088-6fd1-440c-884d-41158adbf4ed.png)
### 7.千与千寻 ![image](https://user-images.githubusercontent.com/58458394/230825470-a063057a-7ab1-48f8-9c1e-3c9369bda6a4.png)
### 8.辛特勒的名单 ![image](https://user-images.githubusercontent.com/58458394/230825508-345f5fcd-cc21-4dec-ac21-01a49382072b.png)
### 9.盗梦空间 ![image](https://user-images.githubusercontent.com/58458394/230825542-829d297a-2ac1-44c4-8872-bf4da1368ab1.png)
### 10.忠犬八公的故事 ![image](https://user-images.githubusercontent.com/58458394/230825568-1ba120d6-c6e1-48f2-bcc4-4b39848819e9.png)
## 不足及改进
1、爬取豆瓣短评只能爬取前十页，十页之后需要进行验证。
2、爬取短评后进行分词时难以识别部分特有的名词。
3、通过关键词对电影进行分析存在较大的片面性，难以全方位的了解电影内容及主题。
4、无法自动消除一些无效关键词，需要多次调试去除无效关键词。
