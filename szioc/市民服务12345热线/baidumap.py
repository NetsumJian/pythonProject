import json
import requests
import pandas as pd
import os
import numpy as np
import time

def p2l(name):
    # 1、设置url和3个参数（输出格式，key，要翻译的地址）

    # output = 'json'
    ak = 'weui6qjrGlg3YTSLR2B1Be1Z7eQ8w9NU'
    url = 'http://api.map.baidu.com/place/v2/search?query=%s&region=深圳&output=json&ak=%s' %(name,ak)
    print(url)

    resp = requests.request('get',url)

    # 4、读取response字符串
    response_str = resp.text

    # 5、str转json
    response_json = json.loads(response_str)
    print(response_json)

    # 6、读json，
    lat=response_json['results'][0]['location']['lat']
    lng=response_json['results'][0]['location']['lng']

    return lat,lng

# os.chdir(r'D:\华为科技\02-深圳IOC\02-市民服务分析报告\V4')
# df = pd.read_excel('施工.xlsx',index_col='区域')
# locs = pd.DataFrame(np.random.randn(len(df),3),index=df.index,columns=['lat','lng','num'])
# locs['num'] = df['数量']
# for i in df.index:
#     try:
#         lat,lng = p2l(i)
#         locs['lat'][i] = lat
#         locs['lng'][i] = lng
#         time.sleep(5)
#     except Exception:
#         print(i)

# print(df.head())
# print(locs.head())

# locs.to_excel('locs.xlsx')
while True:
    name = input()
    try:
        loc = p2l(name)
        print(loc)
    except:
        pass
