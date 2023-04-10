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
