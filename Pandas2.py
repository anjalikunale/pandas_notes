'''
		# pandas in python

• Faster indexing
• Easy for data analysis
• Open sourse liabrary
• python functions can apply on it
• analies big data easily
• use the power and speed of numpy to
make data analysis and processing easy for data scientist
'''
import numpy as np
import pandas as pd

dict1={"Names":["Anjali","Sakshi","Priya","Shreya"],
			 "Marks":[95,92,90,88],
			 "City":["Lohara","Narande","Solapur","Kolhapur"]
}
df=pd.DataFrame(dict1)
print(df)

 #export this data frame into csv
df.to_csv("pandas2.csv")
df.to_csv("pandas2_index_false.csv",index=False)

 #read csv file using pandas
data=pd.read_csv("pandas2.csv")
print(data)

 #read csv file
content=pd.read_csv("pandas3.csv")
print(content)
 
 #change indexing
content.index=["first","second","third","fourth"]
print(content)

 #view data 
 #first two rows
print(df.head(2))
 #last two rows
print(content.tail(2))

 #statistical analysis ofnumeric columns
print(content.describe())

'''
PANDAS DATA STRUCTURE:
	Series: one dimentional array containing one column or 
	row of data in data frame
	
	DataFrame: dataframe looks like excel sheet or		spradsheet
'''
 #series : syntax - pd.Series(np.random.rand(rows no))
ser=pd.Series(np.random.rand(34))
#print(ser)
#print(type(ser))

 #dataframe
newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
#print(newdf)
#print(type(newdf))
#print(newdf.columns)
#print(newdf.index)
#print(newdf.dtypes)
#print(newdf.T)
#print(newdf.describe())
#print(newdf.to_numpy())
#print(newdf.head(12))
#print(newdf.tail())

#print("~~~~~"*10)
# #sor by index i.e rows
#print(newdf)
#print(newdf.sort_index(axis=0,ascending=False))

# #sort by columns
#print(newdf.sort_index(axis=1,ascending=False))

# #change column names
#newdf.columns=["A","B","C","D","E"]
#print(newdf)

# #make a copy of dataframe
#newdf2=newdf
#'''
#this will return view of dataframe that means if changed the element of dataframe2 it will automatically changes the element of previous dataframe
#'''
#newdf2=newdf.copy()
#newdf2.loc[0,"A"]=95
#print(newdf)
#print(newdf2)

#newdf2.loc[0,0]=950  #creats new column 
#print(newdf2)  

# #inplace effects on origional dataframe
#newdf2.drop(0,inplace=True) #drops row
#print(newdf2)

#newdf2.drop(0,axis=1,inplace=True)
#print(newdf2)

# # Access set of columns and rows
#print(newdf.loc[[0,3],["A","B","D"]])
# # Access all columns
#print(newdf.loc[[0,3],:])
# # Access all rows
#print(newdf.loc[:,["A","B","C"]])

# # Arithmetic operations
#print(newdf.loc[(newdf["A"]>0)] )

# #iloc df.iloc[row index. colm index]
#print(newdf.iloc[0,4])  #access specific element
#print(newdf.iloc[0])     #acess 0th row
#print(newdf.iloc[:,[0]])  #access 0th column

# #drop row and column
#print(newdf.drop([0])) #drops a 0th row
#print(newdf.drop(["A"],axis=1))  #drops A column

# #Above two operations doesn't affects on otigionak df
#print(newdf)
# #to apply above two conditions use inolace=True
#newdf.drop([0],inplace=True)
#newdf.drop([5],inplace=True)
#print(newdf.head())
# #we droped a 0th & 5th row that's why we should reindex 
#newdf.reset_index(inplace=True) #returns new and old indixes
#print(newdf)

newdf.reset_index(drop=True,inplace=True)#drops old index
print(newdf)

# #make null column to "B"
#newdf.loc[:,[2]]=None
#print(newdf)
#print(newdf.isnull())
#print(newdf.notnull())


df=pd.DataFrame({"name":["anjali","sakshi","anjali"],
								  "age":[np.nan,20,21],
								  "city":[np.nan,np.nan,np.nan]})

print(df)
print()
print()
'''
 #dropna() :
 	how: ("any","all", bydefault:"any")
 	 1. any - if any element is none then drop whole row/column
 	  2. all - if all elements of row or column are none then drop whole row or column
 '''
#df.dropna(inplace=True)  #take axis=1 to drop column
#print(df)	  
#df.dropna(how="all",axis=1,inplace=True)    
#print(df)   

'''
 drop_duplocates :
 	keep : ("first","last","False", bydefault : "first")  
 '''
df.drop_duplicates(subset=["name"],keep="last",inplace=True)
print(df)

print(df.shape)
print(df.describe())
print(df.info())
print(df["name"].value_counts())