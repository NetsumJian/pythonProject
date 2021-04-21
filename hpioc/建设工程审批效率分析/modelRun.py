# -*- coding:utf-8 -*-
"""
Description:

@author: Wangjunxi
@date: 2020-12-09
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
    import algorithms.dxsj1 as dx1
    import algorithms.dxsj2 as dx2
    import algorithms.extract as ex
    logger = elog()

    url = args['url']  # 'jdbc:postgresql://215.0.2.36:25308/epoint_ztk'
    url1 = args['url1']  # 'jdbc:postgresql://215.0.2.36:25308/epoint_zbk'
    username = args['username']   #'epoint'
    password = args['password']   #'Epoint@123'
    tablename = args['tablename']   #'public.jgw'
    wtable = args['wtable']  #'public.xzfw_jsgcxkzgk'
    wtable1 = args['wtable1']  # 'public.xzfw_zftzxmxq'
    df = dx1.readtable(url, username, password, tablename)
    
    logger.info("成功读取全量数据")

    df,df_xmxq = ex.data_extract(df)


    logger.info("成功提取筛选工单")

    dx1.writetable(url1, username, password, wtable, df)
    dx2.writetable(url1, username, password, wtable1, df_xmxq)
    logger.info("成功回写MPP库的"+wtable+"表")
    return "OK"


def main():
    # 初始化
    init(commonUtil.load_step_param("init"))

    # 全量工单筛选

    SQLdata(commonUtil.load_step_param("SQLdata"))


if __name__ == '__main__':
    main()