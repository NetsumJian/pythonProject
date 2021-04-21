import pandas as pd
import numpy as np
import os
from epointml.utils import DbPoolUtil
import datetime


#  包命名：com.epoint.fxyj.tzsb

def readtable(mysqlurl, username, password, tablename):
    """
    读取数据库中的表
    :param mysqlurl:
    :param username:
    :param password:
    :param tablename: str, 数据库中表名
    :return: DataFrame，读取的数据库表
    """

    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    db = DbPoolUtil(url=mysqlurl, username=username, password=password)

    # 读取表中数据
    sql = 'SELECT * FROM ' + tablename
    result = db.execute_query(sql)
    df = [list(x) for x in result]
    df = pd.DataFrame(df)

    # 读取列名
    slst = tablename.split(".")
    tschema = slst[0]
    tname = slst[1]
    sql = 'select column_name from information_schema.columns ' \
          "where table_schema='" + tschema + "' and " + \
          "table_name='" + tname + "' ORDER BY ordinal_position"
    result = db.execute_query(sql)
    cname = [list(x)[0] for x in result]
    df.columns = cname
    return df

def createtable(mysqlurl, username, password, tablename):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    db = DbPoolUtil(url=mysqlurl, username=username, password=password)
    sql = 'create table if not exists ' + tablename + \
          '(rowguid varchar(50),fxyjid varchar(20),fxyjdomainid varchar(10),fxyjtitle varchar(50),' + \
          'fxyjlevel varchar(2),fxyjtime datetime,fxyjmodelid varchar(50),fxyjsource varchar(2),createtime datetime,' + \
          'fxyjbasicstatus varchar(2),fxyjprops text,fxyjcorpname varchar(500),fxyjobjecttype varchar(2),fxyjuscc varchar(50))'
    db.execute(sql)

def writetable(mysqlurl, username, password, tablename, dfr):
    """
    写数据库表
    :param mysqlurl:
    :param username:
    :param password:
    :param tablename: str, 数据库回写表名
    :param dfr: DataFrame，需要写入数据库的最终结果表
    :return:
    """
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    db = DbPoolUtil(url=mysqlurl, username=username, password=password)
  

    # 插表
    narray = np.array(dfr)
    lst = narray.tolist()
    try:
        # 建表
        sql = 'create table if not exists ' + tablename + \
           '(year varchar(50),xmlx varchar(50),xmxl varchar(50),kgsj varchar(50),xmsl varchar(50),pjkgsj varchar(50));'
        # year 年份，xmlx 项目类型，xmxl 项目小类，kgsj 开工时间，xmsl 项目数量 ,pjkgsj 近五年平均开工时间
        db.execute(sql)
        sql = 'insert into ' + tablename + ' (year,xmlx, xmxl,kgsj,xmsl,pjkgsj)values(%s,%s,%s,%s,%s,%s)'
        db.execute_many_iud(sql, lst)
    except:
        print('插表失败')
    else:
        # 删表
        sql = 'truncate ' + tablename
        db.execute_iud(sql)
        sql = 'insert into ' + tablename + ' (year,xmlx, xmxl,kgsj,xmsl,pjkgsj)values(%s,%s,%s,%s,%s,%s)'
        db.execute_many_iud(sql, lst)

    


if __name__ == '__main__':
    df = readtable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_df')
    df_base = readtable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_df_base')
    createtable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_wtable')
    df_base['model_id'] = '54321'





