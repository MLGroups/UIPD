# -*- coding: utf-8 -*-
# @Time     :2018/4/17 下午5:46
# @Author   :李二狗
# @Site     :
# @File     :pre_handle_data.py
# @Software :PyCharm


import numpy as np
import pandas as pd

"""
    dataset split:
                     user_train_dateset3: 20141219 (behavior_type = 4),features3 from 20141209~20141218
                     user_train_dateset2: 20141212 (behavior_type = 4),features2 from 20141202~20141212  
                     user_train_dateset1: 20141205 (behavior_type = 4),features1 from 20141125~20141205
                     user_train_dateset0: 20141128 (behavior_type = 4),features0 from 20141118~20141127    


    1 item related:


    2 user related:

    3 item-user related:



"""

user_train = pd.read_csv('data/tianchi_fresh_comp_train_user.csv', header=0, dtype=str)
# dataset3:
user_train_dateset3 = user_train[((user_train.time >= '2014-12-09 00') & (user_train.time < '2014-12-18 24'))]
user_train_dateset3.to_csv('data/user_train_dateset3.csv', index=None)
print('user_train_dateset3', user_train_dateset3.shape)

user_train_dateset2 = user_train[((user_train.time >= '2014-12-02 00') & (user_train.time < '2014-12-11 24'))]
user_train_dateset2.to_csv('data/user_train_dateset2.csv', index=None)
print('user_train_dateset2', user_train_dateset2.shape)

user_train_dateset1 = user_train[((user_train.time >= '2014-11-25 00') & (user_train.time < '2014-12-04 24'))]
user_train_dateset1.to_csv('data/user_train_dateset1.csv', index=None)
print('user_train_dateset1', user_train_dateset1.shape)

user_train_dateset0 = user_train[((user_train.time >= '2014-11-18 00') & (user_train.time < '2014-11-27 24'))]
user_train_dateset0.to_csv('data/user_train_dateset0.csv', index=None)
print('user_train_dateset0', user_train_dateset0.shape)

# dataset3:
user_day_buy_dateset2 = user_train[((user_train.time >= '2014-12-12 00') & (user_train.time < '2014-12-12 24')) & (user_train.behavior_type == '4')]
user_day_buy_dateset2.to_csv('data/user_day_buy_dateset2.csv', index=None)
print('user_day_buy_dateset2', user_day_buy_dateset2.shape)

user_day_buy_dateset1 = user_train[((user_train.time >= '2014-12-05 00') & (user_train.time < '2014-12-05 24')) & (user_train.behavior_type == '4')]
user_day_buy_dateset1.to_csv('data/user_day_buy_dateset1.csv', index=None)
print('user_day_buy_dateset1', user_day_buy_dateset1.shape)

user_day_buy_dateset0 = user_train[((user_train.time >= '2014-11-28 00') & (user_train.time < '2014-11-28 24')) & (user_train.behavior_type == '4')]
user_day_buy_dateset0.to_csv('data/user_day_buy_dateset0.csv', index=None)
print('user_day_buy_dateset0', user_day_buy_dateset0.shape)
