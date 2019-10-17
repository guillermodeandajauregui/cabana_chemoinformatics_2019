#package import
import rdkit
import pandas as pd
import numpy as np
import scipy
import networkx as nx #if I want to play around with networks
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#read data

my_data = pd.read_csv("https://raw.githubusercontent.com/BarbaraDiazE/CABANA_CHEMOINFORMATICS/master/Day_3/UnsupervisedLearning_Clustering/K_Means/Data_cluster.csv")

#select features
features = ['HBA', 'HBD', 'RB', 'LogP', 'TPSA', 'MW', 'Heavy Atom', 'Ring Count', 'Fraction CSP3']

#make data frame with only features
df = my_data[features]

#check correlation (Pearson) of features
df.corr()
sns.heatmap(df.corr()) #you can see some features are 

#scatter plots of two variables vs MW
sns.set_style("whitegrid")
sns.lmplot("LogP", "MW", data=my_data, hue="Library", palette="cool", fit_reg = False, size=6, aspect=1)
sns.lmplot("TPSA", "MW", data=my_data, hue="Library", palette="cool", fit_reg = False, size=6, aspect=1)

#prepare kmeans clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

