"""# -*- coding: utf-8 -*-
Created at home on June 20, 2020

Python final assignment zhuzhuangtu part

@author: yang'yan'qing
"""
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
from collections import Counter
from jieba import posseg as psg
import matplotlib.pyplot as plt
 
mpl.rcParams['font.sans-serif']=['SimHei'] # X 轴可以显示中文
mpl.rcParams['axes.unicode_minus']= False # X 轴可以显示中文
 
font = FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=14)
f3 = open('./fencihou/忠犬八公的故事.txt','r').read()
stopwords = ['的', '这种', '这样', '还是', '就是', '这个','电影','这部','一部','片子','即使','虽然','但是','那个','看到','第一次','一次','一个','有些','什么',"宫崎","德勒","可以","没有","有些","时候","真的","很多","没有","不能","看过","画片","哈哈","不过","因为","哗啦","只是"]
 
wods =[x.word for x in psg.cut(f3) if len(x.word)>=2 and (x.word) not in stopwords]#当词语的长度合适且不在无效列表里时进行统计
word_count = Counter(wods)
print(word_count)#打印出词语及其数量
 
x=[x[0] for x in word_count.most_common(20)] #统计top20个关键字
y=[x[1] for x in word_count.most_common(20)] #统计top20个关键字出现的次数
fig = plt.figure(figsize=(10,5))#生成柱状图的尺寸
plt.grid(False)
plt.bar(x,y,color='lightskyblue')#x轴、y轴、柱状图颜色
plt.xlabel('关键词',FontProperties=font)#x轴对应元素名称
plt.ylabel('出现次数',FontProperties=font)#y轴对应元素名称
plt.title('短评关键词',FontProperties=font)#柱状图标题
plt.show()#打印柱状图