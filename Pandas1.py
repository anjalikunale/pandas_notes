import pandas as pd
import numpy as np

	#create series
#s=pd.Series([1,2,3,4,5,6,7,np.nan,np.nan,8,9])
#print(s)

	#create date range
d=pd.date_range("20211101",periods=10)
print(d)

	#create dataframe
df=pd.DataFrame(np.random.randn(10,4),index=d,		columns=["A","B","C","D"])
print(df)

		#Create dataframe using dictionary and series
#df1=pd.DataFrame({"A":[1,2,3,4],
#									"B":pd.date_range("20211101",periods=4),
#									"C":pd.Series(1,index=list(range(4)),dtype="float32"),
#									"D":np.array([5]*4,dtype="int32"),
#									"E":(["True","False","True","True"]),
#									"F":(["Anjali","neha","shital","sherya"])})
#									
#print(df1)

	#check datatype of all columns
#print(df1.dtypes)

	##How to view Data:
	
	#view first five rows and last five rows
#print("First five rows: ")
#print(df.head())

#print("Last five rows :")
#print(df.tail())

#	#view specific rows
#print("First three rows :")
#print(df.head(3))

#print("Last two rows :")
#print(df.tail(2))

#	#view index values
#print("all values of index :")
#print(df.index)

#	#print all columns name
#print("columns name :")
#print(df.columns)

#	#represent dataframe as numpy
#print("representation of dataframe as numpy :")
#print(df.to_numpy())

#	#more info about dataframe data
#print("more info about data :")
#print(df.describe())

#	#sord df data by index
#print(df.sort_index(axis=1,ascending=False))

#	#sort df data by column 'C'
#print(df.sort_values(by="C"))

#	#print all values of column C
#print("column c values :")
#print(df['C'])

#	#print first three rows
#print("first three rows :")
#print(df[0:3])

#	#print specific piece of df
#print("specific piece of df :")
#print(df[2:6])

#	#print data by lables
#print("prints data by lables :")
#print(df.loc[d[0]])

#	#select multi axes using lables
#print("multi axes using lables :")
#print(df.loc[:,['D','C']])

#print("multi axes using lables :")
#print(df.loc['20211103':'20211106',["D","A"]])

#	#most imp fun to view data
#	#syntax: df_name.iloc[s_r_i:e_r_i,s_c_i:e_c_i]
#print(df.iloc[2:6,1:4])

#	#Arithmetic operations on dataframe
#print("Print those values which are greater than zero in column A")
#print(df[df['A']>0])

#	##Habdling missing data from dataframes

#	#Reindex previous dataframe

#df2=df.reindex(index=d[0:4],columns=list(df.columns)+["E"])
#df2.loc[d[0]:d[1],"E"]=1
#print(df2)
#check where null values are present in dataframe
#print(df2.isnull())	  #first way
#print(pd.isna(df2)) #another way
#drop the rows where null vaules exist
#print(df2.dropna())
#fill new value to null values i.e fill missing data
#df2=df2.fillna(value=2)
#print(df2)

#	##Pandas operations

#	#Desciptive statistics operations

#print(df.mean())	#mean of all columns
#print(df.mean(1)) #mean of all rows

#s1=pd.Series([1,2,3,np.nan,4,5,6,7,8,9],index=d).shift(2)
#shift(2) will shifts last two values
#print(s1)
#print(df.sub(s1,axis="index"))

#	#Applying functions to the data
#print(df.apply(np.cumsum))
#print(df.apply(np.abs)) #removes -ve sign
#  #subtract min from max of a column by using lambda
#print(df.apply(lambda x: x.max()-x.min()))

#	#string processing operations
#s2=pd.Series(["python","jupyter",np.nan,"pandas","numpy"])
#print(s1)
#print(s2.str.upper())

#	#Histogramming
#print(s1.value_counts())

#	##Merging, Grouping, Reshape Data
#	#Merging

#df=pd.DataFrame(np.random.randn(10,4))
#print(df)

#df2=[df[:3],df[3:7],df[7:]] #three dataframes
#print(df2)
#	#now concat those three dataframes
#print(pd.concat(df2))

#	#left merging right merging

#left=pd.DataFrame({"A":[1,2],"B":[3,4]})
#right=pd.DataFrame({"C":[1,7],"B":[4,5]})
#print(left)
#print(right)
#	#merge left and right dataframe
#print(pd.merge(left,right,on="B"))

#	#>>stack
#my_tuple=list(zip(*[[1,2,3,4,5,6],[7,8,9,10,11,12]]))
#index=pd.MultiIndex.from_tuples(my_tuple,names=["first","second"])
#df=pd.DataFrame(np.random.randn(6,2),index=index,columns=["A","B"])
#print(df)

#	#make a stack
#a=df.stack()
#print(a)

#	#unstack it
#a=a.unstack()
#print(a)

#	#>>Pivot table
#df=pd.DataFrame({"A":["a","b","c","d"]*3,
#								 "B":["A","B","C"]*4,
#								 "C":["P","P","P","Q","Q","Q"]*2,
#								 "D":np.random.randn(12),
#								 "E":np.random.randn(12)})
#print(df)
#print(pd.pivot_table(df,values="D",index=["A","B"],columns=["C"]))

		##TimeSeries and catagoticals

	#Time Series
dates=pd.date_range("3/3/2021",periods=100,freq="S")
#print(dates)
ts=pd.Series(np.random.randint(0,500,len(dates)),dates)
#print(ts)

	#timezone representation
dates=pd.date_range("3/3/2021",periods=5,freq="S")
#print(dates)
ts=pd.Series(np.random.randn(len(dates)),dates)
print(ts)

	#utc timezone
ts_utc=ts.tz_localize("UTC")
print(ts_utc)

	#covert into another timezone
ts_us=ts_utc.tz_convert("US/Eastern")
print(ts_us)

	#convert into timestamp representation
dates=pd.date_range("1/11/2021",periods=5,freq="M")
ts=pd.Series(np.random.randn(len(dates)),dates)
print(ts)

	#convert into period
ps=ts.to_period()
print(ps)

	#convert to timestamp
ts=ps.to_timestamp()
print(ts)

import matplotlib.pyplot as plt
plt.close("all")
ts=pd.Series(np.random.randn(500),
						index=pd.date_range("1/11/2021",periods=500))
ts=ts.cumsum()
print(ts.plot())