# -*- coding: utf-8 -*-
# @Time     :2018/4/18 上午10:21
# @Author   :李二狗
# @Site     :
# @File     :Drop_Day_and_sub_item.py
# @Software :PyCharm

import pandas as pd

user_table = pd.read_csv('data/tianchi_fresh_comp_train_user.csv')
item_table = pd.read_csv('data/tianchi_fresh_comp_train_item.csv')

# 筛选出 item list 存在的数据
user_table = user_table[user_table.item_id.isin(list(item_table.item_id))]
# 获取 日期
user_table['days'] = user_table['time'].map(lambda x:x.split(' ')[0])
# 获取 所在时段
user_table['hours'] = user_table['time'].map(lambda x:x.split(' ')[1])

user_table = user_table[user_table['days'] != '2014-12-12']
user_table = user_table[user_table['days'] != '2014-12-11']
user_table.to_csv('data/drop1112_sub_item.csv', index=None)
