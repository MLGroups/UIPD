# -*- coding: utf-8 -*-
# @Time     :2018/4/17 下午4:04
# @Author   :李二狗
# @Site     :
# @File     :feature_user.py
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



# train dataset
"""

# 补全经纬度信息
def format_geohash(str):
    if str == 'nan':
        return '0000:000'
    else:
        if len(str) == 4:
            return '00' + str[0:2] + ':0' + str[2:4]
        elif len(str) == 5:
            return '0' + str[0:3] + ':0' + str[3:5]
        elif len(str) == 6:
            return '0' + str[0:3]+':'+str[3:6]
        else:
            return str[0:4] + ':' + str[4:7]

user_train_dateset0 = pd.read_csv('data/user_train_dateset0.csv', header=0, dtype=str)

# 经纬度信息
user_train_dateset0['user_geohash'] = user_train_dateset0['user_geohash'].astype('str')
user_train_dateset0['user_geohash'] = user_train_dateset0['user_geohash'].apply(format_geohash)
longi_lati = user_train_dateset0['user_geohash'].str.split(':', expand=True)
df_longi_lati = pd.DataFrame(longi_lati)
df_longi_lati.columns = ['longitude', 'latitude']
user_train_dateset0['longitude'] = df_longi_lati['longitude']
user_train_dateset0['latitude'] = df_longi_lati['latitude']

# 时间
time = user_train_dateset0['time'].str.split(' ', expand=True)
df_time = pd.DataFrame(time)
df_time.columns = ['date', 'hour']
user_train_dateset0['date'] = df_time['date']
user_train_dateset0['hour'] = df_time['hour']
print(user_train_dateset0.head(100))

# 对behavior_type 进行哑编码
from sklearn.preprocessing import OneHotEncoder
behavior_type = pd.DataFrame(user_train_dateset0['behavior_type'])
enc = OneHotEncoder
enc.fit([[0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0]])
print(enc.n_values_)
print(enc.feature_indices_)
# behavior_type = enc.transform(behavior_type.values.tolist())
# print(behavior_type.head())
# user_day_buy_dateset0 = pd.read_csv('data/user_day_buy_dateset0.csv', header=0, dtype=str)

# user_train = user_train_dateset3['time'].str.split(' ', expand=True)
# print(user_train_dateset3.shape)



