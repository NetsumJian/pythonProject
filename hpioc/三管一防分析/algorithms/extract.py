import pandas as pd
import numpy as np
def data_extract(df,df_wg):
    df_WanggeXiaolei = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    df_WanggeRexian = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    df_Rexian = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    df.columns=['taskid','description','discovertime','infobcname','infoscname','streetname','communityname','infotypename','address','x','y'] #mv_taskinfo3的工单数据
    df_ = df
    
    df_wg.loc[df_wg[df_wg['town_rawIdentity']==102].index,'town_areaName']='南京东路街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==101].index,'town_areaName']='五里桥街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==117].index,'town_areaName']='小东门街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==113].index,'town_areaName']='外滩街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==115].index,'town_areaName']='半淞园街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==118].index,'town_areaName']='豫园街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==119].index,'town_areaName']='老西门街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==120].index,'town_areaName']='打浦桥街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==121].index,'town_areaName']='淮海中路街道'

    df_wg.loc[df_wg[df_wg['town_rawIdentity']==122].index,'town_areaName']='瑞金二路街道'
    
    
    df_wg=df_wg.loc[:,['chs_code','description','openTS','level_1','level_2','town_areaName','communityName','infoTypeName','address','x','y']]
    df_wg.columns=['taskid','description','discovertime','infobcname','infoscname','streetname','communityname','infotypename','address','x','y']
    df_=df_.append(df_wg)
    df_.dropna(inplace=True)
    df_.columns = ["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                   "infotypename", "address","x","y"]
    df_.drop_duplicates("taskid",inplace=True)   #数据列提取

    df_热线 = df_[df_["infotypename"] == "12345热线"]     # 热线工单提取
    df_网格 = df_[(df_["infotypename"] == "部件") | (df_["infotypename"] == "事件")]   #  网格工单提取

    list_subtheme = ['花架花钵', '乱设或损坏户外设施', '架空线坠落、乱设', '行道树', '道路破损', '井盖', '机动车乱停放、非机动车乱停放', '暴露垃圾', '乱涂写、乱张贴、乱刻画',
                     '乱晾晒', '占道无证照经营', '路面积水、污水冒溢、粪便冒溢', '雨水井盖', '擅自占用道路堆物、施工']    # 网格小类汇总

    list_theme = ["防台防汛", "安全隐患", "市容市貌"]

    df_网格_key = [['花架', '花钵', '损'], ['掉落', '高空', '空调支架'], [''], ['断枝'], [''],
                 ['破损', '隐患', '塌陷', '凸起', '缺失', '损', '翘起', '不平', '裂', '移', '突', '缺损', '晃', '凸', '钢筋', '复位', '没盖', '松',
                  '翻', '沉', '坏', 'huai', '丢', '未', '遗失', '凹'], ['共享单车', '非机动车', '自行车'],
                 [''], [''], [''], [''], [''], [''], ['']]      #网格关键词汇总

    df_key2 = [['风吹', '掉落'], ['架空线', '刮断', '断枝', '垂落', '电缆线', '下垂'], ['倒流', '地势', '下雨', '积水', '淹没'],['安全隐患'],
               ['共享单车', '非机动车', '自行车'], ['生活垃圾', '乱扔', '无人清理', '乱丢', '临时垃圾', '尽快清理', '脏', '乱倒', '建筑垃圾'],
               ['乱张贴', '贴', '小广告', '乱涂写', '乱涂', '乱写', '乱画', '黑广告'],
               ['乱设摊', '快递堆物', '无证设摊', '摆摊', '摊贩占道', '流动摊', '摊点', '乱晾晒', '占道堆物']]
    df_key3 = ['降噪', '唱歌', '吵闹', '睡眠', '吵醒', '高音喇叭', '分贝', '休息', '广场舞', '减噪', '噪音', '噪声', '扰民', '夜间施工', '喧哗', '声音']
    # 热线和网格关键词汇总 噪音扰民

    for i in np.arange(len(df_key3)):
        df_WanggeRexian = pd.concat([df_WanggeRexian, df_[df_["description"].map(lambda x: str(df_key3[i]) in str(x))]],axis=0, join="outer")
        df_WanggeRexian = df_WanggeRexian.drop_duplicates()
    df_WanggeRexian["subtheme"] = "噪音扰民"
    df_WanggeRexian["theme"] = "噪音扰民"
    #   网格和热线的工单提取 噪音扰民
    df_WanggeRexian_loushui = df_[df_["description"].map(lambda x: "漏水" in str(x))]
    df_WanggeRexian_loushui["subtheme"] = "漏水"
    df_WanggeRexian_loushui["theme"] = "防台防汛"
    df_WanggeRexian = pd.concat([df_WanggeRexian, df_WanggeRexian_loushui], axis=0, join="outer")
    #   网格和热线的工单提取 漏水

    df1 = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    for j in df_key2[0]:
        df_temp1 = df_热线[df_热线["description"].map(lambda x: str(j) in str(x))]
        df1 = pd.concat([df1, df_temp1], axis=0, join="outer")
        df1 = df1.drop_duplicates()

    df2 = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    for j in df_key2[1]:
        df_temp1 = df_热线[df_热线["description"].map(lambda x: str(j) in str(x))]
        df2 = pd.concat([df2, df_temp1], axis=0, join="outer")
        df2 = df2.drop_duplicates()

    df3 = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    for j in df_key2[2]:
        df_temp1 = df_热线[df_热线["description"].map(lambda x: str(j) in str(x))]
        df3 = pd.concat([df3, df_temp1], axis=0, join="outer")
        df3 = df3.drop_duplicates()

    df4 = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    for j in df_key2[3]:
        df_temp1 = df_热线[df_热线["description"].map(lambda x: str(j) in str(x))]
        df4 = pd.concat([df4, df_temp1], axis=0, join="outer")
        df4 = df4.drop_duplicates()

    df5 = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    for j in df_key2[4]:
        df_temp1 = df_热线[df_热线["description"].map(lambda x: str(j) in str(x))]
        df5 = pd.concat([df5, df_temp1], axis=0, join="outer")
        df5 = df5.drop_duplicates()

    df6 = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    for j in df_key2[5]:
        df_temp1 = df_热线[df_热线["description"].map(lambda x: str(j) in str(x))]
        df6 = pd.concat([df6, df_temp1], axis=0, join="outer")
        df6 = df6.drop_duplicates()

    df7 = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    for j in df_key2[6]:
        df_temp1 = df_热线[df_热线["description"].map(lambda x: str(j) in str(x))]
        df7 = pd.concat([df7, df_temp1], axis=0, join="outer")
        df7 = df7.drop_duplicates()

    df8 = pd.DataFrame(
        columns=["taskid", "description", "discovertime", "theme", "subtheme", "streetname", "communityname",
                 "infotypename", "address","x","y"])
    for j in df_key2[7]:
        df_temp1 = df_热线[df_热线["description"].map(lambda x: str(j) in str(x))]
        df8 = pd.concat([df8, df_temp1], axis=0, join="outer")
        df8 = df8.drop_duplicates()
    df1["theme"] = "防台防汛"
    df1["subtheme"] = "高空坠物"
    df2["theme"] = "防台防汛"
    df2["subtheme"] = "部件损毁"
    df3["theme"] = "防台防汛"
    df3["subtheme"] = "积水"
    df4["theme"] = "安全隐患"
    df4["subtheme"] = "安全隐患"
    df5["theme"] = "市容市貌"
    df5["subtheme"] = "非机动车乱停放"
    df6["theme"] = "市容市貌"
    df6["subtheme"] = "暴露垃圾"
    df7["theme"] = "市容市貌"
    df7["subtheme"] = "乱涂写、乱张贴、乱刻画"
    df8["theme"] = "市容市貌"
    df8["subtheme"] = "街面秩序"
    df_Rexian = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=0, join="outer")
    #   热线工单提取

    n = 0
    for i in zip(df_网格_key, list_subtheme):
        n += 1
        for j in np.arange(len(i[0])):
            df_temp = df_网格[df_网格["subtheme"].map(lambda x: str(i[1]) in str(x))]
            df_temp = df_temp[df_temp["description"].map(lambda x: str(i[0][j]) in str(x) and "快速" not in str(x))]
            if n < 3:
                df_temp["theme"] = "防台防汛"
                df_temp["subtheme"] = "高空坠物"
            if 3 <= n < 5:
                df_temp["theme"] = "防台防汛"
                df_temp["subtheme"] = "部件损毁"
            if 5 <= n < 7:
                df_temp["theme"] = "安全隐患"
                df_temp["subtheme"] = "安全隐患"
            if n == 7:
                df_temp["theme"] = "市容市貌"
                df_temp["subtheme"] = "非机动车乱停放"
            if n == 8:
                df_temp["theme"] = "市容市貌"
                df_temp["subtheme"] = "暴露垃圾"
            if n == 9:
                df_temp["theme"] = "市容市貌"
                df_temp["subtheme"] = "乱涂写、乱张贴、乱刻画"
            if 10 <= n < 13:
                df_temp["theme"] = "市容市貌"
                df_temp["subtheme"] = "街面秩序"
            if n >= 13:
                df_temp["theme"] = "防台防汛"
                df_temp["subtheme"] = "积水"
            df_WanggeXiaolei = pd.concat([df_temp, df_WanggeXiaolei], axis=0, join="outer")
    df_WanggeXiaolei.drop_duplicates(inplace=True)
    # 网格工单提取

    df_total = pd.concat([df_Rexian, df_WanggeRexian, df_WanggeXiaolei], axis=0, join="outer")
    #df_total = df_total.iloc[:, [7, 2, 3, 8, 6, 5, 1, 4, 0]]
    df_total = df_total.drop_duplicates(subset=['taskid','subtheme'])
    df_total.dropna(inplace=True)
    df_total=df_total.reindex(columns=['taskid','description','discovertime','theme','subtheme','streetname','communityname','infotypename','address','x','y'])
    return df_total


    #      生成最终表