from sklearn.cluster import KMeans
from sklearn import  preprocessing
import pandas as pd
import  numpy as np
import sys
import csv
#输入数据
data=pd.read_csv('./data.csv',encoding='gbk')
train_x=data[['2019年国际排名','2018世界杯','2015亚洲杯']]
df=pd.DataFrame(train_x)
kmeans=KMeans(n_clusters=3)
#规范化到【0,1】
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
kmeans.fit(train_x)
predict_y=kmeans.predict(train_x)
#合并聚类结果，插入到原始数据
result=pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类'},axis=1,inplace=True)
#将结果写入CSV文件
filename='result.csv'
df=pd.DataFrame(result)
df.to_csv(filename)