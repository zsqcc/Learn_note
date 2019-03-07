# -*- coding: utf-8 -*-
"""
    pandas可以看作增强版numpy，其有Series、DataFrame、Index对象
    Index对象：可看作不可变数组，其具备切片等功能
"""
import pandas as pd

# Series对象是一个带索引的一维数组 / 特殊的字典
def create_series():
    # 创建
     data=pd.Series([0.25,0.5,0.75,1.0])
     # 属性
     data.values
     data.index
     # 切片功能
     data[1:3]
     # 自定义索引
     data_index1=pd.Series([0,1,2,3,4],index=['a','b','c','d','e'])
     data_index2=pd.Series({"a":1,"b":2,"c":3,"d":4,"e":5})
     # 显示索引，包括右边
     print(data_index1["a":"c"])
     # 隐式索引，不包含右边
     print(data_index2[1:2])
     # 创建标量数据
     data_scalar=pd.Series(5,index=range(5))
     print(data_scalar)

# index是一个不可变数组或有序集合
def create_index():
    ind=pd.Index([1,2,3,4])
    print(ind)
    # 具有集合操作属性
    # & | # 交集、并集、异或
    indA=pd.Index([1,2,3,4])
    indB=pd.Index([3,4,6,7])
    print(indA & indB)      
    
create_series()
create_index()