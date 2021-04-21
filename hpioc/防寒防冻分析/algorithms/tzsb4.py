import pandas as pd
import numpy as np
import os
from epointml.utils import DbPoolUtil


#  包命名：com.epoint.fxyj.tzsb

def readtable(mysqlurl, username, password, tablename):
    """
    读取数据库中的表
    :param mysqlurl:
    :param username:
    :param password:
    :param tablename: str, 数据库中表名
    :return: Data
    
    
    
    rame，读取的数据库表
    """

    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    db = DbPoolUtil(url=mysqlurl, username=username, password=password)

    # 读取表中数据 
    sql = 'SELECT * FROM ' + tablename + " where  extract(month from discovertime) in (1,2,3,12) and (discovertime < '2020-01-01 00:00:00') or (discovertime > '2020-01-01 00:00:00' and infotypename like '%%热线%%')"
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
    
    
def readtable_wg(mysqlurl, username, password, tablename):
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
    sql = 'SELECT * FROM ' + tablename + ' where  extract(month from "openTS"::timestamp) in (1,2,3,12) and "openTS" ' + " >= '2020-01-01 00:00:00'  "
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
          '(taskid varchar(250),description varchar(2555),discovertime varchar(255),infozcname varchar(250),' + \
          'atname varchar(255),streetname varchar(255),communityname varchar(250),infotypename varchar(255),address  varchar(255),' + \
          ' x varchar(2555),y varchar(2555))'
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

    # 删表
    sql = 'drop table if exists ' + tablename
    db.execute_iud(sql)

    # # 建表
    sql = 'create table if not exists ' + tablename + \
          '(taskid varchar(250),description varchar(2555),discovertime timestamp,theme varchar(250),' + \
          'subtheme varchar(255),streetname varchar(255),communityname varchar(250),infotypename varchar(255),address  varchar(255),' + \
            ' x varchar(2555),y varchar(2555))'
    db.execute(sql)

    # 插表
    narray = np.array(dfr)
    lst = narray.tolist()


    sql = 'insert into ' + tablename + '(taskid,description,discovertime,theme,subtheme,streetname, ' + \
    ' communityname,infotypename,address,x,y)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    db.execute_many_iud(sql, lst)



if __name__ == '__main__':
    df = readtable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_df')


