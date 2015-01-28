from pandas import Series, DataFrame
import pandas as pd
import numpy as np
#set up files
## creat a main directory
main_dir = "C:\Users\gabriel\Documents\GitHub\data" 
txt_file = "\File1_small.txt"
## join together 
main_dir+txt_file
# import data
pd.read_table(main_dir+txt_file, sep = " ")
##create a dataframe, df 
df=pd.read_table(main_dir+txt_file, sep = " ")
##extract rows 60 99 
df[60:100]
## extract values higher than 30

df[df.kwh>30]