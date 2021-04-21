import pandas as pd
import datetime

def niu_nai_total(df):

    df.columns = ['人数', '身份证', '年龄', '街道', '性别']
    df.dropna(axis=0, how='any', inplace=True)
    df.drop_duplicates(subset=['身份证'], keep='first', inplace=True)
    df.drop('身份证', inplace=True, axis=1)
    df.reset_index(drop=True, inplace=True)
    df['t'] = df['年龄'].str.isdigit()
    df = df[df['t'] == True]
    df.reset_index(drop=True, inplace=True)
    df = df.drop('t',axis = 1)
    df1 = df.pivot_table(index=['街道', '性别', '年龄'], values='人数', aggfunc='count').reset_index()
    df2 = pd.DataFrame()
    df2['人数'] = df1['人数']
    df2['年龄'] = df1['年龄']
    df2['街道'] = df1['街道']
    df2['性别'] = df1['性别']
    df = df2
    df['年龄'] = df['年龄'].astype('int')
    df['年龄'] = datetime.datetime.now().year - df['年龄']
    df['人数1'] = df['人数'] * 1.01
    df['年龄1'] = df['年龄'] + 1
    df['人数2'] = df['人数1'] * 1.01
    df['年龄2'] = df['年龄1'] + 1
    df['人数3'] = df['人数2'] * 1.01
    df['年龄3'] = df['年龄2'] + 1
    df['人数4'] = df['人数3'] * 1.01
    df['年龄4'] = df['年龄3'] + 1
    df['人数5'] = df['人数4'] * 1.01
    df['年龄5'] = df['年龄4'] + 1
    df['人数1'] = df['人数1'].apply(lambda x: round(x, 0))
    df['人数1'] = df['人数1'].apply(lambda x: int(x))
    df['人数2'] = df['人数2'].apply(lambda x: round(x, 0))
    df['人数2'] = df['人数2'].apply(lambda x: int(x))
    df['人数3'] = df['人数3'].apply(lambda x: round(x, 0))
    df['人数3'] = df['人数3'].apply(lambda x: int(x))
    df['人数4'] = df['人数4'].apply(lambda x: round(x, 0))
    df['人数4'] = df['人数4'].apply(lambda x: int(x))
    df['人数5'] = df['人数5'].apply(lambda x: round(x, 0))
    df['人数5'] = df['人数5'].apply(lambda x: int(x))
    df.drop(columns='性别', axis=1, inplace=True)
    df1 = df.groupby(['街道'])
    list1 = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']

    df11 = pd.DataFrame()
    df22 = pd.DataFrame()
    for j in range(len(list1)):
        df2 = df1.get_group(list1[j])

        m1 = 0
        for i in df2.index:
            if df.iloc[i, 1] >= 90:
                m1 = m1 + df.iloc[i, 0]
        print(m1)

        m2 = 0
        for i in df2.index:
            if df.iloc[i, 4] >= 90:
                m2 = m2 + df.iloc[i, 3]
        print(m2)

        m3 = 0
        for i in df2.index:
            if df.iloc[i, 6] >= 90:
                m3 = m3 + df.iloc[i, 5]
        print(m3)

        m4 = 0
        for i in df2.index:
            if df.iloc[i, 8] >= 90:
                m4 = m4 + df.iloc[i, 7]
        print(m4)

        m5 = 0
        for i in df2.index:
            if df.iloc[i, 10] >= 90:
                m5 = m5 + df.iloc[i, 9]
        print(m5)

        m6 = 0
        for i in df2.index:
            if df.iloc[i, 12] >= 90:
                m6 = m6 + df.iloc[i, 11]
        print(m6)

        list11 = [[list1[j], m1, m2, m3, m4, m5, m6]]
        df11 = pd.DataFrame(list11)
        df22 = df22.append(df11)

    df22.columns = ['JD', 'QN', '1ST', '2ND', '3RD', '4TH', '5TH']
    df22.reset_index(drop=True, inplace=True)

    year_1 = str(datetime.datetime.now().year)
    year_2 = str(datetime.datetime.now().year + 1)
    year_3 = str(datetime.datetime.now().year + 2)
    year_4 = str(datetime.datetime.now().year + 3)
    year_5 = str(datetime.datetime.now().year + 4)
    df22.columns=['JD','QN',year_1,year_2,year_3,year_4,year_5]
    list_f = []
    for i in range(10):
        for j in range(5):
            list_f.append([df22.iloc[i, 0], df22.columns[j + 2], df22.iloc[i, j + 2]])
    df33 = pd.DataFrame(list_f)
    df33.columns = ['jiedao', 'year_', 'num']

    return  df33

