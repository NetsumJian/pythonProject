def data_extract(df,df_wg):

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
    df=df.append(df_wg)
    df.drop_duplicates(subset='taskid',inplace=True)
    df_rexian=df[df['infotypename'].astype(str)=='12345热线'].append(df[df['infotypename'].astype(str)=='市民热线'])
    
    df_wangge=df[df['infotypename'].astype(str)=='事件'].append(df[df['infotypename'].astype(str)=='部件'])
    
    df_1=df_rexian[df_rexian['atname'].map(lambda x:str(x) in ['维修添置','物业安保','排水工程'])][df_rexian[df_rexian['atname'].map(lambda x:str(x) in ['维修添置','物业安保','排水工程'])]['description'].map(lambda x: '水管' in x )]
    
    df_1_=df_rexian[df_rexian['atname'].map(lambda x:str(x)  == '水管维修')]
    df_1__=df_wangge[df_wangge['infozcname']=='自来水管破裂']
    df_sgbl=df_1.append(df_1_).append(df_1__)

    df_sgbl=df_sgbl[['taskid','description','discovertime','infozcname','atname','streetname','communityname','infotypename','address','x','y']]

    df_sgbl['infozcname']='水管爆裂'

    df_2=df_rexian[df_rexian['description'].map(lambda x:'路' in x and '结冰' in x)]

    df_lmjb=df_2[['taskid','description','discovertime','infozcname','atname','streetname','communityname','infotypename','address','x','y']]

    df_lmjb['infozcname']='路面结冰'
    
    df_3=df_rexian[df_rexian['atname'].map(lambda x:str(x) in ['流浪人员管理','流浪救助'])]
    df_3_=df_wangge[df_wangge['infozcname']=='流浪乞讨']
    df_llry=df_3.append(df_3_)
    
    df_llry=df_llry[['taskid','description','discovertime','infozcname','atname','streetname','communityname','infotypename','address','x','y']]

    df_llry['infozcname']='流浪人员'
    #df_3=df_rexian[df_rexian['description'].map(lambda x:'倒流'in x or '地势'in x or '下雨'in x or '积水'in x or '淹没'in x or'低洼'in x  )]

    #df_js=df_3[['taskid','description','discovertime','infozcname','atname','streetname','communityname','infotypename','address','x','y']]

    #df_js['infozcname']='积水'

    df_4=df_rexian[df_rexian['description'].map(lambda x:'风吹' in x or '掉落' in x or '高空' in x)]

    df_gkzw=df_4[['taskid','description','discovertime','infozcname','atname','streetname','communityname','infotypename','address','x','y']]

    df_gkzw['infozcname']='高空坠物'

    df_total=df_sgbl.append(df_lmjb).append(df_llry).append(df_gkzw)

    df_total.columns=['taskid', 'description', 'discovertime', 'theme','subtheme', 'streetname', 'communityname', 'infotypename', 'address','x', 'y']

    df_total=df_total.reset_index().drop('index',axis=1)

    return  df_total