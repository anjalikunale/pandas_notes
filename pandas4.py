		 # pandas updating tows and columns
dic={"name":["anjali","sakshi","priya","neha","heena"],
				"last":["kunale","jatrate","sonavane","jadhav","khan"],
				"email":["anjalik8@gmail.com","sakshij7@gmail.com","priyas5@gmail.com","nehaj4@gmail.com","heebak6@gmail.com"]}

import pandas as pd

df=pd.DataFrame(dic)
print(df)

print(df.columns)
df.columns=["first_name","last_name","email_id"]
print(df.columns)

df.columns=[x.lower() for x in df.columns]

df.rename(columns={"first_name":"name"},inplace=True)
print(df)

df.rename(columns={"email_id":"email"}, inplace=True)

df.loc[2,"last_name"]="deshmukh"
print(df)

filt=(df["name"]=="heena")
df.loc[filt,"last_name"]="shaikh"
print(df)


df["name"]=df["name"].str.upper()
#print(df)
df["name"]=df["name"].str.lower()
print(df)

df["email"]=df["email"].str.capitalize()
print(df)

print(df["email"].apply(len))

df["name"]=df["name"].str.capitalize()

# apply explicit function
def update_name(name):
	return f"Miss.{name}"
	
df["name"]=df["name"].apply(update_name)
print(df)

#apply lambda function
df["last_name"]=df["last_name"].apply(lambda x: x.capitalize())
print(df)

#lenth of each emaid id in email column
print(df["email"].apply(len))
#how many riws are in each column
print(df.apply(len,axis="rows"))
#how many columns in each row
print(df.apply(len,axis="columns"))


#add salary column
#df.loc[:,["salary"]]=[500,600,300,700,330]
#print(df)

#find min of each column
print(df.apply(pd.Series.min))

#applymap applies function to each indivisual element of a fadataframe.. if there is integer column then we cannot apply string functions to this column and it will give an error
print(df.applymap(len))

#map works on a series, substitutes all values to new values, if we didn't substitute all values it will substitute remaining values to nan
def update_name(name):
	name=name.split(".")[1]
	return name.lower()
df["name"]=df["name"].apply(update_name)
print(df)
print(df["name"].map({"anjali":"angel","sakshi":"sejal","priya":"priyu"}))

#to overcome the above problem we should use replace method
df["name"].replace({"anjali":"angel","sakshi":"sejal","neha":"nehu"},inplace=True)
print(df)

filt=(df["name"]=="angel")
df.loc[filt,"email"]="angel@gmail.com"
print(df)