	#Grouping Aggregating - Analyzing and Exploring

import pandas as pd
import numpy as np

df=pd.DataFrame({"name":["a","b","c","d","e","b","c"],
								"last":["l","m","n","o","p","l","m"],
								"city":["x","y","z","x","y","y","z"],
								"age":[20,23,19,30,27,20,19],
								"code":["yes","yes","no","yes",np.nan,"no",np.nan],
								"social media":["yt","insta","yt","wp","yt","insta","wp"],
								"language":["python;java;c","c;c++;python;ruby","java;c","java;c++","python;sql;html;css","java;html;css;javascript","sql;mysql;html"],
								"salary":[500,300,200,500,300,600,200]})
#pd.set_option("display.max_columns",5)
#pd.set_option("display.max_rows",5)

print(df)


print(df["name"].count())
print(df["code"].count())
print(df["code"].value_counts())
print(df["last"].value_counts())												
print("median is ",df["salary"].median())	
print(df[["age","salary"]].median())

 #check social media counts how many uses social media and which
print(df["social media"].value_counts())
 #check percentage if use if social media
print(df["social media"].value_counts(normalize=True))

'''
	#Group by : 1.split a object
						  2. apply a function
						  3.combine results	
'''

						  										
grp=df.groupby(["city"])
print(grp.get_group("y"))
 #get all groups 
print(grp["social media"].value_counts())
	#get specific group
print(grp["social media"].value_counts().loc["x"])


 #search a median of all city salary 
print(grp["salary"].median())
 #search a median of specific city salary
print(grp["salary"].median().loc["y"])

 #aggregate the all cities median mean
print(grp["salary"].agg(["median","mean"]))

 #find the median salary and mean salary for y

print(grp["salary"].agg(["median","mean"]).loc["y"])

filt=df["city"]=="y"
print(df.loc[filt,"code"])

filt=df["city"]=="y"
print(df.loc[filt,"language"].str.contains("python").sum())

 #use gruop by variable
print(grp["language"].apply(lambda x : x.str.contains("python").value_counts(normalize=True)))


