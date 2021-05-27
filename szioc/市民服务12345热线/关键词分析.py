import os
import csv
import codecs
import jieba
import jieba.posseg as pseg

# 设置工作目录
os.chdir(r'C:\Users\dwx1024047\Documents\Work\12345热线\V4')

# 加载数据
txt = open("办结信息.txt", encoding="utf8").read()

# 加载用户自定义词典
# jieba.load_userdict("userdict.txt")

# 加载用户自定义禁词
stopwords = [line.strip() for line in open("stopword.txt", encoding="utf8").readlines()]
cixing = pseg.lcut(txt)
count = jieba.lcut(txt)
word_count = {}
word_flag = {}
all = []

# 词频统计
with codecs.open(filename='banjie.csv', mode='w',encoding="utf8")as f:
    write = csv.writer(f, dialect='excel')
    write.writerow(["word", "count", "flag"])

    # 词性统计
    for w in cixing:
        word_flag[w.word] = w.flag

    # 词频统计
    for word in count:
        if word not in stopwords:
            # 不统计字数为一的词
            if len(word) == 1:
                continue
            else:
                word_count[word] = word_count.get(word, 0) + 1

    items = list(word_count.items())
    # 按词频排序
    items.sort(key=lambda x: x[1], reverse=True)
    # 查询词频字典里关键字的词性
    for i in range(len(items)):
        word = []
        word.append(items[i][0])
        word.append(items[i][1])
        # 若词频字典里，该关键字有分辨出词性，则记录，否则为空
        if items[i][0] in word_flag.keys():
            word.append(word_flag[items[i][0]])
        else:
            word.append("")
        all.append(word)

    for res in all:
        write.writerow(res)
