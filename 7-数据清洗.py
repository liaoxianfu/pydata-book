# import numpy as np
# import pandas as pd
# # import tensorflow as tf
# from numpy import nan as NA

# # 创建数据
# string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])

# print(string_data)
# # 判断数据是否为NAN
# print(string_data.isnull())
# print(string_data.dropna())
# data = pd.Series([1, NA, 2, NA, 7])
# print(data)
# print("-------------")
# # print(data.dropna())
# # print(data)
# # print(data.notnull())
# data_notnull = data.dropna()
# # print(data_notnull)

# def data_not_null(data):

#     return data.dropna()

# # print(data_not_null(data))

# datas = [[1., 6.5, 3.], [1., NA, NA],
#          [NA, NA, NA], [NA, 6.5, 3.]]

# data1 = pd.DataFrame(datas)
# # print(data1)
# # print(data1.dropna())
# # print(data1.dropna(how='all'))
# # print(data1.dropna(axis=1,how='all'))
# # print()
# import numpy
# data = numpy.random.randn(7, 3)
# print(data)
# df = pd.DataFrame(data)
# print(df)
# df.iloc[:4, 1] = NA
# print(df)
# d1 = np.arange(3.)
# d2 = np.arange(6).reshape(3, 2)
# print(d2)
# print(d1)

# # 算数对齐
# print(pd.Series(np.arange(1, 6), index=['a', 'b', 'c', 'd', 'e']))
# print("dmeo")
# # 数据分析
# with open("README.md","r") as f:
#     a = f.read()
#     print(a)

import requests
reponse = requests.get("http://www.baidu.com")
# reponse.decode('gbk').encode('utf-8')
reponse.encoding = "utf-8"
print(reponse.text)
# str = reponse.text
# str.decode("gbk").encode("utf-8");
# print(str)