# -*- coding: utf-8 -*-
"""
Created at home on June 20, 2020
Python final assignment Crawling and taking bean petals part
@author: yang'yan'qing
"""
# -*-coding:utf-8-*-
import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread
import jieba

def getHtml(url):
    """获取url页面"""
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    req = urllib.request.Request(url,headers=headers)
    req = urllib.request.urlopen(req)
    content = req.read().decode('utf-8')
    return content

def getComment(url):
    """解析HTML页面"""
    html = getHtml(url)
    Comment = BeautifulSoup(html, 'html.parser')
    comments = Comment.findAll('span', 'short')
    onePageComments = []
    for comment in comments:
        # print(comment.getText()+'\n')
        onePageComments.append(comment.getText()+'\n')
    return onePageComments

if __name__ == '__main__':
    f = open('./短评/阿甘正传10.txt', 'w', encoding='utf-8') 
    for page in range(10):  # 豆瓣爬取多页评论需要验证。' + str(20*page) + '
        url = 'https://movie.douban.com/subject/1292720/comments?start=' + str(20*page) + '&limit=20&sort=new_score&status=P'
        print('第%s页的评论:' % (page+1))
        print(url + '\n')

        for i in getComment(url):
            f.write(i)
            print(i)
        print('\n')
text = open("./短评/阿甘正传10.txt","rb").read()
#结巴分词
wordlist = jieba.cut(text,cut_all=True)
wl = " ".join(wordlist)
#print(wl)#输出分词之后的txt
#把分词后的txt写入文本文件
fenciTxt  = open("./fencihou/阿甘正传.txt","w+")
fenciTxt.writelines(wl)
fenciTxt.close()
#设置词云
wc = WordCloud(background_color = "white", #设置背景颜色
               mask = imread('./images/aganzhengzhuan.jpg'),  #设置背景图片
               max_words = 2000, #设置最大显示的字数
               stopwords = ["的", "这种", "这样", "还是", "就是", "这个","电影","这部","一部","片子","即使","虽然","但是","那个","看到","第一次","一次","一个","有些","时候","真的","很多","没有","不能","看过"], #设置停用词
               font_path = "C:\Windows\Fonts\simkai.ttf",  # 设置为楷体 常规 #设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）      
               max_font_size = 200,  #设置字体最大值
               random_state = 30, #设置有多少种随机生成状态，即有多少种配色方案
    )
myword = wc.generate(wl)#生成词云
wc.to_file('./result/阿甘正传.jpg')
#展示词云图
plt.imshow(myword)
plt.axis("off")
plt.show()