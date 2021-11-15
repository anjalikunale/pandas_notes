	# missing values and casting datatype
	
	## Missing Values

import pandas as pd
import numpy as np

people={"name":["anjali","sakshi","amruta","shruti",np.nan,None,"NA"],
				"last":["kunale","jatrate","kasar","mohare",np.nan,np.nan,"Missing"],
				"email":["anjali@gmail","sakshij@gmail","amruta@mail",None,"Missing","shreya@gmail","NA"],
				"age":[20,20,23,32,None,None,"Missing"]}

df=pd.DataFrame(people)

 #replace the NA and Missing string as null
df.replace({"NA":np.nan,"Missing":np.nan},inplace=True)
print(df)

print()
 #this will drop row if any column have null value
 #axis can be index or 0 for row
print(df.dropna(axis=0,how="any"))
print()
print(df.dropna(axis="index",how="any"))

 #drop row if and only if row contail all null values
print()
print(df.dropna(axis="index",how="all"))

 #drop column if all values are null
 #axis can be columns or 1 for column
print()
print(df.dropna(axis="columns",how="all"))

print()
print(df.dropna(axis=1,how="any"))

  #drop row if that has null value for email
print()
print(df.dropna(axis="index",how="any",subset=["email"]))

 #people must have either last name or email if both are null then drop that row

print(df.dropna(axis="index",how="all",subset=["last","email"]))

 #people must have both last name and email if any one value of last name or email is null then drop row

print(df.dropna(axis="index",how="any",subset=["last","email"]))

	#check wgere are null values
print(df.isna())

	#fill null values by missing string
print(df.fillna("Missing"))
	#you can fill null value by any string or any integer
print(df.fillna(0))	

	##Casting Datatype
print(df.dtypes)
	#average of age column	
print(df["age"].mean())