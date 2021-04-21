import pandas as pd
import numpy as np
import os
from epointml.utils import DbPoolUtil

def readtable1(mysqlurl, username, password, tablename):
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
    sql = "select * from " + tablename
    result = db.execute_query(sql)
    df = [list(x) for x in result]
    df = pd.DataFrame(df)

    # 读取列名

    sql = 'select column_name from information_schema.columns ' \
          "where table_name='" + tablename + "' ORDER BY ordinal_position"
    result = db.execute_query(sql)
    cname = [list(x)[0] for x in result]
    df.columns = cname
    return df

def createtable(mysqlurl, username, password, tablename):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    db = DbPoolUtil(url=mysqlurl, username=username, password=password)
    sql = 'create table if not exists ' + tablename + \
          '(timereduction varchar(10),immediatedegree varchar(10),freematerial varchar(10),' + \
          'zerorunning varchar(10),serviceindex varchar(10),month varchar(10))'
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

    try:
        # 插表
        narray = np.array(dfr)
        lst = narray.tolist()
        ###dfr = dfr.T
        ###lst = dfr.apply(lambda x: tuple(x))

        sql = 'insert into ' + tablename + ' (timereduction, immediatedegree, freematerial, zerorunning, serviceindex,month) values (%s,%s,%s,%s,%s,%s)'
        db.execute_many_iud(sql, lst)

    except:
        print("插表失败")

    else:
        # 删表
        sql = 'truncate ' + tablename
        db.execute_iud(sql)

        # # 建表
        # sql = 'create table if not exists ' + tablename + \
        #       '(rowguid varchar(50),fxyjid varchar(20),fxyjdomainid varchar(10),fxyjtitle varchar(50),' + \
        #       'fxyjlevel varchar(2),fxyjtime date,fxyjmodelid varchar(50),fxyjsource varchar(2),createtime datetime,' + \
        #       'fxyjbasicstatus varchar(2),fxyjprops text,fxyjcorpname varchar(500),fxyjobjecttype varchar(2),fxyjuscc varchar(50))'
        # db.execute(sql)

        # 插表
        narray = np.array(dfr)
        lst = narray.tolist()
        ###dfr = dfr.T
        ###lst = dfr.apply(lambda x: tuple(x))

        sql = 'insert into ' + tablename + ' (timereduction, immediatedegree, freematerial, zerorunning, serviceindex,month) values (%s,%s,%s,%s,%s,%s)'
        db.execute_many_iud(sql, lst)