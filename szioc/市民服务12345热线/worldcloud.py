from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
import os

os.chdir(r'D:\华为科技\02-深圳IOC\02-市民服务分析报告\V4')
# backgroup_Image = plt.imread('sz.jpg') #笼罩图
f = open('施工.txt','r',encoding="utf8").read()  # 生成词云的文档

wordcloud = WordCloud(
    background_color='white',  # 背景颜色，根据图片背景设置，默认为黑色
    # mask = backgroup_Image, #笼罩图
    font_path='C:\Windows\Fonts\STZHONGS.TTF', # 若有中文需要设置才会显示中文
    contour_width=2,
    contour_color = 'blue',
    width=1920,
    height=1000
    # margin=2
).generate(f)  # generate 可以对全部文本进行自动分词
# 参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 保存图片：默认为此代码保存的路径
wordcloud.to_file('sg.jpg')