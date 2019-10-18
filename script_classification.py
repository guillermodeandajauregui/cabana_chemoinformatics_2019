#Linear regression
#Calculate IC50 from chemo-data

#load libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#read data
my_data = pd.read_csv("https://raw.githubusercontent.com/BarbaraDiazE/CABANA_CHEMOINFORMATICS/master/Day_4/Supervised_Learning_Classifications/SVM/Data/Data_SVM.csv", sep=",", index_col=[0])

#look at the data
my_data.head
my_data.columns.values

#predict druglikeliness

##Drug-likeness encoded in "Drug Like"
my_data["Drug Like"].unique()

#select numeric variables
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64'] 
my_vars = list(my_data.select_dtypes(include=numerics).columns.values)
my_vars.remove("Drug Like") #remove our target variable

sns.heatmap(my_data[my_vars].corr())

#remove highly correlated measures
#pending
#my_data[my_vars].corr().index[>0.8]


#split test and training data

X_train, X_test, y_train, y_test = train_test_split(my_data[my_vars], my_data["Drug Like"], test_size = 0.5, random_state=42)

# make svm
svf_rbf = SVC(C=1.0, kernel='rbf')

svf_rbf.fit(X_train, y_train)

#Evaluate with test data
svf_rbf.score(X_test, y_test)
sk.metrics.confusion_matrix(y_test, svf_rbf.predict(X_test))

#Make Decision tree

my_tree = DecisionTreeClassifier(criterion="gini", max_leaf_nodes=8)

my_tree.fit(X_train, y_train)

#Evaluate

my_tree.score(X_test, y_test)
sk.metrics.confusion_matrix(y_test, my_tree.predict(X_test))
