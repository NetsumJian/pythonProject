import pandas as pd
import numpy as np
from epointml.utils import DbPoolUtil
def data_extract(url,tablename):
    db = DbPoolUtil(url=url, username='epoint', password='Epoint@123')
    slst = 'public.mv_taskinfo3'.split(".")
    tschema = slst[0]
    tname = slst[1]
    sql = 'select column_name from information_schema.columns ' \
      "where table_schema='" + tschema + "' and " + \
      "table_name='" + tname + "' ORDER BY ordinal_position"
    result = db.execute_query(sql)
    cname = [list(x)[0] for x in result]
    cname = [s.lower() for s in cname]
    
    #'jdbc:postgresql://215.0.1.20:25308/epoint_ztk'
    df_total_社区管理 = pd.DataFrame()
    list_社区管理 = ['维修添置', '业委会', '纠纷协调', '楼道堆物']
    list_社区管理_sql_热线 = [
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where ((EXECUTEDEPTNAME like '%%永业%%' or  EXECUTEDEPTNAME  like '%%南房%%' or  EXECUTEDEPTNAME  like '%%金外滩%%') or (  EXECUTEDEPTNAME   like '%%街道%%' and  EXECUTEDEPTNAME  not like '%%卫%%' and  EXECUTEDEPTNAME  not like '%%中队%%' and  EXECUTEDEPTNAME  not like '%%市场%%' and  EXECUTEDEPTNAME  not like '%%处理%%'))  and (INFOtypeNAME like '%%热线%%') and (DESCRIPTION like '%%漏水%%' or DESCRIPTION like '%%装修%%' or (DESCRIPTION like '%%装修%%' and (DESCRIPTION like '%%雨棚%%' or DESCRIPTION like '%%脚手架%%' or DESCRIPTION like '%%空调%%')) or DESCRIPTION like '%%厨房%%' or (DESCRIPTION like '%%施工队%%' and DESCRIPTION not like '%%噪音%%' and DESCRIPTION not like '%%扬尘%%') or DESCRIPTION like '%%屋顶%%' or (DESCRIPTION like '%%卫生间%%' and DESCRIPTION not like '%%群租%%') or DESCRIPTION like '%%水管%%' or (DESCRIPTION like '%%施工方%%' and DESCRIPTION not like '%%噪音%%' and DESCRIPTION not like '%%扬尘%%')  or DESCRIPTION like '%%下水道%%' or (DESCRIPTION like '%%老房子%%' and DESCRIPTION not like '%%群租%%') or (DESCRIPTION like '%%空调%%'  and DESCRIPTION not like '%%噪音%%' and DESCRIPTION not like '%%噪声%%' and DESCRIPTION not like '%%声音%%') or DESCRIPTION like '%%脚手架%%' or DESCRIPTION like '%%马桶%%' or DESCRIPTION like '%%工程%%' or DESCRIPTION like '%%疏通%%' or DESCRIPTION like '%%外墙%%' or DESCRIPTION like '%%积水%%' or DESCRIPTION like '%%堵塞%%' or DESCRIPTION like '%%通行%%' or DESCRIPTION like '%%车位%%' or DESCRIPTION like '%%污水%%' or DESCRIPTION like '%%雨棚%%' or (DESCRIPTION like '%%垃圾桶%%' and (DESCRIPTION not like '声音'  or DESCRIPTION not like '噪音') ) or (DESCRIPTION like '%%私房%%' and DESCRIPTION not like '动迁') or DESCRIPTION like '%%水表%%' or DESCRIPTION like '%%阳台%%' or DESCRIPTION like '%%粉刷%%'); ",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where ( INFOTYPENAME  = '12345热线' or  INFOTYPENAME  = '市民热线') and ( EXECUTEDEPTNAME  = '南京东路街道' or  EXECUTEDEPTNAME  = '淮海中路街道'  or  EXECUTEDEPTNAME  = '小东门街道' or  EXECUTEDEPTNAME  = '豫园街道' or  EXECUTEDEPTNAME  = '五里桥街道'  or  EXECUTEDEPTNAME  = '打浦桥街道' or  EXECUTEDEPTNAME  = '外滩街道' or  EXECUTEDEPTNAME  = '瑞金二路街道' or  EXECUTEDEPTNAME  = '老西门街道' or  EXECUTEDEPTNAME  = '半淞园街道') and ( DESCRIPTION  like '%%业委会%%');",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from (select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y  from public.mv_taskinfo3  where  INFOTYPENAME  like '%%热线%%'  and  EXECUTEDEPTNAME  like '%%街道%%' and  EXECUTEDEPTNAME  not like '%%卫%%' and  EXECUTEDEPTNAME  not like '%%中队%%' and  EXECUTEDEPTNAME  not like '%%市场%%' and  EXECUTEDEPTNAME  not like '%%处理%%') a where  DESCRIPTION  like '%%纠纷%%' or  DESCRIPTION  like '%%协调%%';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3  where  (description  like '%%楼道%%'  or description  like '%%消防通道%%' or description  like '%%堆物%%' or description  like '%%占用%%公共%%' or description  like '%%占用%%楼道%%') and(description not like '%%道路%%') and (infotypename ='12345热线' and executedeptname  like '%%街道%%' and executedeptname not like '%%卫%%' and executedeptname not like '%%中队%%' and executedeptname not like '%%市场%%' and executedeptname not like '%%处理%%');"]

    # list_社区管理_sql_网格=[[],[],[],[]]
    for i in range(4):
        result_热线 = db.execute_query(list_社区管理_sql_热线[i])
        
        df_热线 = [list(x) for x in result_热线]
        
        df_热线 = pd.DataFrame(df_热线)
 
        df_热线.columns = ['taskid', 'description', 'discovertime', 'theme', 'subtheme', 'streetname', 'communityname',
                         'infotypename', 'address', 'x', 'y']
        
        df = df_热线
        df['subtheme'] = list_社区管理[i]

        df.drop_duplicates(subset='taskid',inplace=True)
        df_total_社区管理 = pd.concat([df, df_total_社区管理], axis=0)
    df_total_社区管理['theme'] = '社区管理'

    df_total_环卫市容 = pd.DataFrame()
    list_环卫市容 = ['暴露垃圾', '道路保洁', '乱张贴、乱涂写', '乱晾晒']
    list_环卫市容_sql_热线 = [
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (description like '%%生活垃圾%%' or description like '%%乱扔%%' or description like '%%无人清理%%' or description like '%%乱丢%%'  or description like '%%临时垃圾%%'  or description like '%%尽快清理%%'  or description like '%%脏%%'  or description like '%%乱倒%%'  or description like '%%建筑垃圾%%') and INFOTYPENAME like '%%热线%%';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y FROM public.mv_taskinfo3 where (DESCRIPTION like '%%道路%%尘%%' or DESCRIPTION like '%%路面%%尘%%' or DESCRIPTION like '%%道路%%扫%%' or (DESCRIPTION like '%%吐痰%%' and DESCRIPTION not like '%%租%%') or (DESCRIPTION like '%%垃圾箱%%' and DESCRIPTION not like '%%小区%%') or (DESCRIPTION like '%%垃圾桶%%' and DESCRIPTION not like '%%小区%%')) and INFOTYPENAME like '%%热线%%';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (description like '%%乱张贴%%' or description like '%%小广告%%' or description like '%%乱涂写%%' or description like '%%乱涂%%'  or description like '%%乱写%%'  or description like '%%乱画%%'  or description like '%%脏%%'  ) and INFOTYPENAME like '%%热线%%';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (description like '%%乱晾晒%%'  ) and INFOTYPENAME like '%%热线%%';"]
    
    环卫市容_sql_网格1='''select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg   where (level_2 like '%%暴露垃圾%%'  )   and  "openTS" >=  '2020-01-01 00:00:00'  ;'''
    环卫市容_sql_网格2='''select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg   where (level_2 like '%%道路保洁%%'  )   and  "openTS" >=  '2020-01-01 00:00:00'  ;'''
    环卫市容_sql_网格3='''select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg   where (level_2 like '%%乱涂写、乱张贴、乱刻画%%'  )   and  "openTS" >=  '2020-01-01 00:00:00'  ;'''
    环卫市容_sql_网格4='''select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg   where (level_2 like '%%乱晾晒%%'  )   and  "openTS" >=  '2020-01-01 00:00:00'  ;'''

    
    list_环卫市容_sql_网格 = [
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%暴露垃圾%%'  ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件') and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%道路保洁%%'  ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件') and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%乱涂写、乱张贴、乱刻画%%'  ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件') and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%乱晾晒%%'  ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件') and discovertime < '2020-01-01 00:00:00';"]
    list_环卫市容_sql_网格_ = [环卫市容_sql_网格1,环卫市容_sql_网格2,环卫市容_sql_网格3,环卫市容_sql_网格4]
    for i in range(4):
        result_热线 = db.execute_query(list_环卫市容_sql_热线[i])
        df_热线 = [list(x) for x in result_热线]
        df_热线 = pd.DataFrame(df_热线)
        
        result_网格 = db.execute_query(list_环卫市容_sql_网格[i])
        df_网格 = [list(x) for x in result_网格]
        df_网格 = pd.DataFrame(df_网格)
        
        result_网格_ = db.execute_query(list_环卫市容_sql_网格_[i])
        df_网格_ = [list(x) for x in result_网格_]
        df_网格_ = pd.DataFrame(df_网格_)
        
        df_网格=df_网格.append(df_网格_)
        

        df_热线.columns = ['taskid', 'description', 'discovertime', 'theme', 'subtheme', 'streetname', 'communityname',
                         'infotypename', 'address', 'x', 'y']
        df_网格.columns = ['taskid', 'description', 'discovertime', 'theme', 'subtheme', 'streetname', 'communityname',
                         'infotypename', 'address', 'x', 'y']
        df = pd.concat([df_网格, df_热线], axis=0)
        df['subtheme'] = list_环卫市容[i]

        df.drop_duplicates(subset='taskid',inplace=True)
        df_total_环卫市容 = pd.concat([df, df_total_环卫市容], axis=0)
    df_total_环卫市容['theme'] = '环卫市容'

    df_total_街面秩序 = pd.DataFrame()
    list_街面秩序 = ['占道无照经营', '擅自占用道路堆物', '机动车乱停放、非机动车乱停放', '流浪乞讨']
    list_街面秩序_sql_热线 = [
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (description like '%%乱设摊%%' or description like '%%无证设摊%%' or description like '%%摆摊%%' or description like '%%摊贩占道%%'  or description like '%%流动摊%%'  or description like '%%摊点%%' ) and INFOTYPENAME like '%%热线%%';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (description like '%%占道堆物%%' or description like '%%快递堆物%%') and INFOTYPENAME like '%%热线%%';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (description like '%%共享单车%%' or description like '%%非机动车%%' or description like '%%自行车%%') and INFOTYPENAME like '%%热线%%';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where ( DESCRIPTION  like '%%强讨%%' or  DESCRIPTION  like '%%卖唱%%' or  DESCRIPTION  like '%%卖艺%%' or  DESCRIPTION  like '%%流落%%' or   DESCRIPTION  like '%%露宿%%' or ( DESCRIPTION  like '%%流浪%%' and  DESCRIPTION  not like '%%猫%%' and  DESCRIPTION  not like '%%狗%%' and  DESCRIPTION  not like '%%动物%%')) and  INFOTYPENAME  like '%%热线%%' ;"]


    街面秩序_sql_网格1='select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg  ' + "   where (level_2 like '%%占道无证照经营%%'  ) " + '  and  "openTS" >= '  + " '2020-01-01 00:00:00'  ;"
    街面秩序_sql_网格2='select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg  ' + "   where (level_2 like '%%擅自占用道路堆物、施工%%'  ) " + '  and  "openTS" >= '  + " '2020-01-01 00:00:00'  ;"
    街面秩序_sql_网格3='select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg  ' + "   where (level_2 like '%%机动车乱停放、非机动车乱停放%%' and description like '%%共享单车%%' or description like '%%非机动车%%' or description like '%%自行车%%' ) " + '  and  "openTS" >= '  + " '2020-01-01 00:00:00'  ;"
    街面秩序_sql_网格4='select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg  ' + "   where (level_2 like '%%流浪乞讨%%'  ) " + '  and  "openTS" >= '  + " '2020-01-01 00:00:00'  ;"

    list_街面秩序_sql_网格_ = [街面秩序_sql_网格1,街面秩序_sql_网格2,街面秩序_sql_网格3,街面秩序_sql_网格4]


    list_街面秩序_sql_网格 = [
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%占道无证照经营%%'  ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件') and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%擅自占用道路堆物、施工%%'  ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件') and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%机动车乱停放、非机动车乱停放%%' and description like '%%共享单车%%' or description like '%%非机动车%%' or description like '%%自行车%%' ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件') and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%流浪乞讨%%'  ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件') and discovertime < '2020-01-01 00:00:00';"]

    for i in range(4):
        result_热线 = db.execute_query(list_街面秩序_sql_热线[i])
        df_热线 = [list(x) for x in result_热线]
        df_热线 = pd.DataFrame(df_热线)   #  mv_taskinfo3热线数据
        
        result_网格 = db.execute_query(list_街面秩序_sql_网格[i])
        df_网格 = [list(x) for x in result_网格]
        df_网格 = pd.DataFrame(df_网格)  #  mv_taskinfo3网格数据
        
        result_网格_ = db.execute_query(list_街面秩序_sql_网格_[i])
        df_网格_ = [list(x) for x in result_网格_]
        df_网格_ = pd.DataFrame(df_网格_) #  mv_taskinfo_wg网格数据
        
        df_网格=df_网格.append(df_网格_)
        
        df = pd.concat([df_网格, df_热线], axis=0)
 
        df.columns = ['taskid', 'description', 'discovertime', 'theme', 'subtheme', 'streetname', 'communityname','infotypename', 'address', 'x', 'y']
        # df_网格.columns=['taskid','description','discovertime','theme','subtheme','streetname','communityname','infotypename','address','x','y']
        df['subtheme'] = list_街面秩序[i]

        df.drop_duplicates(subset='taskid',inplace=True)
        df_total_街面秩序 = pd.concat([df, df_total_街面秩序], axis=0)
    df_total_街面秩序['theme'] = '街面秩序'

    df_total_设施损坏 = pd.DataFrame()
    list_设施损坏 = ['户外公益广告损坏', '道路破损', '各类井盖', '立杆']
    list_设施损坏_sql_热线 = [
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (( EXECUTEDEPTNAME  = '区文明办' or  SUBEXECUTEDEPTNAME  = '区文明办') and  INFOSCNAME  = '乱设或损坏户外设施') or (description like '%%公益%%广告%%' and INFOTYPENAME like '%%热线%%');",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where ( INFOTYPENAME  like '%%热线%%') and ((DESCRIPTION like '%%突起%%' and  DESCRIPTION  not like '%%小便%%' and DESCRIPTION not like '%%墙砖%%' ) or  DESCRIPTION  like '%%盲道%%缺失%%' or  DESCRIPTION  like '%%缺失%%盲道%%' or  DESCRIPTION  like '%%盲道%%碎裂%%' or  DESCRIPTION  like '%%路面破损%%' or  DESCRIPTION  like '%%道路破损%%' or  DESCRIPTION  like '%%路面损坏%%' or  DESCRIPTION  like '%%道路损坏%%');",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (description like '%%井盖%%' ) and INFOTYPENAME like '%%热线%%';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3  where (  DESCRIPTION   like '%%杆损坏%%' or  DESCRIPTION   like '%%杆%%歪%%' or  DESCRIPTION   like '%%杆%%斜%%') and ( DESCRIPTION   not like '%%车%%' and  DESCRIPTION   not like '%%红白%%' and  DESCRIPTION   not like '%%美%%' and  DESCRIPTION   not like '%%斜坡%%') and  INFOTYPENAME  like '%%热线%%' ;"]
    
    设施损坏_sql_网格1='select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg  ' + "   where (level_2  = '乱设或损坏户外设施') or (description like '%%公益%%广告%%' ) " + '  and  "openTS" >= '  + " '2020-01-01 00:00:00'  ;"
    设施损坏_sql_网格2='select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg  ' + "   where (level_2 like '%%道路破损%%'  )  " + '  and  "openTS" >= '  + " '2020-01-01 00:00:00'  ;"
    设施损坏_sql_网格3='select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg  ' + "   where (level_2 like '%%井盖%%'  ) and (description like '%%损%%' or description like '%%翘%%' or description like '%%缺%%' or description like '%%突%%' or description like '%%裂%%' or description like '%%陷%%') " + '  and  "openTS" >= '  + " '2020-01-01 00:00:00'  ;"
    设施损坏_sql_网格4='select "chs_code" , "description" , "openTS" , "level_1" , "level_2" , "town_rawIdentity" , "communityName" , "infoTypeName" , "address" ,"x", "y" from mv_taskinfo_wg  ' + "   where (level_2 = '其它立杆' or   level_2 = '市政立杆' or   level_2 = '擅自架设管线、杆线设施' or   level_2 = '交通立杆'or   level_2 = '电力杆')  " + '  and  "openTS" >= '  + " '2020-01-01 00:00:00'  ;"
    
    list_设施损坏_sql_网格_ = [设施损坏_sql_网格1,设施损坏_sql_网格2,设施损坏_sql_网格3,设施损坏_sql_网格4]
    
    list_设施损坏_sql_网格 = [
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (( EXECUTEDEPTNAME  = '区文明办' or  SUBEXECUTEDEPTNAME  = '区文明办') and  INFOSCNAME  = '乱设或损坏户外设施') or (description like '%%公益%%广告%%' and INFOTYPENAME like '%%热线%%')and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%道路破损%%'  ) and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件')and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname like '%%井盖%%'  ) and (description like '%%损%%' or description like '%%翘%%' or description like '%%缺%%' or description like '%%突%%' or description like '%%裂%%' or description like '%%陷%%')and(INFOTYPENAME = '部件' or INFOTYPENAME = '事件')and discovertime < '2020-01-01 00:00:00';",
        "select taskid ,  description ,  discovertime ,  infobcname ,  infoscname , streetname ,  communityname ,  infotypename ,  address ,  x ,  y from public.mv_taskinfo3 where (infoscname = '其它立杆' or   infoscname = '市政立杆' or   infoscname = '擅自架设管线、杆线设施' or   infoscname = '交通立杆'or   infoscname = '电力杆') and (INFOTYPENAME = '部件' or INFOTYPENAME = '事件')and discovertime < '2020-01-01 00:00:00';"]

    for i in range(4):
        result_热线 = db.execute_query(list_设施损坏_sql_热线[i])
        df_热线 = [list(x) for x in result_热线]
        df_热线 = pd.DataFrame(df_热线)
        
        result_网格 = db.execute_query(list_设施损坏_sql_网格[i])
        df_网格 = [list(x) for x in result_网格]
        df_网格 = pd.DataFrame(df_网格)
        
        result_网格_ = db.execute_query(list_设施损坏_sql_网格_[i])
        df_网格_ = [list(x) for x in result_网格_]
        df_网格_ = pd.DataFrame(df_网格_)
                
        df_网格=df_网格.append(df_网格_)
 
        df_热线.columns = ['taskid', 'description', 'discovertime', 'theme', 'subtheme', 'streetname', 'communityname',
                         'infotypename', 'address', 'x', 'y']
        df_网格.columns = ['taskid', 'description', 'discovertime', 'theme', 'subtheme', 'streetname', 'communityname',
                         'infotypename', 'address', 'x', 'y']
        df = pd.concat([df_网格, df_热线], axis=0)
        df['subtheme'] = list_设施损坏[i]

        df.drop_duplicates(subset='taskid',inplace=True)
        df_total_设施损坏 = pd.concat([df, df_total_设施损坏], axis=0)
    df_total_设施损坏['theme'] = '设施损坏'

    # 设施损坏类工单提取
    df_total = pd.concat([df_total_设施损坏, df_total_街面秩序, df_total_环卫市容, df_total_社区管理], axis=0)
    df_total = df_total[df_total['x'].notna()]
    df_total = df_total[df_total['communityname'].notna()]
    df_total = df_total[df_total['streetname'].notna()]
    df_total = df_total.reindex(columns=['taskid','description','discovertime','theme','subtheme','streetname','communityname','infotypename','address','x','y'])
    df_total = df_total.reset_index().drop(['index'],axis=1)
    #整合表
    
    df_total.loc[df_total[df_total['streetname']==102].index,'streetname']='南京东路街道'

    df_total.loc[df_total[df_total['streetname']==101].index,'streetname']='五里桥街道'

    df_total.loc[df_total[df_total['streetname']==117].index,'streetname']='小东门街道'

    df_total.loc[df_total[df_total['streetname']==113].index,'streetname']='外滩街道'

    df_total.loc[df_total[df_total['streetname']==115].index,'streetname']='半淞园街道'

    df_total.loc[df_total[df_total['streetname']==118].index,'streetname']='豫园街道'

    df_total.loc[df_total[df_total['streetname']==119].index,'streetname']='老西门街道'

    df_total.loc[df_total[df_total['streetname']==120].index,'streetname']='打浦桥街道'

    df_total.loc[df_total[df_total['streetname']==121].index,'streetname']='淮海中路街道'

    df_total.loc[df_total[df_total['streetname']==122].index,'streetname']='瑞金二路街道'
    
    return df_total


    #      生成最终表