def niu_nai_qushi(df):

    df.columns = ['人数', '身份证', '年龄', '街道', '性别']
    df.dropna(axis=0, how='any', inplace=True)
    df.drop_duplicates(subset=['身份证'], keep='first', inplace=True)
    df.drop('身份证', inplace=True, axis=1)
    df.reset_index(drop=True, inplace=True)
    df['t'] = df['年龄'].str.isdigit()
    df = df[df['t'] == True]
    df.reset_index(drop=True, inplace=True)
    df = df.drop('t',axis = 1)
    df1 = df.pivot_table(index=['街道', '性别', '年龄'], values='人数', aggfunc='count').reset_index()
    df2 = pd.DataFrame()
    df2['人数'] = df1['人数']
    df2['年龄'] = df1['年龄']
    df2['街道'] = df1['街道']
    df2['性别'] = df1['性别']
    df = df2
    df['年龄'] = df['年龄'].astype('int')
    df['年龄'] = datetime.datetime.now().year - df['年龄']
    df['人数1'] = df['人数'] * 1.01
    df['年龄1'] = df['年龄'] + 1
    df['人数2'] = df['人数1'] * 1.01
    df['年龄2'] = df['年龄1'] + 1
    df['人数3'] = df['人数2'] * 1.01
    df['年龄3'] = df['年龄2'] + 1
    df['人数4'] = df['人数3'] * 1.01
    df['年龄4'] = df['年龄3'] + 1
    df['人数5'] = df['人数4'] * 1.01
    df['年龄5'] = df['年龄4'] + 1
    df['人数1'] = df['人数1'].apply(lambda x: round(x, 0))
    df['人数1'] = df['人数1'].apply(lambda x: int(x))
    df['人数2'] = df['人数2'].apply(lambda x: round(x, 0))
    df['人数2'] = df['人数2'].apply(lambda x: int(x))
    df['人数3'] = df['人数3'].apply(lambda x: round(x, 0))
    df['人数3'] = df['人数3'].apply(lambda x: int(x))
    df['人数4'] = df['人数4'].apply(lambda x: round(x, 0))
    df['人数4'] = df['人数4'].apply(lambda x: int(x))
    df['人数5'] = df['人数5'].apply(lambda x: round(x, 0))
    df['人数5'] = df['人数5'].apply(lambda x: int(x))
    df.drop(columns='性别', axis=1, inplace=True)
    df1 = df.groupby(['街道'])
    list1 = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']

    df11 = pd.DataFrame()
    df22 = pd.DataFrame()
    for j in range(len(list1)):
        df2 = df1.get_group(list1[j])

        m1 = 0
        for i in df2.index:
            if df.iloc[i, 1] >= 90:
                m1 = m1 + df.iloc[i, 0]
        print(m1)

        m2 = 0
        for i in df2.index:
            if df.iloc[i, 4] >= 90:
                m2 = m2 + df.iloc[i, 3]
        print(m2)

        m3 = 0
        for i in df2.index:
            if df.iloc[i, 6] >= 90:
                m3 = m3 + df.iloc[i, 5]
        print(m3)

        m4 = 0
        for i in df2.index:
            if df.iloc[i, 8] >= 90:
                m4 = m4 + df.iloc[i, 7]
        print(m4)

        m5 = 0
        for i in df2.index:
            if df.iloc[i, 10] >= 90:
                m5 = m5 + df.iloc[i, 9]
        print(m5)

        m6 = 0
        for i in df2.index:
            if df.iloc[i, 12] >= 90:
                m6 = m6 + df.iloc[i, 11]
        print(m6)

        list11 = [[list1[j], m1, m2, m3, m4, m5, m6]]
        df11 = pd.DataFrame(list11)
        df22 = df22.append(df11)


    df22.columns = ['JD', 'QN', '1ST', '2ND', '3RD', '4TH', '5TH']
    df22.reset_index(drop=True, inplace=True)
    year_1 = str(datetime.datetime.now().year)
    year_2 = str(datetime.datetime.now().year + 1)
    year_3 = str(datetime.datetime.now().year + 2)
    year_4 = str(datetime.datetime.now().year + 3)
    year_5 = str(datetime.datetime.now().year + 4)
    list_m_tr = [[df22['1ST'].sum(), df22['2ND'].sum(), df22['3RD'].sum(), df22['4TH'].sum(), df22['5TH'].sum()]]
    df_milk_tr = pd.DataFrame(list_m_tr)
    df_milk_tr.columns = [year_1, year_2, year_3, year_4, year_5]
    df_milk_tr1 = df_milk_tr.T
    df_milk_tr1.reset_index(inplace=True)
    df_milk_tr1.columns = ['year_', 'num']

    return  df_milk_tr1

