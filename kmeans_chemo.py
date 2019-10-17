#package import
import rdkit
import pandas as pd
import numpy as np
import scipy
import networkx as nx #if I want to play around with networks
import seaborn as sns
import matplotlib.pyplot as plt


#read data

my_data = pd.read_csv("https://raw.githubusercontent.com/BarbaraDiazE/CABANA_CHEMOINFORMATICS/master/Day_3/UnsupervisedLearning_Clustering/K_Means/Data_cluster.csv")

#select features
features = ['HBA', 'HBD', 'RB', 'LogP', 'TPSA', 'MW', 'Heavy Atom', 'Ring Count', 'Fraction CSP3']

#make data frame with only features

df = my_data[features]

sns.heatmap(df.corr())