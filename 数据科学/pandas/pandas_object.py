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
     # Series对象只保存显示定义的键值对
     data_t=pd.Series({2:'a',3:'g',1:'h'},index=[2,3,4])
     print(data_t)

# DataFrame是具有灵活的行索引及灵活列名的二维数组
# 可看作多个Series累加
def create_dataframe():
    area_dict={"c":333,"b":555,"f":998}
    area=pd.Series(area_dict)
    popu_dict={"c":3303,"b":5505,"f":9908}
    popu=pd.Series(popu_dict)
    # 此dataframe为二维数组,colume为列索引，index为行索引
    states=pd.DataFrame({"area":area,"popu":popu})
    print(states)
    print(states.index)
    print(states.columns)
    print(states["area"]["c"])
    
        
    ind=pd.Index([1,2,3,4])
    print(ind)
    indA=pd.Index([1,2,3,4])
    indB=pd.Index([3,4,6,7])
    print(indA & indB)      

create_dataframe()    
create_series()
