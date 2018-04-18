# -*- coding: utf-8 -*-
# @Time     :2018/4/17 下午4:04
# @Author   :李二狗
# @Site     :
# @File     :feature_item.py
# @Software :PyCharm

import numpy as np
import pandas as pd


"""
    dataset split:
                     dateset3: 20141219 (behavior_type = 4),features3 from 20141209~20141218
                     dateset2: 20141212 (behavior_type = 4),features2 from 20141202~20141212  
                     dateset1: 20141205 (behavior_type = 4),features1 from 20141125~20141205
                     dateset0: 20141128 (behavior_type = 4),features0 from 20141118~20141127    
                     
                     
    1 item related:
      
    
    2 user related:
    
    3 item-user related:
      
        
                     
"""


item_train = pd.read_csv('data/tianchi_fresh_comp_train_item.csv', header=0, dtype=str)
print(item_train.head(100))
# print(item_train.info())


# dataset3:
# feature3 = off_train[((off_train.date>='20160401')&(off_train.date<='20160630'))