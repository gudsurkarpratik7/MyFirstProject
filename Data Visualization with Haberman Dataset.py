import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#readin the dataset into a dataframe


haberman =pd.read_csv('haberman.csv')

print('_________________________________________________________________________________________')
print('How many data points the given datasets have?')
shape=haberman.shape
print('The dataset has',shape[0],'entries/rows and ',shape[1],'coloums/features')
print('')
print('_________________________________________________________________________________________')
print('What are the Features or Variables the dataset have ?')
feature=haberman.columns
i=1
for ele in feature:
    if(i==4):
        print(i, '.', ele," : This is also called as class label")
        break
    print(i,'.',ele)
    i+=1

''' Feature or Variables or Columns Information 
1. Age of patient at time of operation (numerical) 
2. Patient's year of operation (year - 1900, numerical) 
3. Number of positive axillary nodes detected (numerical) 
4. Survival status (class attribute) 
-- 1 = the patient survived 5 years or longer 
-- 2 = the patient died within 5 year

'''
print('_________________________________________________________________________________________')
print('Data points Per class')
print(haberman["status"].value_counts())
print('Observation: This is a inbalanced dataset')
print('_________________________________________________________________________________________')

#objective: To predict wheather patient will survive or not baased on the current age provided, the year of operation and
# number of cancer nodes detected in his body during dialysis


#Univariate Analysis
print('2D scatter plot :')
haberman.plot(kind='scatter', x='age', y='nodes') ;
plt.show()

print('Pair Plots:')
sns.set_style('whitegrid')
sns.FacetGrid(haberman,hue='status',height=4)\
   .map(plt.scatter,'age','nodes')\
   .add_legend();
plt.show();
plt.close();
#obeservation :1.It is complex to seperate status1 and status2 patient from each other as they are spread across the
#range of age unevenly
#2.Age and nodes parameters are not sufficient to classify them

#PDF/hstogram:(PDF is smoothed histogram)
sns.FacetGrid(haberman,hue='status',size=5)\
    .map(sns.distplot,'age')\
    .add_legend();
plt.show()

sns.FacetGrid(haberman,hue='status',size=5)\
    .map(sns.distplot,'year')\
    .add_legend();
plt.show()

sns.FacetGrid(haberman,hue='status',size=5)\
    .map(sns.distplot,'nodes')\
    .add_legend();
plt.show()

#CDF


#Bivariate:Pair Plots
sns.set_style("whitegrid");               #Step1:Set the gird to white.
sns.pairplot(haberman, hue="status",vars=['age','year','nodes'] ,height=2);#.pairplot(dataset,hue='',size=n) function to plot pairplot
plt.show()


#observation:Year of tratement and number of  nodes are  the 2 parameteres that shows better seperation that others
#Git Push Check 
