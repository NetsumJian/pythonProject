import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
from epointml.utils import DbPoolUtil
def data_extract(df):
    # 政府投资index
    政府投资_index = df[df['zjly'].str.split().map(lambda x: x[0].split('：')[1]).astype(float) > 50].index
    # 国企投资index
    国企投资_index = df[df['zjly'].str.split().map(lambda x: x[2].split('：')[1]).astype(float) > 50].index
    # 政府投资赋值
    df.loc[政府投资_index, 'zjly'] = '政府投资'
    # 国企投资赋值
    df.loc[国企投资_index, 'zjly'] = '国企投资'
    # 社会投资
    社会投资_index = df[df['zjly'] != '国企投资'][df[df['zjly'] != '国企投资']['zjly'] != '政府投资']['zjly'].index
    df.loc[社会投资_index, 'zjly'] = '社会投资'
    # 新改扩赋值
    df.loc[list(df[df['jsxz'] == '新建'].index) + list(df[df['jsxz'] == '改建'].index) + list(df[df['jsxz'] == '扩建'].index), 'jsxz'] = '新改扩'
    # 装修赋值
    df.loc[df[df['jsxz'] != '新改扩'].index, 'jsxz'] = '装修'
    timelimit = df['fzrq'].max() - timedelta(days=1461, hours=0, minutes=0, seconds=0)  # 时间范围

    df=df[df['pzrq']>datetime(timelimit.year,1,1)]  # 近五年的数据

    df_新改扩 = df[df['jsxz'] == '新改扩']
    df_装修 = df[df['jsxz'] == '装修']
    # 建设审批效率概况
    list1 = []
    for i in range(5):
        for j in ['社会投资', '政府投资', '国企投资']:
            if len(df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                       df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j]) != 0:
                a = int((df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                             df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j]['fzrq'] -
                         df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                             df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j][
                             'pzrq']).sum().days / len(
                    df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                        df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j]))
                b = len(df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                            df_新改扩[df_新改扩['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j])

                list1.append([timelimit.year + i, '新改扩项目', j, a, b])

    # 新改扩项目近五年开工时间、项目数量

    # int(pd.DataFrame(list1)[pd.DataFrame(list1)[2]=='社会投资'][3].sum()/pd.DataFrame(list1)[pd.DataFrame(list1)[2]=='社会投资'][4].sum())

    for i in range(5):
        for j in ['社会投资', '政府投资', '国企投资']:
            if len(df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                       df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j]) != 0:
                a = int((df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                             df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j]['fzrq'] -
                         df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                             df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j][
                             'pzrq']).sum().days / len(df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                                                           df_装修[df_装修['pzrq'].map(
                                                               lambda x: x.year) == timelimit.year + i]['zjly'] == j]))
                b = len(df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i][
                            df_装修[df_装修['pzrq'].map(lambda x: x.year) == timelimit.year + i]['zjly'] == j])
                list1.append([timelimit.year + i, '装修项目', j, a, b])
    # 装修项目近五年开工时间、项目数量
    
    
    for i in range(5):
        if len(df_新改扩[df_新改扩['pzrq'].map(lambda x:x.year)==timelimit.year+i]['zjly'])!=0:
            a=(df_新改扩[df_新改扩['pzrq'].map(lambda x:x.year)==timelimit.year+i]['fzrq']-df_新改扩[df_新改扩['pzrq'].map(lambda x:x.year)==timelimit.year+i]['pzrq']).sum().days/len(df_新改扩[df_新改扩['pzrq'].map(lambda x:x.year)==timelimit.year+i])
            b=len(df_新改扩[df_新改扩['pzrq'].map(lambda x:x.year)==timelimit.year+i]) 
            list1.append([timelimit.year+i,'新改扩项目','总体',int(a),b])

    for i in range(5):
        if len(df_装修[df_装修['pzrq'].map(lambda x:x.year)==timelimit.year+i]['zjly'])!=0:
            a=(df_装修[df_装修['pzrq'].map(lambda x:x.year)==timelimit.year+i]['fzrq']-df_装修[df_装修['pzrq'].map(lambda x:x.year)==timelimit.year+i]['pzrq']).sum().days/len(df_装修[df_装修['pzrq'].map(lambda x:x.year)==timelimit.year+i])
            b=len(df_装修[df_装修['pzrq'].map(lambda x:x.year)==timelimit.year+i]) 
            list1.append([timelimit.year+i,'装修项目','总体',int(a),b])

    list1.append(
        ['近五年', '新改扩项目', '总体', int((df_新改扩['fzrq'] - df_新改扩['pzrq']).map(lambda x: x.days).sum() / len(df_新改扩)),
         len(df_新改扩)])
    # 近五年新改扩项目总体开工时间、项目数量

    list1.append(['近五年', '装修项目', '总体', int((df_装修['fzrq'] - df_装修['pzrq']).map(lambda x: x.days).sum() / len(df_装修)),
                  len(df_装修)])
    # 近五年装修项目总体开工时间、项目数量
    
    list1.append(['近五年','全部','总体',int((df['fzrq']-df['pzrq']).map(lambda x:x.days).sum()/len(df)) ,len(df)])
    #近五年全部项目总体开工时间、项目数量

    df_list1 = pd.DataFrame(list1)

    df_list1.columns = ['year', 'xmlx', 'xmxl', 'kgsj', 'xmsl']
    #近五年平均开工时间
    df_list1['pjkgsj'] = 0

    for j in ['新改扩项目', '装修项目']:
        for i in ['社会投资', '政府投资', '国企投资','总体']:
            df_list1.loc[df_list1[df_list1['xmlx']==j][df_list1[df_list1['xmlx']==j]['xmxl']==i]['pjkgsj'].index,'pjkgsj']=int((df_list1[df_list1['xmlx']==j][df_list1[df_list1['xmlx']==j]['xmxl']==i]['kgsj'].sum()/len(df_list1[df_list1['xmlx']==j][df_list1[df_list1['xmlx']==j]['xmxl']==i])))

    #建表，没有数据的年份展示NaN
    df_list1['kgsj'] = df_list1['kgsj'].astype(str)
    df_list1['xmsl'] = df_list1['xmsl'].astype(str)
    df_list1['pjkgsj'] = df_list1['pjkgsj'].astype(str)

    df_frame = pd.DataFrame()  # columns=['year','xmlx','xmxl','kgsj','xmsl','pjkgsj'])

    # columns=['year','xmlx','xmxl','kgsj','xmsl','pjkgsj']

    for i in range(5):
        for l in ['新改扩项目', '装修项目']:
            for j in ['社会投资', '政府投资', '国企投资']:
                a=df_list1[df_list1['xmlx']==l][df_list1[df_list1['xmlx']==l]['xmxl']==j]['pjkgsj'].iloc[0]
                df_frame=df_frame.append([['{}'.format(timelimit.year+i),'{}'.format(l),'{}'.format(j),np.nan,np.nan,'{}'.format(a)]])
            
    df_frame.columns = ['year', 'xmlx', 'xmxl', 'kgsj', 'xmsl', 'pjkgsj']

    df_total = pd.concat([df_list1, df_frame])
    
    df_total.loc[df_total[df_total['xmlx']=='全部']['pjkgsj'].index,'pjkgsj']=df_total[df_total['xmlx']=='全部']['kgsj'].iloc[0]
    df_total.loc[df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='新改扩项目'][df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='新改扩项目']['year']=='近五年'].index,'pjkgsj']=df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='新改扩项目'][df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='新改扩项目']['year']=='近五年']['kgsj'].iloc[0]
    df_total.loc[df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='装修项目'][df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='装修项目']['year']=='近五年'].index,'pjkgsj']=df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='装修项目'][df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='装修项目']['year']=='近五年']['kgsj'].iloc[0]

    df_zx=df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='装修项目'][df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='装修项目']['year']!='近五年']

    df_xgk=df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='新改扩项目'][df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='新改扩项目']['year']!='近五年']

    df_total.loc[df_xgk.index,'pjkgsj']=df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='新改扩项目'][df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='新改扩项目']['year']=='近五年']['kgsj'].iloc[0]
    #int(df_xgk['kgsj'].astype(int).sum()/len(df_xgk))

    df_total.loc[df_zx.index,'pjkgsj']=df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='装修项目'][df_total[df_total['xmxl']=='总体'][df_total[df_total['xmxl']=='总体']['xmlx']=='装修项目']['year']=='近五年']['kgsj'].iloc[0]
    #int(df_zx['kgsj'].astype(int).sum()/len(df_zx))

    df_total['year'] = df_total['year'].astype(str)
    df_total['xmlx'] = df_total['xmlx'].astype(str)
    df_total['xmxl'] = df_total['xmxl'].astype(str)
    # df_total['kgsj']=df_total['kgsj'].astype(int)

    df_total = df_total.drop_duplicates(subset=['year', 'xmlx', 'xmxl'], keep='first')

    df_total = df_total.reset_index().drop(['index'], axis=1)
    # 项目详情展示

    df['kgsj'] = (pd.to_datetime(df['fzrq']) - df['pzrq']).map(lambda x: x.days)

    # df['fzrq']=df['fzrq'].map(lambda x:x.date())

    df_新改扩项目 = df[df['jsxz'] == '新改扩'][df[df['jsxz'] == '新改扩']['zjly'] == '政府投资'].loc[:,
               ['bjbh', 'xmmc', 'jsdw', 'ztz', 'zmj', 'pzrq', 'fzrq', 'kgsj']]

    df_装修项目 = df[df['jsxz'] == '装修'][df[df['jsxz'] == '装修']['zjly'] == '政府投资'].loc[:,
              ['bjbh', 'xmmc', 'jsdw', 'ztz', 'zmj', 'pzrq', 'fzrq', 'kgsj']]

    df_新改扩项目['xmlx'] = '新改扩项目'

    df_装修项目['xmlx'] = '装修项目'

    df_项目 = df_新改扩项目.append(df_装修项目)

    df_项目['fzrq'] = df_项目['fzrq'].astype(str)
    df_项目['pzrq'] = df_项目['pzrq'].astype(str)
    df_项目=df_项目[datetime.now()-pd.to_datetime(df_项目['fzrq'])<timedelta(days=365)].sort_values('kgsj',ascending=False)
    df_项目['fzrq']=df_项目['fzrq'].map(lambda x:x.split(' ')[0])
    return df_total,df_项目