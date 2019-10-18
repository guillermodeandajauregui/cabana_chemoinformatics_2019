#Linear regression
#Calculate IC50 from chemo-data

#load libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#read data
my_data = pd.read_csv("https://raw.githubusercontent.com/BarbaraDiazE/CABANA_CHEMOINFORMATICS/master/Day_4/Practices_in_Regressions_with_Python_Jupyter/QSAR/Bromodomain_Histone.csv", sep=";", index_col=[0])

#look at the data
my_data.head
my_data.columns.values

my_data["Test name"].unique()

#get the variables for regression

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64'] 
my_vars = my_data.select_dtypes(include=numerics).columns.values
my_vars = list(my_vars[1:]) #make it list for easier handling
my_vars.remove("Activity") #remove our target variable
my_vars

#heatmap for correlation evaluation

sns.heatmap(my_data[my_vars].corr())

#train split

X_train, X_test, y_train, y_test = train_test_split(my_data[my_vars], my_data["Activity"], test_size = 0.5, random_state=42)

#linear regression

lm = LinearRegression()
lm.fit(X_train, y_train)

#Inspect linear regression
lm.intercept_ #intercept, independent term linear model
lm.coef_ #estimated coefficients

#evaluate the model
lm.score(X_test, y_test)
lm.predict(X_test)[1:6]
y_test[1:6]