def niu_nai_degree(df):

    df.columns = ['人数', '身份证', '年龄', '街道', '性别']
    df.dropna(axis=0, how='any', inplace=True)
    df.drop_duplicates(subset=['身份证'], keep='first', inplace=True)
    df.drop('身份证', inplace=True, axis=1)
    df.reset_index(drop=True, inplace=True)
    df['t'] = df['年龄'].str.isdigit()
    df = df[df['t'] == True]
    df.reset_index(drop=True, inplace=True)
    df = df.drop('t',axis = 1)
    df1 = df.pivot_table(index=['街道', '性别', '年龄'], values='人数', aggfunc='count').reset_index()
    df2 = pd.DataFrame()
    df2['人数'] = df1['人数']
    df2['年龄'] = df1['年龄']
    df2['街道'] = df1['街道']
    df2['性别'] = df1['性别']
    df = df2
    df['年龄'] = df['年龄'].astype('int')
    df['年龄'] = datetime.datetime.now().year - df['年龄']
    df['人数1'] = df['人数'] * 1.01
    df['年龄1'] = df['年龄'] + 1
    df['人数2'] = df['人数1'] * 1.01
    df['年龄2'] = df['年龄1'] + 1
    df['人数3'] = df['人数2'] * 1.01
    df['年龄3'] = df['年龄2'] + 1
    df['人数4'] = df['人数3'] * 1.01
    df['年龄4'] = df['年龄3'] + 1
    df['人数5'] = df['人数4'] * 1.01
    df['年龄5'] = df['年龄4'] + 1
    df['人数1'] = df['人数1'].apply(lambda x: round(x, 0))
    df['人数1'] = df['人数1'].apply(lambda x: int(x))
    df['人数2'] = df['人数2'].apply(lambda x: round(x, 0))
    df['人数2'] = df['人数2'].apply(lambda x: int(x))
    df['人数3'] = df['人数3'].apply(lambda x: round(x, 0))
    df['人数3'] = df['人数3'].apply(lambda x: int(x))
    df['人数4'] = df['人数4'].apply(lambda x: round(x, 0))
    df['人数4'] = df['人数4'].apply(lambda x: int(x))
    df['人数5'] = df['人数5'].apply(lambda x: round(x, 0))
    df['人数5'] = df['人数5'].apply(lambda x: int(x))
    df.drop(columns='性别', axis=1, inplace=True)
    df1 = df.groupby(['街道'])
    list1 = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']

    df11 = pd.DataFrame()
    df22 = pd.DataFrame()
    for j in range(len(list1)):
        df2 = df1.get_group(list1[j])

        m1 = 0
        for i in df2.index:
            if df.iloc[i, 1] >= 90:
                m1 = m1 + df.iloc[i, 0]
        print(m1)

        m2 = 0
        for i in df2.index:
            if df.iloc[i, 4] >= 90:
                m2 = m2 + df.iloc[i, 3]
        print(m2)

        m3 = 0
        for i in df2.index:
            if df.iloc[i, 6] >= 90:
                m3 = m3 + df.iloc[i, 5]
        print(m3)

        m4 = 0
        for i in df2.index:
            if df.iloc[i, 8] >= 90:
                m4 = m4 + df.iloc[i, 7]
        print(m4)

        m5 = 0
        for i in df2.index:
            if df.iloc[i, 10] >= 90:
                m5 = m5 + df.iloc[i, 9]
        print(m5)

        m6 = 0
        for i in df2.index:
            if df.iloc[i, 12] >= 90:
                m6 = m6 + df.iloc[i, 11]
        print(m6)

        list11 = [[list1[j], m1, m2, m3, m4, m5, m6]]
        df11 = pd.DataFrame(list11)
        df22 = df22.append(df11)

    df22.columns = ['JD', 'QN', '1ST', '2ND', '3RD', '4TH', '5TH']
    df22.reset_index(drop=True, inplace=True)


    list_degree = ['QN', '1ST', '2ND', '3RD', '4TH', '5TH']
    for i in range(len(list_degree)):
        df22.loc[
            ((df22[list_degree[i]] > 0) & (df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.1)), list_degree[
                i]] = 1
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.1) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.2)), list_degree[i]] = 2
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.2) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.3)), list_degree[i]] = 3
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.3) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.4)), list_degree[i]] = 4
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.4) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.5)), list_degree[i]] = 5
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.5) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.6)), list_degree[i]] = 6
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.6) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.7)), list_degree[i]] = 7
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.7) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.8)), list_degree[i]] = 8
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.8) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 0.9)), list_degree[i]] = 9
        df22.loc[((df22[list_degree[i]] > (df22[list_degree[i]].max()) * 0.9) & (
                    df22[list_degree[i]] <= (df22[list_degree[i]].max()) * 1)), list_degree[i]] = 10


    year_1 = str(datetime.datetime.now().year)
    year_2 = str(datetime.datetime.now().year + 1)
    year_3 = str(datetime.datetime.now().year + 2)
    year_4 = str(datetime.datetime.now().year + 3)
    year_5 = str(datetime.datetime.now().year + 4)
    df22.columns=['JD','QN',year_1,year_2,year_3,year_4,year_5]
    list_f = []
    for i in range(10):
        for j in range(5):
            list_f.append([df22.iloc[i, 0], df22.columns[j + 2], df22.iloc[i, j + 2]])
    df33 = pd.DataFrame(list_f)
    df33.columns = ['jiedao', 'year_', 'num']


    return  df33

