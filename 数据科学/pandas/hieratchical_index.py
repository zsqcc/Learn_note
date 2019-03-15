# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:31:55 2019
层级索引(hierarchical indexing)
@author: shuquan.zhang
"""
import pandas as pd
import numpy as np

def hierarchical_index():
    # 之前的知识建立三维数组，筛选数据时非常不方便
    area_info=[('California', 2000), ('California', 2010),('New York', 2000), 
           ('New York', 2010),('Texas', 2000), ('Texas', 2010)]
    populations=[33871648, 37253956,18976457, 19378102,20851820, 25145561]
    # 使用dataframe的方式创建数据
    pop_dataframe=pd.DataFrame(populations,index=area_info)
    pop=pd.Series(populations,index=area_info)
    print(pop)
    # 需要使用python语法糖(列表解析式)进行筛选
    print(pop[[i for i in pop.index if i[1]==2010]])
    # 创建多级索引
    index=pd.MultiIndex.from_tuples(area_info)
    # 索引重置为MultiIndex
    pop_multi=pop.reindex(index)
    print(pop_multi)
    # 使用pandas正常切片的方式获得2010年的数据
    print(pop_multi[:,2010])
    print("初始数据")
    print(pop_dataframe)
    # 使用unstack方法，将多级索引回退
    print("原版经过索引重置的数据")
    print(pop_multi)
    pop_unstack=pop_multi.unstack()
    # 将索引重置的数据转化为普通dataframe数据
    print(pop_unstack)
    # 使用stack()将普通dataframe数据转换为索引重置的数据
    pop_stack=pop_unstack.stack()
    print(pop_stack)
    # 给已经重置索引的数据，可以轻松增加一列
    pop_df=pd.DataFrame({'total':pop_multi,'under18':[9267089, 9284094,4687374, 4318033,5906301, 6879014]})
    print(pop_df)
    # 计算
    print("计算")
    f_u18=pop_df['under18'] / pop_df['total']
    print(f_u18)
    print(f_u18.unstack())

def multi_index():
    # 多级索引的创建
    df_mul=pd.DataFrame(np.random.rand(4, 2),index=[['a', 'a', 'b', 'b'],
                    [1, 2, 1, 2]],columns=['data1', 'data2'])
    print(df_mul)
    data={('California', 2000): 33871648,('California', 2010): 37253956,
          ('Texas', 2000): 20851820,('Texas', 2010): 25145561,
          ('New York', 2000): 18976457,('New York', 2010): 19378102}
    print(pd.Series(data))
    # 显式创建多级索引:通过数组组成的列表创建MultiIndex
    print(pd.MultiIndex.from_arrays([['a','a','b','b'],[1,2,1,2]]))
    # 通过包含多个索引值的元组构成的列表创建MultiIndex
    print(pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)]))
    # 使用笛卡儿积的方式创建
    print("使用笛卡尔积的方式")
    print(pd.MultiIndex.from_product([['a','b'],[1,2]]))
    d=pd.MultiIndex.from_product([['a','b'],[1,2]])
    print(pd.DataFrame(d))
    # 使用levels和labels的方式
    print("使用levels和labels的方式")
#    print(pd.MultiIndex(levels=[['a','b'],[1,2]],labels=[[0,0,1,1],[0,1,0,1]]))
    # 隐式创建索引
    print(pd.Index([("A","x1"),("A","x2"),("B","y1"),("B","y2"),("B","y3")],name=["class1","class2"]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




hierarchical_index()
multi_index()