# -*- coding: utf-8 -*-
"""
    pandas的取值和选择
"""

import pandas as pd

# Series提供多种取值方式
def get_series():
    data=pd.Series([0.25,0.5,0.75,1],index=['a','b','c','d'])
    # 键值获取
    print(data['a'])
    # 表达式的方式
    print('a' in data)
    print(data.keys())
    print(list(data.items()))
    # 显示索引切片, 隐式索引切片(隐式不包括2)
    print(data['a':'c'])
    print(data[0:2])
    # 掩码
    print(data[(data>0.5)])
    # 花哨（即使用索引筛选）
    print(data[['a','d']])
    # loc属性表示显示切片，iloc表示隐式切片
    print(data.loc['a':'c'])
    print(data.iloc[0:1])
    
def get_dataframe():
    area=pd.Series({"a":1,"b":2,"c":3,"d":4,"e":5})
    pop=pd.Series({"a":11,"b":21,"c":13,"d":14,"e":51})
    data=pd.DataFrame({'area':area,'pop':pop})
    # 字典和attribute-style方式获的字符串，需要注意，当属性和dataframe内置方法冲突时，这种方式不可用
    print(data['area'])
    print(data.area)
    # 动态增加列
    data['density']=data['area']/data['pop']
    print(data)
    # 矩阵转置
    print(data.T)
    # 第一行
    print(data.values[0])
    # 
    print(data['area'])
get_series()
get_dataframe()