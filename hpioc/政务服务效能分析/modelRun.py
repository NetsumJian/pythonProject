# -*- coding:utf-8 -*-
"""
Description:

@author: zuoxiaoyan
@date: 20201-2-5
"""
from epointml.utils import commonUtil, elog
import os
commonUtil.setRootPath(os.path.split(os.path.realpath(__file__))[0])


def init(args):
    """
    初使化
    """
    logger = elog()
    logger.info("开始初始化")
    commonUtil.installpackage(args["whlsource"])
    logger.info("三方包下载完毕")
    return "OK"


def SQLdata(args):
    import algorithms.tzsb as tb
    import algorithms.data_stat as ds
    logger = elog()

    mysqlurl = args['mysqlurl']  # 'jdbc:mysql://192.168.219.123:3306/zxy'
    username = args['username']   #'root'
    password = args['password']   #Infra5@Gep0int'
    tablename = args['tablename']   #'auditfwzn'
    tablename1 = args['tablename1']   #'auditfwznextend'
    tablename2 = args['tablename2']  # 'auditfwznmaterial'
    wtable=args['wtable']  #'zxy.zwfw_serviceeffic'
    tb_fwzn = tb.readtable1(mysqlurl, username, password, tablename)
    tb_fwzne = tb.readtable1(mysqlurl, username, password, tablename1)
    tb_fwznm = tb.readtable1(mysqlurl, username, password, tablename2)

    logger.info("成功读取全量数据")

    zwfw_serv = ds.data_stat(tb_fwzn, tb_fwzne, tb_fwznm)


    logger.info("成功计算服务指标")
    tb.createtable(mysqlurl, username, password, wtable)
    tb.writetable(mysqlurl, username, password, wtable, zwfw_serv)
    logger.info("成功回写MYSQL库的"+wtable+"表")
    return "OK"


def main():
    # 初始化
    init(commonUtil.load_step_param("init"))

    # 全量工单筛选

    SQLdata(commonUtil.load_step_param("SQLdata"))


if __name__ == '__main__':
    main()