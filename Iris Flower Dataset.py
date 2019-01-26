#Objective: Classify a new flower as belonging to one of the 3 classes(species) given the 4 features(Variables)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#'''downlaod iris.csv from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'''
#Load Iris.csv into a pandas dataFrame.
iris = pd.read_csv("iris.csv")







# (Q) how many data-points and features?
print('Number of datapoints are:')
print (iris.shape)
#(Q) What are the column names in our dataset?
print('features/Variables are :')
print (iris.columns)#variables








#2-D scatter plot:
print('DO you want to see 2D scatter plot?')
input()

iris.plot(kind='scatter', x='sepal_length', y='sepal_width') ;
plt.show()












#2d scatter plot with colour using seaborn library




print('Cannot make much sense out it. What if we color the points by thier class-label/flower-type ?')
sns.set_style("whitegrid");                             #Step1: Set the gird to white. #Step2: .FacetGrid(dataset,hue='',size=n)  #step3: .map(type,xLable,yLable)
sns.FacetGrid(iris, hue="species", size=4) \
   .map(plt.scatter, "sepal_length", "sepal_width") \
   .add_legend();                                       #step4:  .add_legend()
plt.show();
plt.close();










#Pair plots



print('We human are not able so 4-D plot we only can see 3D but plotting of 3D plots on paper is not convinient \n so we use Pair plots')
sns.set_style("whitegrid");               #Step1:Set the gird to white.
sns.pairplot(iris, hue="species", size=3);#.pairplot(dataset,hue='',size=n) function to plot pairplot
plt.show()

