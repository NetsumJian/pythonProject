import pandas as pd
import numpy as np
import os
from epointml.utils import DbPoolUtil


#  包命名：com.epoint.fxyj.tzsb

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
    sql = "select count(*),zjhm,left(CSRQ,4),JZDJDHZ,XBHZ from " + tablename + " where ((JZDJDHZ = '五里桥街道' or JZDJDHZ = '半淞园路街道' or JZDJDHZ = '南京东路街道' or JZDJDHZ = '外滩街道' or JZDJDHZ = '小东门街道' or JZDJDHZ = '打浦桥街道' or JZDJDHZ = '淮海中路街道' or JZDJDHZ = '瑞金二路街道' or JZDJDHZ = '老西门街道' or JZDJDHZ = '豫园街道') and (hjdxzqhhz = '上海市黄浦区')) group by zjhm,left(CSRQ,4),JZDJDHZ,XBHZ order by JZDJDHZ,left(CSRQ,4)"
    result = db.execute_query(sql)
    df = [list(x) for x in result]
    df = pd.DataFrame(df)
    return df

def readtable2(mysqlurl, username, password, tablename):
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

def writetable_niunaitotal(mysqlurl, username, password, tablename, dfr):
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

        sql = 'insert into ' + tablename + ' (jiedao,year_,num) values (%s,%s,%s)'
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

        sql = 'insert into ' + tablename + ' (jiedao,year_,num) values (%s,%s,%s)'
        db.execute_many_iud(sql, lst)

def writetable_niunaidegree(mysqlurl, username, password, tablename, dfr):
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

        sql = 'insert into ' + tablename + ' (jiedao,year_,num) values (%s,%s,%s)'
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

        sql = 'insert into ' + tablename + ' (jiedao,year_,num) values (%s,%s,%s)'
        db.execute_many_iud(sql, lst)


def writetable_niunaiqushi(mysqlurl, username, password, tablename, dfr):
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

        sql = 'insert into ' + tablename + ' (year_,num) values (%s,%s)'
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

        sql = 'insert into ' + tablename + ' (year_,num) values (%s,%s)'
        db.execute_many_iud(sql, lst)

def writetable_niunaitop5(mysqlurl, username, password, tablename, dfr):
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

        sql = 'insert into ' + tablename + ' (jd,num) values (%s,%s)'
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

        sql = 'insert into ' + tablename + ' (jd,num) values (%s,%s)'
        db.execute_many_iud(sql, lst)

def writetable_zhucantotal(mysqlurl, username, password, tablename, dfr):
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

        sql = 'insert into ' + tablename + ' (jiedao,year_,num) values (%s,%s,%s)'
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

        sql = 'insert into ' + tablename + ' (jiedao,year_,num) values (%s,%s,%s)'
        db.execute_many_iud(sql, lst)

def writetable_zhucandegree(mysqlurl, username, password, tablename, dfr):
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

        sql = 'insert into ' + tablename + ' (jiedao,year_,num) values (%s,%s,%s)'
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

        sql = 'insert into ' + tablename + ' (jiedao,year_,num) values (%s,%s,%s)'
        db.execute_many_iud(sql, lst)

def writetable_zhucanqushi(mysqlurl, username, password, tablename, dfr):
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

        sql = 'insert into ' + tablename + ' (year_,num) values (%s,%s)'
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

        sql = 'insert into ' + tablename + ' (year_,num) values (%s,%s)'
        db.execute_many_iud(sql, lst)

def writetable_zhucantop5(mysqlurl, username, password, tablename, dfr):
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

        sql = 'insert into ' + tablename + ' (jd,num) values (%s,%s)'
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

        sql = 'insert into ' + tablename + ' (jd,num) values (%s,%s)'
        db.execute_many_iud(sql, lst)

if __name__ == '__main__':
    df = readtable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_df')



