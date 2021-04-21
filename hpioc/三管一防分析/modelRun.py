# -*- coding:utf-8 -*-
"""
Description:

@author: Wangjunxi
@date: 2020-6-18
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
    import algorithms.tzsb2 as tb
    import algorithms.extract as ex
    logger = elog()

    url = args['url']  # 'jdbc:postgresql://215.0.2.36:25308/epoint_ztk'
    url1 = args['url1']  # 'jdbc:postgresql://215.0.2.36:25308/epoint_mx'
    username = args['username']   #'epoint'
    password = args['password']   #'Epoint@123'
    tablename = args['tablename']   #'public.mv_taskinfo3'
    tablename_wg = args['tablename_wg']   #'public.mv_taskinfo3'
    wtable=args['wtable']
    df = tb.readtable(url, username, password, tablename)
    df_wg= tb.readtable_wg(url, username, password, tablename_wg)
    logger.info("成功读取全量数据")

    df = ex.data_extract(df,df_wg)
    logger.info("成功提取筛选工单")

    tb.writetable(url1, username, password, wtable, df)
    logger.info("成功回写MPP库的"+wtable+"表")
    return "OK"


def main():
    # 初始化
    init(commonUtil.load_step_param("init"))

    # 全量工单筛选

    SQLdata(commonUtil.load_step_param("SQLdata"))


if __name__ == '__main__':
    main()