def niu_nai_top5(df):

    df.columns = ['人数', '身份证', '年龄', '街道', '性别']
    df.dropna(axis=0, how='any', inplace=True)
    df.drop_duplicates(subset=['身份证'], keep='first', inplace=True)
    df.drop('身份证', inplace=True, axis=1)
    df.reset_index(drop=True, inplace=True)
    df['t'] = df['年龄'].str.isdigit()
    df = df[df['t'] == True]
    df.reset_index(drop=True, inplace=True)
    df = df.drop('t',axis = 1)
    df1 = df.pivot_table(index=['街道', '性别', '年龄'], values='人数', aggfunc='count').reset_index()
    df2 = pd.DataFrame()
    df2['人数'] = df1['人数']
    df2['年龄'] = df1['年龄']
    df2['街道'] = df1['街道']
    df2['性别'] = df1['性别']
    df = df2
    df['年龄'] = df['年龄'].astype('int')
    df['年龄'] = datetime.datetime.now().year - df['年龄']
    df['人数1'] = df['人数'] * 1.01
    df['年龄1'] = df['年龄'] + 1
    df['人数2'] = df['人数1'] * 1.01
    df['年龄2'] = df['年龄1'] + 1
    df['人数3'] = df['人数2'] * 1.01
    df['年龄3'] = df['年龄2'] + 1
    df['人数4'] = df['人数3'] * 1.01
    df['年龄4'] = df['年龄3'] + 1
    df['人数5'] = df['人数4'] * 1.01
    df['年龄5'] = df['年龄4'] + 1
    df['人数1'] = df['人数1'].apply(lambda x: round(x, 0))
    df['人数1'] = df['人数1'].apply(lambda x: int(x))
    df['人数2'] = df['人数2'].apply(lambda x: round(x, 0))
    df['人数2'] = df['人数2'].apply(lambda x: int(x))
    df['人数3'] = df['人数3'].apply(lambda x: round(x, 0))
    df['人数3'] = df['人数3'].apply(lambda x: int(x))
    df['人数4'] = df['人数4'].apply(lambda x: round(x, 0))
    df['人数4'] = df['人数4'].apply(lambda x: int(x))
    df['人数5'] = df['人数5'].apply(lambda x: round(x, 0))
    df['人数5'] = df['人数5'].apply(lambda x: int(x))
    df.drop(columns='性别', axis=1, inplace=True)
    df1 = df.groupby(['街道'])
    list1 = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']

    df11 = pd.DataFrame()
    df22 = pd.DataFrame()
    for j in range(len(list1)):
        df2 = df1.get_group(list1[j])

        m1 = 0
        for i in df2.index:
            if df.iloc[i, 1] >= 90:
                m1 = m1 + df.iloc[i, 0]
        print(m1)

        m2 = 0
        for i in df2.index:
            if df.iloc[i, 4] >= 90:
                m2 = m2 + df.iloc[i, 3]
        print(m2)

        m3 = 0
        for i in df2.index:
            if df.iloc[i, 6] >= 90:
                m3 = m3 + df.iloc[i, 5]
        print(m3)

        m4 = 0
        for i in df2.index:
            if df.iloc[i, 8] >= 90:
                m4 = m4 + df.iloc[i, 7]
        print(m4)

        m5 = 0
        for i in df2.index:
            if df.iloc[i, 10] >= 90:
                m5 = m5 + df.iloc[i, 9]
        print(m5)

        m6 = 0
        for i in df2.index:
            if df.iloc[i, 12] >= 90:
                m6 = m6 + df.iloc[i, 11]
        print(m6)

        list11 = [[list1[j], m1, m2, m3, m4, m5, m6]]
        df11 = pd.DataFrame(list11)
        df22 = df22.append(df11)


    df22.columns = ['JD', 'QN', '1ST', '2ND', '3RD', '4TH', '5TH']
    df22.reset_index(drop=True, inplace=True)

    list_m_top5 = [
        [df22.T[0].iloc[2:].sum(), df22.T[1].iloc[2:].sum(), df22.T[2].iloc[2:].sum(), df22.T[3].iloc[2:].sum(),
         df22.T[4].iloc[2:].sum(), df22.T[5].iloc[2:].sum(), df22.T[6].iloc[2:].sum(), df22.T[7].iloc[2:].sum(),
         df22.T[8].iloc[2:].sum(), df22.T[9].iloc[2:].sum()]]
    df_milk_top5 = pd.DataFrame(list_m_top5)
    df_milk_top5.columns = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']
    df_milk_top5 = pd.DataFrame(df_milk_top5.T.sort_values(by=0, ascending=False)[0].iloc[0:5])
    df_milk_top5.reset_index(inplace=True)
    df_milk_top5.columns = ['jd', 'num']

    return  df_milk_top5

