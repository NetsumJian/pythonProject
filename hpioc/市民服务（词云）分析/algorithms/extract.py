import pandas as pd
import numpy as np
import jieba
from datetime import datetime
from datetime import timedelta
from collections import Counter
from epointml.utils import DbPoolUtil
def data_extract(df):
    list_keywords = ['动迁', '物业', '房屋', '搭建', '扰民', '噪音', '施工', '协调', '垃圾', '拆除', '冠状病毒', '装修', '安装', '违章', '停车', '经营',
                     '维修', '群租', '人行道', '安全隐患', '工资', '违章建筑', '漏水', '停放', '堆放', '户口', '设摊', '无证', '楼道', '改造', '弄堂',
                     '环境', '垃圾桶', '合同', '拖欠', '出租', '补贴', '非机动车', '租房', '租赁', '停车费', '居住证', '幼儿园', '油烟', '绿化', '雨棚',
                     '改建', '消防通道', '跨门', '污水', '杂物', '民宿', '外墙', '广告', '建筑工地', '废品', '脚手架', '补助', '厕所', '消防', '承重墙',
                     '残疾人', '垃圾堆', '房产证', '堵塞', '餐饮店', '物业管理', '拆违', '拖欠工资', '房屋结构', '充电', '菜场', '施工方', '清运', '市容',
                     '围墙', '保障', '积水', '养老院', '车库', '营业执照', '下水道', '损坏', '棋牌室', '火灾', '修剪', '封闭', '墙面', '拆掉', '危险',
                     '酒吧', '堆物', '脏乱差', '退款', '教育', '报修', '调解', '广告牌', '玻璃', '扩音', '廉租房', '破墙', '招牌', '疏通', '晾晒', '低保',
                     '扬尘', '入学', '业主大会']

    df.columns = ['TASKID', 'STREETNAME', 'COMMUNITYNAME', 'DESCRIPTION', 'ADDRESS', 'INFOTYPENAME', 'DISCOVERTIME']
    
    df.drop_duplicates(subset='TASKID',keep='last',inplace=True)
    df = pd.concat([df[df['INFOTYPENAME'] == '12345热线'], df[df['INFOTYPENAME'] == '市民热线']], axis=0)

    df['DISCOVERTIME'] = pd.to_datetime(df['DISCOVERTIME'])

    df = df.reset_index().drop('index', axis=1)

    df.loc[df[df['STREETNAME'] == '半淞园街道'].index, 'STREETNAME'] = '半淞园路街道'

    df['STREETNAME_COMMUNITYNAME'] = df['STREETNAME'] + df['COMMUNITYNAME']

    df_threemonths = df[datetime.now() - df['DISCOVERTIME'] <= timedelta(days=90, hours=0, minutes=0, seconds=0)]
    df_ninemonths = df[(datetime.now() - df['DISCOVERTIME']) > timedelta(days=90, hours=0, minutes=0, seconds=0)][(datetime.now() -df[(datetime.now() - df['DISCOVERTIME']) > timedelta(days=90,hours=0,minutes=0,seconds=0)]['DISCOVERTIME']) < timedelta(days=365, hours=0, minutes=0, seconds=0)]
    df_months = df[datetime.now() - df['DISCOVERTIME'] >= timedelta(days=365, hours=0, minutes=0, seconds=0)]

    sentence_depart_threemonths = df_threemonths['DESCRIPTION'].apply(jieba.lcut, 1)
    sentence_depart_ninemonths = df_ninemonths['DESCRIPTION'].apply(jieba.lcut, 1)
    sentence_depart_months = df_months['DESCRIPTION'].apply(jieba.lcut, 1)

    list_threemonths = []
    for i in sentence_depart_threemonths:
        for j in i:
            list_threemonths.append(j)
    ans_threemonths = [x for x in list_threemonths if len(x) > 1 and x in list_keywords]  # 去除停用词

    list_ninemonths = []
    for i in sentence_depart_ninemonths:
        for j in i:
            list_ninemonths.append(j)
    ans_ninemonths = [x for x in list_ninemonths if len(x) > 1 and x in list_keywords]

    list_months = []
    for i in sentence_depart_months:
        for j in i:
            list_months.append(j)
    ans_months = [x for x in list_months if len(x) > 1 and x in list_keywords]

    dict_final = (Counter(ans_threemonths * 6) + Counter(ans_months) + Counter(ans_ninemonths * 3))

    dict_final = dict(sorted(dict_final.items(), key=lambda d: d[1], reverse=True))

    df_keywords = pd.DataFrame(sorted(dict_final.items(), key=lambda d: d[1], reverse=True))

    df_keywords.columns = ['keywords', 'num_keywords']

    df_keywords = df_keywords[:50]

    return  df_keywords