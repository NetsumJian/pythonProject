# -*- coding:utf-8 -*-
"""
Description:

@author: ZhengYi Yin
@date: 2021-1-11
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
    import algorithms.old_people as ex
    logger = elog()

    url_rkjbxx = args['url_rkjbxx']  # 'jdbc:postgresql://215.0.1.20:25308/epoint_zbk'
    url_oldpeopleneedmonthnew = args['url_oldpeopleneedmonthnew']  # 'jdbc:postgresql://215.0.1.20:25308/epoint_zbk'
    url_niunai_zhucan_ku = args['url_niunai_zhucan_ku']
    username = args['username']   #'epoint'
    password = args['password']   #'Epoint@123'
    tablename_rkjbxx = args['tablename_rkjbxx']
    tablename_oldpeopleneedmonthnew = args['tablename_oldpeopleneedmonthnew']
    wtable_niunai_total = args['wtable_niunai_total']
    wtable_niunai_degree = args['wtable_niunai_degree']
    wtable_niunai_qushi = args['wtable_niunai_qushi']
    wtable_niunai_top5 = args['wtable_niunai_top5']
    wtable_zhucan_total = args['wtable_zhucan_total']
    wtable_zhucan_degree = args['wtable_zhucan_degree']
    wtable_zhucan_qushi = args['wtable_zhucan_qushi']
    wtable_zhucan_top5 = args['wtable_zhucan_top5']



    logger.info("成功读取全量数据")

    df_7 = tb.readtable1(url_rkjbxx, username, password, tablename_rkjbxx)
    df7 = ex.niu_nai_total(df_7)
    df_1 = tb.readtable1(url_rkjbxx, username, password, tablename_rkjbxx)
    df1 = ex.niu_nai_degree(df_1)
    df_2 = tb.readtable1(url_rkjbxx, username, password, tablename_rkjbxx)
    df2 = ex.niu_nai_qushi(df_2)
    df_3 = tb.readtable1(url_rkjbxx, username, password, tablename_rkjbxx)
    df3 = ex.niu_nai_top5(df_3)
    df_8 = tb.readtable1(url_rkjbxx, username, password, tablename_rkjbxx)
    dfa_8 = tb.readtable2(url_oldpeopleneedmonthnew, username, password, tablename_oldpeopleneedmonthnew)
    df8 = ex.zhu_can_total(df_8,dfa_8)
    df_4 = tb.readtable1(url_rkjbxx, username, password, tablename_rkjbxx)
    dfa_4 = tb.readtable2(url_oldpeopleneedmonthnew, username, password, tablename_oldpeopleneedmonthnew)
    df4 = ex.zhu_can_degree(df_4,dfa_4)
    df_5 = tb.readtable1(url_rkjbxx, username, password, tablename_rkjbxx)
    dfa_5 = tb.readtable2(url_oldpeopleneedmonthnew, username, password, tablename_oldpeopleneedmonthnew)
    df5 = ex.zhu_can_qushi(df_5,dfa_5)
    df_6 = tb.readtable1(url_rkjbxx, username, password, tablename_rkjbxx)
    dfa_6 = tb.readtable2(url_oldpeopleneedmonthnew, username, password, tablename_oldpeopleneedmonthnew)
    df6 = ex.zhu_can_top5(df_6,dfa_6)

    logger.info("成功提取筛选工单")

    tb.writetable_niunaidegree(url_niunai_zhucan_ku, username, password, wtable_niunai_degree, df1)
    tb.writetable_niunaiqushi(url_niunai_zhucan_ku, username, password, wtable_niunai_qushi, df2)
    tb.writetable_niunaitop5(url_niunai_zhucan_ku, username, password, wtable_niunai_top5, df3)
    tb.writetable_niunaitotal(url_niunai_zhucan_ku, username, password, wtable_niunai_total, df7)
    tb.writetable_zhucandegree(url_niunai_zhucan_ku, username, password, wtable_zhucan_degree, df4)
    tb.writetable_zhucanqushi(url_niunai_zhucan_ku, username, password, wtable_zhucan_qushi, df5)
    tb.writetable_zhucantop5(url_niunai_zhucan_ku, username, password, wtable_zhucan_top5, df6)
    tb.writetable_zhucantotal(url_niunai_zhucan_ku, username, password, wtable_zhucan_total, df8)

    logger.info("成功回写MPP库的表")

    return "OK"


def main():
    # 初始化
    init(commonUtil.load_step_param("init"))

    # 全量工单筛选

    SQLdata(commonUtil.load_step_param("SQLdata"))


if __name__ == '__main__':
    main()