def zhu_can_total(df,dfa):

    df.columns = ['人数', '身份证', '年龄', '街道', '性别']
    df.dropna(axis=0, how='any', inplace=True)
    df.drop_duplicates(subset=['身份证'], keep='first', inplace=True)
    df.drop('身份证', inplace=True, axis=1)
    df.reset_index(drop=True, inplace=True)
    df['t'] = df['年龄'].str.isdigit()
    df = df[df['t'] == True]
    df.reset_index(drop=True, inplace=True)
    df = df.drop('t',axis = 1)
    df1 = df.pivot_table(index=['街道', '性别', '年龄'], values='人数', aggfunc='count').reset_index()
    df2 = pd.DataFrame()
    df2['人数'] = df1['人数']
    df2['年龄'] = df1['年龄']
    df2['街道'] = df1['街道']
    df2['性别'] = df1['性别']
    df = df2
    df['年龄'] = df['年龄'].astype('int')
    df['年龄'] = datetime.datetime.now().year - df['年龄']
    df['人数1'] = df['人数'] * 1.01
    df['年龄1'] = df['年龄'] + 1
    df['人数2'] = df['人数1'] * 1.01
    df['年龄2'] = df['年龄1'] + 1
    df['人数3'] = df['人数2'] * 1.01
    df['年龄3'] = df['年龄2'] + 1
    df['人数4'] = df['人数3'] * 1.01
    df['年龄4'] = df['年龄3'] + 1
    df['人数5'] = df['人数4'] * 1.01
    df['年龄5'] = df['年龄4'] + 1
    df['人数1'] = df['人数1'].apply(lambda x: round(x, 0))
    df['人数1'] = df['人数1'].apply(lambda x: int(x))
    df['人数2'] = df['人数2'].apply(lambda x: round(x, 0))
    df['人数2'] = df['人数2'].apply(lambda x: int(x))
    df['人数3'] = df['人数3'].apply(lambda x: round(x, 0))
    df['人数3'] = df['人数3'].apply(lambda x: int(x))
    df['人数4'] = df['人数4'].apply(lambda x: round(x, 0))
    df['人数4'] = df['人数4'].apply(lambda x: int(x))
    df['人数5'] = df['人数5'].apply(lambda x: round(x, 0))
    df['人数5'] = df['人数5'].apply(lambda x: int(x))
    df.drop(columns='性别', axis=1, inplace=True)
    df1 = df.groupby(['街道'])
    list1 = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']

    dfb = dfa.groupby(['service_name'])
    dfc = dfb.get_group('老年人助餐')
    dfc = dfc[(dfc['datatime'] > (2019 * 100)) & (dfc['datatime'] < (2019 * 100 + 13))]
    dfd = dfc.groupby(['jzdjdhz'])
    df33 = pd.DataFrame()
    df44 = pd.DataFrame()
    for j in range(len(list1)):
        dfe = dfd.get_group(list1[j])
        list22 = [[list1[j], dfe.reset_index().count().iloc[0]]]
        df33 = pd.DataFrame(list22)
        df44 = df44.append(df33)

    df55 = pd.DataFrame()
    df66 = pd.DataFrame()
    for j in range(len(list1)):
        df2 = df1.get_group(list1[j])

        c1 = 0
        for i in df2.index:
            if df.iloc[i, 1] >= 65:
                c1 = c1 + df.iloc[i, 0]

        c2 = 0
        for i in df2.index:
            if df.iloc[i, 4] >= 65:
                c2 = c2 + df.iloc[i, 3]

        c3 = 0
        for i in df2.index:
            if df.iloc[i, 6] >= 65:
                c3 = c3 + df.iloc[i, 5]

        c4 = 0
        for i in df2.index:
            if df.iloc[i, 8] >= 65:
                c4 = c4 + df.iloc[i, 7]

        c5 = 0
        for i in df2.index:
            if df.iloc[i, 10] >= 65:
                c5 = c5 + df.iloc[i, 9]

        c6 = 0
        for i in df2.index:
            if df.iloc[i, 12] >= 65:
                c6 = c6 + df.iloc[i, 11]

        list33 = [[list1[j], c1, c2, c3, c4, c5, c6]]
        df55 = pd.DataFrame(list33)
        df66 = df66.append(df55)

    df66 = pd.merge(df66, df44, on=[0], how='inner')
    df66['1ST'] = (round(df66[2] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['2ND'] = (round(df66[3] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['3RD'] = (round(df66[4] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['4TH'] = (round(df66[5] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['5TH'] = (round(df66[6] / (df66['1_x'] / df66['1_y']), 0)).astype('int')

    df66.drop(axis=1, columns=['1_x', 2, 3, 4, 5, 6], inplace=True)
    df66.columns = ['JD', 'QN', '1ST', '2ND', '3RD', '4TH', '5TH']

    year_1 = str(datetime.datetime.now().year)
    year_2 = str(datetime.datetime.now().year + 1)
    year_3 = str(datetime.datetime.now().year + 2)
    year_4 = str(datetime.datetime.now().year + 3)
    year_5 = str(datetime.datetime.now().year + 4)
    df66.columns=['JD','QN',year_1,year_2,year_3,year_4,year_5]
    list_f = []
    for i in range(10):
        for j in range(5):
            list_f.append([df66.iloc[i, 0], df66.columns[j + 2], df66.iloc[i, j + 2]])
    df77 = pd.DataFrame(list_f)
    df77.columns = ['jiedao', 'year_', 'num']

    return  df77

def zhu_can_qushi(df,dfa):

    df.columns = ['人数', '身份证', '年龄', '街道', '性别']
    df.dropna(axis=0, how='any', inplace=True)
    df.drop_duplicates(subset=['身份证'], keep='first', inplace=True)
    df.drop('身份证', inplace=True, axis=1)
    df.reset_index(drop=True, inplace=True)
    df['t'] = df['年龄'].str.isdigit()
    df = df[df['t'] == True]
    df.reset_index(drop=True, inplace=True)
    df = df.drop('t',axis = 1)
    df1 = df.pivot_table(index=['街道', '性别', '年龄'], values='人数', aggfunc='count').reset_index()
    df2 = pd.DataFrame()
    df2['人数'] = df1['人数']
    df2['年龄'] = df1['年龄']
    df2['街道'] = df1['街道']
    df2['性别'] = df1['性别']
    df = df2
    df['年龄'] = df['年龄'].astype('int')
    df['年龄'] = datetime.datetime.now().year - df['年龄']
    df['人数1'] = df['人数'] * 1.01
    df['年龄1'] = df['年龄'] + 1
    df['人数2'] = df['人数1'] * 1.01
    df['年龄2'] = df['年龄1'] + 1
    df['人数3'] = df['人数2'] * 1.01
    df['年龄3'] = df['年龄2'] + 1
    df['人数4'] = df['人数3'] * 1.01
    df['年龄4'] = df['年龄3'] + 1
    df['人数5'] = df['人数4'] * 1.01
    df['年龄5'] = df['年龄4'] + 1
    df['人数1'] = df['人数1'].apply(lambda x: round(x, 0))
    df['人数1'] = df['人数1'].apply(lambda x: int(x))
    df['人数2'] = df['人数2'].apply(lambda x: round(x, 0))
    df['人数2'] = df['人数2'].apply(lambda x: int(x))
    df['人数3'] = df['人数3'].apply(lambda x: round(x, 0))
    df['人数3'] = df['人数3'].apply(lambda x: int(x))
    df['人数4'] = df['人数4'].apply(lambda x: round(x, 0))
    df['人数4'] = df['人数4'].apply(lambda x: int(x))
    df['人数5'] = df['人数5'].apply(lambda x: round(x, 0))
    df['人数5'] = df['人数5'].apply(lambda x: int(x))
    df.drop(columns='性别', axis=1, inplace=True)
    df1 = df.groupby(['街道'])
    list1 = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']

    dfb = dfa.groupby(['service_name'])
    dfc = dfb.get_group('老年人助餐')
    dfc = dfc[(dfc['datatime'] > (2019 * 100)) & (dfc['datatime'] < (2019 * 100 + 13))]
    dfd = dfc.groupby(['jzdjdhz'])
    df33 = pd.DataFrame()
    df44 = pd.DataFrame()
    for j in range(len(list1)):
        dfe = dfd.get_group(list1[j])
        list22 = [[list1[j], dfe.reset_index().count().iloc[0]]]
        df33 = pd.DataFrame(list22)
        df44 = df44.append(df33)

    df55 = pd.DataFrame()
    df66 = pd.DataFrame()
    for j in range(len(list1)):
        df2 = df1.get_group(list1[j])

        c1 = 0
        for i in df2.index:
            if df.iloc[i, 1] >= 65:
                c1 = c1 + df.iloc[i, 0]

        c2 = 0
        for i in df2.index:
            if df.iloc[i, 4] >= 65:
                c2 = c2 + df.iloc[i, 3]

        c3 = 0
        for i in df2.index:
            if df.iloc[i, 6] >= 65:
                c3 = c3 + df.iloc[i, 5]

        c4 = 0
        for i in df2.index:
            if df.iloc[i, 8] >= 65:
                c4 = c4 + df.iloc[i, 7]

        c5 = 0
        for i in df2.index:
            if df.iloc[i, 10] >= 65:
                c5 = c5 + df.iloc[i, 9]

        c6 = 0
        for i in df2.index:
            if df.iloc[i, 12] >= 65:
                c6 = c6 + df.iloc[i, 11]

        list33 = [[list1[j], c1, c2, c3, c4, c5, c6]]
        df55 = pd.DataFrame(list33)
        df66 = df66.append(df55)

    df66 = pd.merge(df66, df44, on=[0], how='inner')
    df66['1ST'] = (round(df66[2] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['2ND'] = (round(df66[3] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['3RD'] = (round(df66[4] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['4TH'] = (round(df66[5] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['5TH'] = (round(df66[6] / (df66['1_x'] / df66['1_y']), 0)).astype('int')

    df66.drop(axis=1, columns=['1_x', 2, 3, 4, 5, 6], inplace=True)
    df66.columns = ['JD', 'QN', '1ST', '2ND', '3RD', '4TH', '5TH']
    year_1 = str(datetime.datetime.now().year)
    year_2 = str(datetime.datetime.now().year + 1)
    year_3 = str(datetime.datetime.now().year + 2)
    year_4 = str(datetime.datetime.now().year + 3)
    year_5 = str(datetime.datetime.now().year + 4)
    list_zhucan_tr = [[df66['1ST'].sum(), df66['2ND'].sum(), df66['3RD'].sum(), df66['4TH'].sum(), df66['5TH'].sum()]]
    df_zhucan_tr = pd.DataFrame(list_zhucan_tr)
    df_zhucan_tr.columns=[year_1,year_2,year_3,year_4,year_5]
    df_zhucan_tr1 = df_zhucan_tr.T
    df_zhucan_tr1.reset_index(inplace=True)
    df_zhucan_tr1.columns = ['year_', 'num']

    return  df_zhucan_tr1

def zhu_can_degree(df,dfa):

    df.columns = ['人数', '身份证', '年龄', '街道', '性别']
    df.dropna(axis=0, how='any', inplace=True)
    df.drop_duplicates(subset=['身份证'], keep='first', inplace=True)
    df.drop('身份证', inplace=True, axis=1)
    df.reset_index(drop=True, inplace=True)
    df['t'] = df['年龄'].str.isdigit()
    df = df[df['t'] == True]
    df.reset_index(drop=True, inplace=True)
    df = df.drop('t',axis = 1)
    df1 = df.pivot_table(index=['街道', '性别', '年龄'], values='人数', aggfunc='count').reset_index()
    df2 = pd.DataFrame()
    df2['人数'] = df1['人数']
    df2['年龄'] = df1['年龄']
    df2['街道'] = df1['街道']
    df2['性别'] = df1['性别']
    df = df2
    df['年龄'] = df['年龄'].astype('int')
    df['年龄'] = datetime.datetime.now().year - df['年龄']
    df['人数1'] = df['人数'] * 1.01
    df['年龄1'] = df['年龄'] + 1
    df['人数2'] = df['人数1'] * 1.01
    df['年龄2'] = df['年龄1'] + 1
    df['人数3'] = df['人数2'] * 1.01
    df['年龄3'] = df['年龄2'] + 1
    df['人数4'] = df['人数3'] * 1.01
    df['年龄4'] = df['年龄3'] + 1
    df['人数5'] = df['人数4'] * 1.01
    df['年龄5'] = df['年龄4'] + 1
    df['人数1'] = df['人数1'].apply(lambda x: round(x, 0))
    df['人数1'] = df['人数1'].apply(lambda x: int(x))
    df['人数2'] = df['人数2'].apply(lambda x: round(x, 0))
    df['人数2'] = df['人数2'].apply(lambda x: int(x))
    df['人数3'] = df['人数3'].apply(lambda x: round(x, 0))
    df['人数3'] = df['人数3'].apply(lambda x: int(x))
    df['人数4'] = df['人数4'].apply(lambda x: round(x, 0))
    df['人数4'] = df['人数4'].apply(lambda x: int(x))
    df['人数5'] = df['人数5'].apply(lambda x: round(x, 0))
    df['人数5'] = df['人数5'].apply(lambda x: int(x))
    df.drop(columns='性别', axis=1, inplace=True)
    df1 = df.groupby(['街道'])
    list1 = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']

    dfb = dfa.groupby(['service_name'])
    dfc = dfb.get_group('老年人助餐')
    dfc = dfc[(dfc['datatime'] > (2019 * 100)) & (dfc['datatime'] < (2019 * 100 + 13))]
    dfd = dfc.groupby(['jzdjdhz'])
    df33 = pd.DataFrame()
    df44 = pd.DataFrame()
    for j in range(len(list1)):
        dfe = dfd.get_group(list1[j])
        list22 = [[list1[j], dfe.reset_index().count().iloc[0]]]
        df33 = pd.DataFrame(list22)
        df44 = df44.append(df33)

    df55 = pd.DataFrame()
    df66 = pd.DataFrame()
    for j in range(len(list1)):
        df2 = df1.get_group(list1[j])

        c1 = 0
        for i in df2.index:
            if df.iloc[i, 1] >= 65:
                c1 = c1 + df.iloc[i, 0]

        c2 = 0
        for i in df2.index:
            if df.iloc[i, 4] >= 65:
                c2 = c2 + df.iloc[i, 3]

        c3 = 0
        for i in df2.index:
            if df.iloc[i, 6] >= 65:
                c3 = c3 + df.iloc[i, 5]

        c4 = 0
        for i in df2.index:
            if df.iloc[i, 8] >= 65:
                c4 = c4 + df.iloc[i, 7]

        c5 = 0
        for i in df2.index:
            if df.iloc[i, 10] >= 65:
                c5 = c5 + df.iloc[i, 9]

        c6 = 0
        for i in df2.index:
            if df.iloc[i, 12] >= 65:
                c6 = c6 + df.iloc[i, 11]

        list33 = [[list1[j], c1, c2, c3, c4, c5, c6]]
        df55 = pd.DataFrame(list33)
        df66 = df66.append(df55)

    df66 = pd.merge(df66, df44, on=[0], how='inner')
    df66['1ST'] = (round(df66[2] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['2ND'] = (round(df66[3] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['3RD'] = (round(df66[4] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['4TH'] = (round(df66[5] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['5TH'] = (round(df66[6] / (df66['1_x'] / df66['1_y']), 0)).astype('int')

    df66.drop(axis=1, columns=['1_x', 2, 3, 4, 5, 6], inplace=True)
    df66.columns = ['JD', 'QN', '1ST', '2ND', '3RD', '4TH', '5TH']
    list_degree = ['QN', '1ST', '2ND', '3RD', '4TH', '5TH']

    for i in range(len(list_degree)):
        df66.loc[
            ((df66[list_degree[i]] > 0) & (df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.1)), list_degree[
                i]] = 1
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.1) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.2)), list_degree[i]] = 2
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.2) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.3)), list_degree[i]] = 3
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.3) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.4)), list_degree[i]] = 4
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.4) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.5)), list_degree[i]] = 5
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.5) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.6)), list_degree[i]] = 6
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.6) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.7)), list_degree[i]] = 7
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.7) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.8)), list_degree[i]] = 8
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.8) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 0.9)), list_degree[i]] = 9
        df66.loc[((df66[list_degree[i]] > (df66[list_degree[i]].max()) * 0.9) & (
                    df66[list_degree[i]] <= (df66[list_degree[i]].max()) * 1)), list_degree[i]] = 10

    year_1 = str(datetime.datetime.now().year)
    year_2 = str(datetime.datetime.now().year + 1)
    year_3 = str(datetime.datetime.now().year + 2)
    year_4 = str(datetime.datetime.now().year + 3)
    year_5 = str(datetime.datetime.now().year + 4)
    df66.columns=['JD','QN',year_1,year_2,year_3,year_4,year_5]
    list_f = []
    for i in range(10):
        for j in range(5):
            list_f.append([df66.iloc[i, 0], df66.columns[j + 2], df66.iloc[i, j + 2]])
    df77 = pd.DataFrame(list_f)
    df77.columns = ['jiedao', 'year_', 'num']

    return  df77

