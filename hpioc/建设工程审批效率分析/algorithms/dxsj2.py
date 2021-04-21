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
            '(bjbh varchar(255),xmmc varchar(255),jsdw varchar(255),ztz  varchar(255),zmj  varchar(255),pzrq  varchar(255),fzrq  varchar(255),kgsj int,xmlx varchar(255));  '       
        # bjbh 办件编号,xmmc 项目名称,jsdw 建设单位,ztz	总投资,zmj 总面积,pzrq 批准日期,FZRQ 发证日期,kgsj 开工时间,xmlx 项目类型)
        db.execute(sql)
        sql = 'insert into ' + tablename + ' (bjbh,xmmc,jsdw,ztz,zmj,pzrq,fzrq,kgsj,xmlx)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        db.execute_many_iud(sql, lst)
    except:
        print('插表失败')
    else:
        # 删表
        sql = 'truncate ' + tablename
        db.execute_iud(sql)
        sql = 'insert into ' + tablename + ' (bjbh,xmmc,jsdw,ztz,zmj,pzrq,fzrq,kgsj,xmlx)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        db.execute_many_iud(sql, lst)


if __name__ == '__main__':
    df = readtable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_df')
    df_base = readtable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_df_base')
    createtable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_wtable')
    df_base['model_id'] = '54321'

    df1 = df_base.apply(check_ans, axis=1).dropna()
    df2 = df_base.apply(exp_ans, axis=1).dropna()

    if not df1.empty:
        writetable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_wtable', df1)
    if not df2.empty:
        writetable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_wtable', df2)

    _ = Anova_model("使用单位名称", "投诉次数", df, df_base, "12345667")
    df3 = _.get_res()
    if not df3.empty:
        writetable('jdbc:mysql://192.168.186.13:3306/', 'root', 'Gepoint', 'gf_tzsb.gf_wtable', df3)


