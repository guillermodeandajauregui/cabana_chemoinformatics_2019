import pandas as pd
import numpy as np
import scipy
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import manifold
from sklearn.decomposition import PCA
import bokeh as bk
from sklearn.preprocessing import StandardScaler

# load data

my_data = pd.read_csv("https://raw.githubusercontent.com/BarbaraDiazE/CABANA_CHEMOINFORMATICS/master/Day_3/UnsupervisedLearning_DimensionReduction/PCA/Databases_CABANA_2.csv", index_col=[0])


# normalize data
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64'] 
my_data_num = my_data.select_dtypes(include=numerics)

scaler = StandardScaler()
my_data_num_norm = pd.DataFrame(scaler.fit_transform(my_data_num), columns = my_data_num.columns)

#make pca
pca = PCA(n_components=3)
my_pca = pca.fit_transform(my_data_num_norm)

#join 
my_data = pd.concat([my_data, pd.DataFrame(my_pca)], axis=1)