def zhu_can_top5(df,dfa):

    df.columns = ['人数', '身份证', '年龄', '街道', '性别']
    df.dropna(axis=0, how='any', inplace=True)
    df.drop_duplicates(subset=['身份证'], keep='first', inplace=True)
    df.drop('身份证', inplace=True, axis=1)
    df.reset_index(drop=True, inplace=True)
    df['t'] = df['年龄'].str.isdigit()
    df = df[df['t'] == True]
    df.reset_index(drop=True, inplace=True)
    df = df.drop('t',axis = 1)
    df1 = df.pivot_table(index=['街道', '性别', '年龄'], values='人数', aggfunc='count').reset_index()
    df2 = pd.DataFrame()
    df2['人数'] = df1['人数']
    df2['年龄'] = df1['年龄']
    df2['街道'] = df1['街道']
    df2['性别'] = df1['性别']
    df = df2
    df['年龄'] = df['年龄'].astype('int')
    df['年龄'] = datetime.datetime.now().year - df['年龄']
    df['人数1'] = df['人数'] * 1.01
    df['年龄1'] = df['年龄'] + 1
    df['人数2'] = df['人数1'] * 1.01
    df['年龄2'] = df['年龄1'] + 1
    df['人数3'] = df['人数2'] * 1.01
    df['年龄3'] = df['年龄2'] + 1
    df['人数4'] = df['人数3'] * 1.01
    df['年龄4'] = df['年龄3'] + 1
    df['人数5'] = df['人数4'] * 1.01
    df['年龄5'] = df['年龄4'] + 1
    df['人数1'] = df['人数1'].apply(lambda x: round(x, 0))
    df['人数1'] = df['人数1'].apply(lambda x: int(x))
    df['人数2'] = df['人数2'].apply(lambda x: round(x, 0))
    df['人数2'] = df['人数2'].apply(lambda x: int(x))
    df['人数3'] = df['人数3'].apply(lambda x: round(x, 0))
    df['人数3'] = df['人数3'].apply(lambda x: int(x))
    df['人数4'] = df['人数4'].apply(lambda x: round(x, 0))
    df['人数4'] = df['人数4'].apply(lambda x: int(x))
    df['人数5'] = df['人数5'].apply(lambda x: round(x, 0))
    df['人数5'] = df['人数5'].apply(lambda x: int(x))
    df.drop(columns='性别', axis=1, inplace=True)
    df1 = df.groupby(['街道'])
    list1 = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道', '豫园街道']

    dfb = dfa.groupby(['service_name'])
    dfc = dfb.get_group('老年人助餐')
    dfc = dfc[(dfc['datatime'] > (2019 * 100)) & (dfc['datatime'] < (2019 * 100 + 13))]
    dfd = dfc.groupby(['jzdjdhz'])
    df33 = pd.DataFrame()
    df44 = pd.DataFrame()
    for j in range(len(list1)):
        dfe = dfd.get_group(list1[j])
        list22 = [[list1[j], dfe.reset_index().count().iloc[0]]]
        df33 = pd.DataFrame(list22)
        df44 = df44.append(df33)

    df55 = pd.DataFrame()
    df66 = pd.DataFrame()
    for j in range(len(list1)):
        df2 = df1.get_group(list1[j])

        c1 = 0
        for i in df2.index:
            if df.iloc[i, 1] >= 65:
                c1 = c1 + df.iloc[i, 0]

        c2 = 0
        for i in df2.index:
            if df.iloc[i, 4] >= 65:
                c2 = c2 + df.iloc[i, 3]

        c3 = 0
        for i in df2.index:
            if df.iloc[i, 6] >= 65:
                c3 = c3 + df.iloc[i, 5]

        c4 = 0
        for i in df2.index:
            if df.iloc[i, 8] >= 65:
                c4 = c4 + df.iloc[i, 7]

        c5 = 0
        for i in df2.index:
            if df.iloc[i, 10] >= 65:
                c5 = c5 + df.iloc[i, 9]

        c6 = 0
        for i in df2.index:
            if df.iloc[i, 12] >= 65:
                c6 = c6 + df.iloc[i, 11]

        list33 = [[list1[j], c1, c2, c3, c4, c5, c6]]
        df55 = pd.DataFrame(list33)
        df66 = df66.append(df55)

    df66 = pd.merge(df66, df44, on=[0], how='inner')
    df66['1ST'] = (round(df66[2] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['2ND'] = (round(df66[3] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['3RD'] = (round(df66[4] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['4TH'] = (round(df66[5] / (df66['1_x'] / df66['1_y']), 0)).astype('int')
    df66['5TH'] = (round(df66[6] / (df66['1_x'] / df66['1_y']), 0)).astype('int')

    df66.drop(axis=1, columns=['1_x', 2, 3, 4, 5, 6], inplace=True)
    df66.columns = ['JD', 'QN', '1ST', '2ND', '3RD', '4TH', '5TH']

    list_zhucan_top5 = [
        [df66.T[0].iloc[2:].sum(), df66.T[1].iloc[2:].sum(), df66.T[2].iloc[2:].sum(), df66.T[3].iloc[2:].sum(),
         df66.T[4].iloc[2:].sum(), df66.T[5].iloc[2:].sum(), df66.T[6].iloc[2:].sum(), df66.T[7].iloc[2:].sum(),
         df66.T[8].iloc[2:].sum(), df66.T[9].iloc[2:].sum()]]
    df_zhucan_top5 = pd.DataFrame(list_zhucan_top5)
    df_zhucan_top5.columns = ['五里桥街道', '半淞园路街道', '南京东路街道', '外滩街道', '小东门街道', '打浦桥街道', '淮海中路街道', '瑞金二路街道', '老西门街道',
                              '豫园街道']
    df_zhucan_top5 = pd.DataFrame(df_zhucan_top5.T.sort_values(by=0, ascending=False)[0].iloc[0:5])
    df_zhucan_top5.reset_index(inplace=True)
    df_zhucan_top5.columns = ['jd', 'num']

    return  df_zhucan_top5