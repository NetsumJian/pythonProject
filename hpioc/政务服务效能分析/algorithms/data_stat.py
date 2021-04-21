import pandas as pd
import numpy as np
from epointml.utils import DbPoolUtil
from datetime import datetime
import dateutil.relativedelta

def data_stat(tb_fwzn, tb_fwzne, tb_fwznm):

    #输出表
    zwfw_serviceeffic = pd.DataFrame(np.zeros((1,6)),columns=('timereduction', 'immediatedegree','freematerial','zerorunning','serviceindex','month'))


    #零跑动
    tb_merge_fwzne = pd.merge(tb_fwzn, tb_fwzne, how='inner', on='rowguid')
    tb_merge_fwzne = tb_merge_fwzne[(tb_merge_fwzne['ql_kind']=='01')&(tb_merge_fwzne['ql_state']=='1')]
    zwfw_serviceeffic.loc[0,'zerorunning'] = format(len(tb_merge_fwzne[tb_merge_fwzne['applyermin_count']=='0'])
                                                * 100 / len(tb_merge_fwzne), '.2f')
    #免材料
    tb_merge_fwznm = pd.merge(tb_fwzn, tb_fwznm, how='inner', left_on='rowguid', right_on='itemguid')
    tb_merge_fwznm = tb_merge_fwznm[(tb_merge_fwznm['is_history']=='0') & (tb_merge_fwznm['ql_state']=='1')
                                    & (tb_merge_fwznm['audit_state']=='40') & (tb_merge_fwznm['file_source']=='2')
                                    & (~ tb_merge_fwznm['ql_kind'].isin(['02', '03', '06']))]
    zwfw_serviceeffic.loc[0, 'freematerial'] = \
        format(len(tb_merge_fwznm[(tb_merge_fwznm['exemption_form'].isin(['1','2','3','4'])) & (tb_merge_fwznm['isconfirm']=='2')])
               * 100/ (len(tb_merge_fwznm)- len(tb_merge_fwznm[(tb_merge_fwznm['exemption_form']=='5') & (tb_merge_fwznm['exemption_form_explain'].isin(['原件需收回或签注','所需证照全部非本市核发','使用国家系统且没有线下办理窗口']))])),'.2f')

    #减时间
    tb_fwzn1 = tb_fwzn[(tb_fwzn['ql_kind']=='01') & (tb_fwzn['ql_state']=='1')]
    tb_fwznc = tb_fwzn1[(~ tb_fwzn1['promise_day'].isin(['未规定'])) & (~ tb_fwzn1['anticipate_day'].isin(['未规定']))]
    tb_fwznc.loc[tb_fwznc['promise_day'].isin(['当场办结']),'promise_day'] = 0
    tb_fwznc.loc[tb_fwznc['anticipate_day'].isin(['当场办结']), 'anticipate_day'] = 0
    tb_fwznc[['promise_day','anticipate_day']] = tb_fwznc[['promise_day','anticipate_day']].apply(pd.to_numeric)
    zwfw_serviceeffic.loc[0, 'timereduction'] =format((sum(tb_fwznc['anticipate_day']) - sum(tb_fwznc['promise_day']))
                                                      * 100 / sum(tb_fwznc['anticipate_day']), '.2f')
    #即办件
    zwfw_serviceeffic.loc[0, 'immediatedegree'] = format(len(tb_fwzn1[tb_fwzn1['bjtype']=='1']) * 100 / len(tb_fwzn1),'.2f')

    zwfw_serviceeffic.loc[0, 'serviceindex'] = format(np.mean(zwfw_serviceeffic.iloc[0,0:4].apply(pd.to_numeric)),'.2f')


    cal_date = datetime.now()+dateutil.relativedelta.relativedelta(months=-1)
    zwfw_serviceeffic.loc[0, 'month'] = str(cal_date.month)
    return zwfw_serviceeffic