import pandas as pd
import numpy as np
import jieba
from collections import Counter
from datetime import timedelta
from epointml.utils import DbPoolUtil
def data_extract(df):
    
    df=df.loc[:,['taskid','discovertime','infozcname','streetname','userevaluate','x','y','description','description_12345','synctime']]
    df.columns = ['taskid', 'discovertime', 'infozcname', 'streetname', 'myd', 'x', 'y', 'description', 'fkjl','synctime']
    df.sort_values('synctime',inplace=True)
    df.drop_duplicates(subset='taskid',keep='last',inplace=True)
    df=df.loc[:,['taskid', 'discovertime', 'infozcname', 'streetname', 'myd', 'x', 'y', 'description', 'fkjl']]
    df = df[df['x'] != '121.468372271213']
    print(len(df))

    # df=df[df['x']!=121.469099349524]
    # df=df[df['x']!=121.48190922212]
    # df=df.loc[:,['taskid','discovertime','infozcname','streetname','myd','x','y', 'description']]

    df['discovertime'] = pd.to_datetime(df['discovertime'])

    df.drop(df[df['myd'] == '未表态'].index, inplace=True)
    df.drop(df[df['myd'] == 'NaN'].index, inplace=True)
    df = df[df['myd'] != '满意']
    df.dropna(subset=['myd'],inplace=True)

    df['infozcname'].loc[df[df['infozcname'] == '国有档案']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '个人档案']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '商业服务']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '工商监管']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '工商信息']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '违法经营']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '合作交流']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '服务质量']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '旅游纠纷']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '旅游信息']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '生活保障']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '救灾赈灾']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '优抚安置']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '社区家政']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '养老保障']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '慈善福利']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '殡葬事业']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '婚姻管理']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '寺庙管理']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '宗教信仰']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '侨务工作']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '统战工作']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '就业创业']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '劳动保护']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '社保信息']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '劳动人事制度']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '医疗医保']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '工伤']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '津贴补助']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '社会保险']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '外事工作']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '知识产权']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '道路维护']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '公共道路']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '工程管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '违法建筑']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '燃气行业监管']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '污染']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '夜间施工许可']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '驾驶培训']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '车辆拍卖']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '公交巴士']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '铁路客运']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '地铁客运']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '出租车']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '港船客运']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '航空客运']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '汽车客运']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '货物运输']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '汽车维修']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '公共交通用卡管理']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '停车管理']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '口岸协调']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '口岸信息']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '禽类饲养']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '环境卫生']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '城市管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '市容市貌']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '绿地绿化']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '动植园林']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '民防工程']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '防灾抗灾']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '水资源管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '排水排污管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '河道流域管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '城市建设用地管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '非城市建设用地管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '建设管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '土地资源管理']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '房屋权属']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '旧房改造']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '保障型住房']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '物业服务管理']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '市场交易管理']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '征收管理']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '住房病虫害']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '物业相关执法']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '财政工作']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '改革规划']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '价格调控']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '国资']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '金融']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '经济信息化']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '村队管理']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '农业生产']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '动植物防疫']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '农民负担']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '商务']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '审计工作']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '税收政策']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '税收管理']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '统计工作']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '招生考试']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '学校管理']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '学生负担']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '入学入托']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '科技开发']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '科技管理']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '体育管理']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '医院监管']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '卫生信息']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '医疗服务']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '特定医疗机构']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '人口计生']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '广播影视']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '文化产业管理']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '文化遗产保护']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '新闻报道']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '刊物市场监管']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '法院受理']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '法院信息']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '护照办理']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '签证签注']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '出境咨询']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '行政管理']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '消防管理']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '消防设备维护']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '审批许可']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '社会噪声']['infozcname'].index] = '环境保护'
    df['infozcname'].loc[df[df['infozcname'] == '交通管理']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '户籍管理']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '犬类管理']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '社会治安']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '特种行业管理']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '国家安全']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '检察院受理']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '法律服务']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '公证服务']['infozcname'].index] = '文化生活'
    df['infozcname'].loc[df[df['infozcname'] == '纠纷仲裁']['infozcname'].index] = '经济发展'
    df['infozcname'].loc[df[df['infozcname'] == '司法直属']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '故障报修']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '限电管理']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '用电计费']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '电力服务']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '违规用电']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '供水报修']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '自来水水质']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '供水计费']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '供水服务']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '违规用水']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '气象预报']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '气象预警']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '燃气报修']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '燃气计费']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '燃气服务']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '通信']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '邮政服务']['infozcname'].index] = '民生保障'
    df['infozcname'].loc[df[df['infozcname'] == '妇联']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '其他社团']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '团市委']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '总工会']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '安全生产']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '职业健康']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '安全管理']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '广告审批']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '申诉举报']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '计量器具检测']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '生产许可证管理']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '特种设备监察']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '组织机构代码证']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '质量认证']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '表扬感谢']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '投诉批评']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '意见建议']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '传真信息']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '12345热线']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '表扬承办部门']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '批评承办部门']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '部队']['infozcname'].index] = '安全管理'
    df['infozcname'].loc[df[df['infozcname'] == '残联']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '工青妇工作']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '机关事务管理']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '纪检监查']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '政风行风']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '无效电话']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '涉港澳台']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '其他']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '咨询信访渠道']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '查询办理进度']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '复查复核']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '事项办理']['infozcname'].index] = '社会服务'
    df['infozcname'].loc[df[df['infozcname'] == '中央直属']['infozcname'].index] = '社会服务'

    df_origin = df

    df = df[df.sort_values('discovertime')['discovertime'].iloc[-1] - df['discovertime'] < timedelta(days=365)]

    df1 = df.loc[:, ['infozcname', 'streetname']]
    df1['amount'] = 1
    df1 = pd.pivot_table(df1, index=['infozcname', 'streetname'], aggfunc='count').reset_index()

    df1_ = df1.sort_values(['infozcname', 'amount'], ascending=False)

    list_keywords = ['动迁', '物业', '房屋', '搭建', '扰民', '噪音', '施工', '协调', '垃圾', '拆除', '冠状病毒', '装修', '安装', '违章', '停车', '经营',
                     '维修', '群租', '人行道', '安全隐患', '工资', '违章建筑', '漏水', '停放', '堆放', '户口', '设摊', '无证', '楼道', '改造', '弄堂',
                     '环境', '垃圾桶', '合同', '拖欠', '出租', '补贴', '非机动车', '租房', '租赁', '停车费', '居住证', '幼儿园', '油烟', '绿化', '雨棚',
                     '改建', '消防通道', '跨门', '污水', '杂物', '民宿', '外墙', '广告', '建筑工地', '废品', '脚手架', '补助', '厕所', '消防', '承重墙',
                     '残疾人', '垃圾堆', '房产证', '堵塞', '餐饮店', '物业管理', '拆违', '拖欠工资', '房屋结构', '充电', '菜场', '施工方', '清运', '市容',
                     '围墙', '保障', '积水', '养老院', '车库', '营业执照', '下水道', '损坏', '棋牌室', '火灾', '修剪', '封闭', '墙面', '拆掉', '危险',
                     '酒吧', '堆物', '脏乱差', '退款', '教育', '报修', '调解', '广告牌', '玻璃', '扩音', '廉租房', '破墙', '招牌', '疏通', '晾晒', '低保',
                     '扬尘', '入学', '业主大会']
    ###############################
    df1_1 = pd.DataFrame()
    df1_1 = pd.concat([df1_1,df1_[df1_['infozcname']=='经济发展'].sort_values('amount', ascending=False).iloc[0:2]], axis=0)
    df1_1 = pd.concat([df1_1,df1_[df1_['infozcname']=='社会服务'].sort_values('amount', ascending=False).iloc[0:2]], axis=0)
    df1_1 = pd.concat([df1_1,df1_[df1_['infozcname']=='环境保护'].sort_values('amount', ascending=False).iloc[0:2]], axis=0)
    df1_1 = pd.concat([df1_1,df1_[df1_['infozcname']=='民生保障'].sort_values('amount', ascending=False).iloc[0:2]], axis=0)
    df1_1 = pd.concat([df1_1,df1_[df1_['infozcname']=='文化生活'].sort_values('amount', ascending=False).iloc[0:2]], axis=0)
    df1_1 = pd.concat([df1_1,df1_[df1_['infozcname']=='安全管理'].sort_values('amount', ascending=False).iloc[0:2]], axis=0)
    #######################################
    list_tuple = []
    for i in range(len(df1_1)):
        list_tuple.append(tuple(df1_1.drop('amount', axis=1).iloc[i]))

    gp = df.groupby(['infozcname', 'streetname'])

    list_wordcut1 = []
    list_wordcut2 = []
    list_wordcut3 = []
    list_wordcut4 = []
    list_wordcut5 = []
    list_wordcut6 = []
    list_wordcut11 = []
    list_wordcut22 = []
    list_wordcut33 = []
    list_wordcut44 = []
    list_wordcut55 = []
    list_wordcut66 = []




    word_cut = gp.get_group(list_tuple[0])['description'].apply(jieba.lcut, 1)

    for m in word_cut:
        for j in m:
            list_wordcut1.append(j)
    ans_jjfz = [x for x in list_wordcut1 if len(x) > 1 and x in list_keywords]
    ans_jjfz = Counter(ans_jjfz)
    if ans_jjfz == Counter():
        ans_jjfz =[]
    else:
        ans_jjfz = list(pd.DataFrame(sorted(ans_jjfz.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])


    word_cut = gp.get_group(list_tuple[1])['description'].apply(jieba.lcut, 1)
    for m in word_cut:
        for j in m:
            list_wordcut11.append(j)
    ans_jjfz1 = [x for x in list_wordcut11 if len(x) > 1 and x in list_keywords]
    ans_jjfz1 = Counter(ans_jjfz1)
    if ans_jjfz1 == Counter():
        ans_jjfz1 =[]
    else:
        ans_jjfz1 = list(pd.DataFrame(sorted(ans_jjfz1.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])


    word_cut = gp.get_group(list_tuple[2])['description'].apply(jieba.lcut, 1)
    for m in word_cut:
        for j in m:
            list_wordcut2.append(j)
    ans_shfw = [x for x in list_wordcut2 if len(x) > 1 and x in list_keywords]
    ans_shfw = Counter(ans_shfw)
    if ans_shfw == Counter():
        ans_shfw =[]
    else:
        ans_shfw = list(pd.DataFrame(sorted(ans_shfw.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])


    word_cut = (gp.get_group(list_tuple[3])['description'].apply(jieba.lcut, 1))
    for m in word_cut:
        for j in m:
            list_wordcut22.append(j)
    ans_shfw1 = [x for x in list_wordcut22 if len(x) > 1 and x in list_keywords]
    ans_shfw1 = Counter(ans_shfw1)
    if ans_shfw1 == Counter():
        ans_shfw1 =[]
    else:
        ans_shfw1 = list(pd.DataFrame(sorted(ans_shfw1.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])


    word_cut = gp.get_group(list_tuple[4])['description'].apply(jieba.lcut, 1)
    for m in word_cut:
        for j in m:
            list_wordcut3.append(j)
    ans_hjbh = [x for x in list_wordcut3 if len(x) > 1 and x in list_keywords]
    ans_hjbh = Counter(ans_hjbh)
    if ans_hjbh == Counter():
        ans_hjbh =[]
    else:
        ans_hjbh = list(pd.DataFrame(sorted(ans_hjbh.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])



    word_cut = (gp.get_group(list_tuple[5])['description'].apply(jieba.lcut, 1))
    for m in word_cut:
        for j in m:
            list_wordcut33.append(j)
    ans_hjbh1 = [x for x in list_wordcut33 if len(x) > 1 and x in list_keywords]
    ans_hjbh1 = Counter(ans_hjbh1)
    if ans_hjbh1 == Counter():
        ans_hjbh1 =[]
    else:
        ans_hjbh1 = list(pd.DataFrame(sorted(ans_hjbh1.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])


    if len(list_tuple)<=6:
        ans_msbz=[]
    else:
        word_cut = gp.get_group(list_tuple[6])['description'].apply(jieba.lcut, 1)
        for m in word_cut:
            for j in m:
                list_wordcut4.append(j)
        ans_msbz = [x for x in list_wordcut4 if len(x) > 1 and x in list_keywords]
        ans_msbz = Counter(ans_msbz)
        if ans_msbz == Counter():
            ans_msbz =[]
        else:
            ans_msbz = list(pd.DataFrame(sorted(ans_msbz.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])
            
            

    if len(list_tuple)<=7:
        ans_msbz1 = []
    else:
        word_cut = (gp.get_group(list_tuple[7])['description'].apply(jieba.lcut, 1))
        for m in word_cut:
            for j in m:
                list_wordcut44.append(j)
        ans_msbz1 = [x for x in list_wordcut44 if len(x) > 1 and x in list_keywords]
        ans_msbz1 = Counter(ans_msbz1)
        if ans_msbz1 == Counter():
            ans_msbz1 = []
        else:
            ans_msbz1 = list(pd.DataFrame(sorted(ans_msbz1.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])

    if len(list_tuple)<=8:
        ans_whsh =[]
    else:
        word_cut = gp.get_group(list_tuple[8])['description'].apply(jieba.lcut, 1)
        for m in word_cut:
            for j in m:
                list_wordcut5.append(j)
        ans_whsh = [x for x in list_wordcut5 if len(x) > 1 and x in list_keywords]
        ans_whsh = Counter(ans_whsh)
        if ans_whsh == Counter():
            ans_whsh =[]
        else:
            ans_whsh = list(pd.DataFrame(sorted(ans_whsh.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])
            
            
    if len(list_tuple)<=9:
        ans_whsh1 =[]
    else:
        word_cut = (gp.get_group(list_tuple[9])['description'].apply(jieba.lcut, 1))
        for m in word_cut:
            for j in m:
                list_wordcut55.append(j)
        ans_whsh1 = [x for x in list_wordcut55 if len(x) > 1 and x in list_keywords]
        ans_whsh1 = Counter(ans_whsh1)
        if ans_whsh1 == Counter():
            ans_whsh1 =[]
        else:
            ans_whsh1 = list(pd.DataFrame(sorted(ans_whsh1.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])

    if len(list_tuple)<=10:
        ans_aqgl = []
    else:
        word_cut = gp.get_group(list_tuple[10])['description'].apply(jieba.lcut, 1)
        for m in word_cut:
            for j in m:
                list_wordcut6.append(j)
        ans_aqgl = [x for x in list_wordcut6 if len(x) > 1 and x in list_keywords]
        ans_aqgl = Counter(ans_aqgl)
        if ans_aqgl == Counter():
            ans_aqgl = []
        else:
            ans_aqgl = list(pd.DataFrame(sorted(ans_aqgl.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])

    if len(list_tuple)<=11:
        ans_aqgl1 = []
    else:
        word_cut = (gp.get_group(list_tuple[11])['description'].apply(jieba.lcut, 1))
        for m in word_cut:
            for j in m:
                list_wordcut66.append(j)
        ans_aqgl1 = [x for x in list_wordcut66 if len(x) > 1 and x in list_keywords]
        ans_aqgl1 = Counter(ans_aqgl1)
        if ans_aqgl1 == Counter():
            ans_aqgl1 = []
        else:
            ans_aqgl1 = list(pd.DataFrame(sorted(ans_aqgl1.items(), key=lambda d: d[1], reverse=True)).iloc[0:6, 0])


    df['key'] = df['infozcname'] + df['streetname']
    df1_1['key'] = df1_1['infozcname'] + df1_1['streetname']

    df_total = df1_1.merge(df, how='inner')

    df_total.loc[df_total[df_total['myd'] == '一般'].index, 'myd'] = 0.6
    df_total.loc[df_total[df_total['myd'] == '基本满意'].index, 'myd'] = 0.8
    df_total.loc[df_total[df_total['myd'] == '不满意'].index, 'myd'] = 0

    # df_temp

    # df_result

    # df_total[df_total['key']==df1_1.iloc[5,-1]]['xy'].value_counts().sort_values(ascending=False)

    # df_total[df_total['key']==df1_1.iloc[1,-1]][df_total[df_total['key']==df1_1.iloc[1,-1]]['xy']==df_total[df_total['key']==df1_1.iloc[1,-1]]['xy'].value_counts().index[0]]

    #

    #

    # Mdf_total[df_total['key']==df1_1.iloc[1,-1]]['myd']

    df_xy = df_origin.loc[:, ['x', 'y', 'infozcname']]

    df_total['xy'] = df_total['x'].astype('str') + df_total['y'].astype('str')

    list1 = list(df1_1['key'])

    df_append = pd.DataFrame()
    list_ = []
    for i in list1:
        df_temp = df_total[df_total['key'] == i][df_total[df_total['key'] == i]['xy'] ==
                                                 df_total[df_total['key'] == i]['xy'].value_counts().sort_values(
                                                     ascending=False).index[0]]
        df_temp['myd'] = df_temp['myd'].astype('float')
        list_.append(
            [df_temp['infozcname'].iloc[0], df_temp['streetname'].iloc[0], df_temp['x'].iloc[0], df_temp['y'].iloc[0],
             df_temp['amount'].iloc[0], df_temp['description'].iloc[0],
             int(np.average(df_total[df_total['key'] == i]['myd'].astype('float')) * 100), df_temp['fkjl'].iloc[0]])
        for n in range(8):
            df_append = df_append.append(df_temp.loc[:, ['x', 'y', 'infozcname']])

    # df_total[df_total['key']==df1_1.iloc[0,-1]]['xy'].value_counts()

    # df_total[df_total['xy']==df_total[df_total['key']==df1_1.iloc[0,-1]]['xy'].value_counts().index[0]]

    df_xy = df_origin.loc[:, ['x', 'y', 'infozcname']]
    df_xy = pd.concat([df_xy, df_append], axis=0)
    # df_xy.append(df_append)

    # 找到病灶点坐标生成山峰

    df_result = pd.DataFrame(list_)
    df_result.columns = ['infozcname', 'streetname', 'x', 'y', 'amount', 'description', 'myd', 'fkjl']

    df_total_ = df_total[df_total['description'].map(lambda x: '重新交办' not in x)]
    list_num = []
    dict1 = {}
    content = list(df_total_[df_total_['key'] == df1_1.iloc[0, -1]]['description'])
    for m in ans_jjfz:
        list_num.append(
            [m, sum(df_total_[df_total_['key'] == df1_1.iloc[0, -1]]['description'].map(lambda x: 1 if m in x else 0)),
             np.average(df_total_[df_total_['key'] == df1_1.iloc[0, -1]][
                            df_total_[df_total_['key'] == df1_1.iloc[0, -1]]['description'].map(
                                lambda x: True if m in x else False)]['myd'].astype('float'))])
        for j in range(len(list(content))):
            if m in content[j]:
                dict1[m] = content[j]
                content.remove(content[j])
                break
    dict2 = {}
    content = list(df_total_[df_total_['key'] == df1_1.iloc[1, -1]]['description'])
    for m in ans_jjfz1:
        list_num.append(
            [m, sum(df_total_[df_total_['key'] == df1_1.iloc[1, -1]]['description'].map(lambda x: 1 if m in x else 0)),
             np.average(df_total_[df_total_['key'] == df1_1.iloc[1, -1]][
                            df_total_[df_total_['key'] == df1_1.iloc[1, -1]]['description'].map(
                                lambda x: True if m in x else False)]['myd'].astype('float'))])
        for j in range(len(list(content))):
            if m in content[j]:
                dict2[m] = content[j]
                content.remove(content[j])
                break
    dict3 = {}
    content = list(df_total_[df_total_['key'] == df1_1.iloc[2, -1]]['description'])
    for m in ans_shfw:
        list_num.append(
            [m, sum(df_total_[df_total_['key'] == df1_1.iloc[2, -1]]['description'].map(lambda x: 1 if m in x else 0)),
             np.average(df_total_[df_total_['key'] == df1_1.iloc[2, -1]][
                            df_total_[df_total_['key'] == df1_1.iloc[2, -1]]['description'].map(
                                lambda x: True if m in x else False)]['myd'].astype('float'))])
        for j in range(len(list(content))):
            if m in content[j]:
                dict3[m] = content[j]
                content.remove(content[j])
                break
    dict4 = {}
    content = list(df_total_[df_total_['key'] == df1_1.iloc[3, -1]]['description'])
    for m in ans_shfw1:
        list_num.append(
            [m, sum(df_total_[df_total_['key'] == df1_1.iloc[3, -1]]['description'].map(lambda x: 1 if m in x else 0)),
             np.average(df_total_[df_total_['key'] == df1_1.iloc[3, -1]][
                            df_total_[df_total_['key'] == df1_1.iloc[3, -1]]['description'].map(
                                lambda x: True if m in x else False)]['myd'].astype('float'))])
        for j in range(len(list(content))):
            if m in content[j]:
                dict4[m] = content[j]
                content.remove(content[j])
                break
    dict5 = {}
    content = list(df_total_[df_total_['key'] == df1_1.iloc[4, -1]]['description'])
    for m in ans_hjbh:
        list_num.append(
            [m, sum(df_total_[df_total_['key'] == df1_1.iloc[4, -1]]['description'].map(lambda x: 1 if m in x else 0)),
             np.average(df_total_[df_total_['key'] == df1_1.iloc[4, -1]][
                            df_total_[df_total_['key'] == df1_1.iloc[4, -1]]['description'].map(
                                lambda x: True if m in x else False)]['myd'].astype('float'))])
        for j in range(len(list(content))):
            if m in content[j]:
                dict5[m] = content[j]
                content.remove(content[j])
                break
    dict6 = {}
    content = list(df_total_[df_total_['key'] == df1_1.iloc[5, -1]]['description'])
    for m in ans_hjbh1:
        list_num.append(
            [m, sum(df_total_[df_total_['key'] == df1_1.iloc[5, -1]]['description'].map(lambda x: 1 if m in x else 0)),
             np.average(df_total_[df_total_['key'] == df1_1.iloc[5, -1]][
                            df_total_[df_total_['key'] == df1_1.iloc[5, -1]]['description'].map(
                                lambda x: True if m in x else False)]['myd'].astype('float'))])
        for j in range(len(list(content))):
            if m in content[j]:
                dict6[m] = content[j]
                content.remove(content[j])
                break
                
                
    dict7 = {}
    if len(df1_1)<=6:
        pass
    else:
        content = list(df_total_[df_total_['key'] == df1_1.iloc[6, -1]]['description'])
        for m in ans_msbz:
            list_num.append(
                [m, sum(df_total_[df_total_['key'] == df1_1.iloc[6, -1]]['description'].map(lambda x: 1 if m in x else 0)),
                 np.average(df_total_[df_total_['key'] == df1_1.iloc[6, -1]][
                                df_total_[df_total_['key'] == df1_1.iloc[6, -1]]['description'].map(
                                    lambda x: True if m in x else False)]['myd'].astype('float'))])
            for j in range(len(list(content))):
                if m in content[j]:
                    dict7[m] = content[j]
                    content.remove(content[j])
                    break
                
                
                
    dict8 = {}
    if len(df1_1)<=7:
        pass
    else:
        content = list(df_total_[df_total_['key'] == df1_1.iloc[7, -1]]['description'])
        for m in ans_msbz1:
            list_num.append(
                [m, sum(df_total_[df_total_['key'] == df1_1.iloc[7, -1]]['description'].map(lambda x: 1 if m in x else 0)),
                 np.average(df_total_[df_total_['key'] == df1_1.iloc[7, -1]][
                                df_total_[df_total_['key'] == df1_1.iloc[7, -1]]['description'].map(
                                    lambda x: True if m in x else False)]['myd'].astype('float'))])
            for j in range(len(list(content))):
                if m in content[j]:
                    dict8[m] = content[j]
                    content.remove(content[j])
                    break
                
    dict9 = {}
    if len(df1_1)<=8:
        pass
    else:
        content = list(df_total_[df_total_['key'] == df1_1.iloc[8, -1]]['description'])
        for m in ans_whsh:
            list_num.append(
                [m, sum(df_total_[df_total_['key'] == df1_1.iloc[8, -1]]['description'].map(lambda x: 1 if m in x else 0)),
                 np.average(df_total_[df_total_['key'] == df1_1.iloc[8, -1]][
                                df_total_[df_total_['key'] == df1_1.iloc[8, -1]]['description'].map(
                                    lambda x: True if m in x else False)]['myd'].astype('float'))])
            for j in range(len(list(content))):
                if m in content[j]:
                    dict9[m] = content[j]
                    content.remove(content[j])
                    break
    dict10 = {}
    if len(df1_1)<=9:
        pass
    else:
        content = list(df_total_[df_total_['key'] == df1_1.iloc[9, -1]]['description'])
        for m in ans_whsh1:
            list_num.append(
                [m, sum(df_total_[df_total_['key'] == df1_1.iloc[9, -1]]['description'].map(lambda x: 1 if m in x else 0)),
                 np.average(df_total_[df_total_['key'] == df1_1.iloc[9, -1]][
                                df_total_[df_total_['key'] == df1_1.iloc[9, -1]]['description'].map(
                                    lambda x: True if m in x else False)]['myd'].astype('float'))])
            for j in range(len(list(content))):
                if m in content[j]:
                    dict10[m] = content[j]
                    content.remove(content[j])
                    break

    dict11 = {}
    if len(df1_1)<=10:
        pass
    else:
        content = list(df_total_[df_total_['key'] == df1_1.iloc[10, -1]]['description'])
        for m in ans_aqgl:
            list_num.append(
                [m, sum(df_total_[df_total_['key'] == df1_1.iloc[10, -1]]['description'].map(lambda x: 1 if m in x else 0)),
                 np.average(df_total_[df_total_['key'] == df1_1.iloc[10, -1]][
                                df_total_[df_total_['key'] == df1_1.iloc[10, -1]]['description'].map(
                                    lambda x: True if m in x else False)]['myd'].astype('float'))])
            for j in range(len(list(content))):
                if m in content[j]:
                    dict11[m] = content[j]
                    content.remove(content[j])
                    break
                    

    dict12 = {}
    if len(df1_1)<=11:
        pass
    else:
        content = list(df_total_[df_total_['key'] == df1_1.iloc[11, -1]]['description'])
        for m in ans_aqgl1:
            list_num.append(
                [m, sum(df_total_[df_total_['key'] == df1_1.iloc[11, -1]]['description'].map(lambda x: 1 if m in x else 0)),
                 np.average(df_total_[df_total_['key'] == df1_1.iloc[11, -1]][
                                df_total_[df_total_['key'] == df1_1.iloc[11, -1]]['description'].map(
                                    lambda x: True if m in x else False)]['myd'].astype('float'))])
            for j in range(len(list(content))):
                if m in content[j]:
                    dict12[m] = content[j]
                    content.remove(content[j])
                    break

    # np.average(df_total_[df_total_['key']==df1_1.iloc[10,-1]][df_total_[df_total_['key']==df1_1.iloc[10,-1]]['description'].map(lambda x : True if m in x else False)]['myd'].astype('float'))

    list_dict = [dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12]
    list_ans = [ans_jjfz, ans_jjfz1, ans_shfw, ans_shfw1, ans_hjbh, ans_hjbh1, ans_msbz, ans_msbz1, ans_whsh, ans_whsh1,
                ans_aqgl, ans_aqgl1]

    list_result = []
    for j in range(len(list_ans)):
        for i in range(len(list_ans[j])):
            if len(df[df['description'] == list_dict[j].get(list_ans[j][i])]['fkjl']) == 0:
                list_result.append(
                    [j + 1, df_result['infozcname'].iloc[j], df_result['streetname'].iloc[j], list_ans[j][i],
                     list_dict[j].get(list_ans[j][i]), df_result['myd'].iloc[j], df_result['x'].iloc[j],
                     df_result['y'].iloc[j], df_result['amount'].iloc[j], 'NaN'])
            else:
                list_result.append(
                    [j + 1, df_result['infozcname'].iloc[j], df_result['streetname'].iloc[j], list_ans[j][i],
                     list_dict[j].get(list_ans[j][i]), df_result['myd'].iloc[j], df_result['x'].iloc[j],
                     df_result['y'].iloc[j], df_result['amount'].iloc[j],
                     df[df['description'] == list_dict[j].get(list_ans[j][i])]['fkjl'].iloc[0]])

    kwords_num = []
    kwords_num1 = []
    for i in list_num:
        kwords_num.append(i[1])
        kwords_num1.append(i[2])

    df_final = pd.DataFrame(list_result)

    df_final['num'] = kwords_num
    df_final['kword_myd'] = kwords_num1

    df_final.columns = ['id', 'infozcname', 'streetname', 'kwords', 'description', 'myd', 'x', 'y', 'amount', 'fkjl',
                        'kword_num', 'kword_myd']

    df_final = df_final.dropna()
    df_final['kword_myd'] = df_final['kword_myd'].map(lambda x: int(x * 100))

    df_final_ = pd.DataFrame()
    for i in range(1, 13):
        if sum(df_final['id'] == i) < 3:
            pass
        else:
            df_final_ = pd.concat([df_final_, df_final[df_final['id'] == i]], axis=0)
    df_xy['num']=1
    df_final_=df_final_.reindex(columns=['id','infozcname','streetname','kwords','description','myd','x','y','amount','fkjl','kword_num','kword_myd'])
    df_final_=df_final_.reset_index().drop(['index'],axis=1)

    return  df_xy,df_final_