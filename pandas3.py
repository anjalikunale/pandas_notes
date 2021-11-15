	#pandas filtering

people={"name":["anjali","sakshi","priya","neha","heena"],
				"last":["kunale","jatrate","sonavane","jadhav","khan"],
				"email":["anjalik8@gmail.com","sakshij7@gmail.com","priyas5@gmail.com","nehaj4@gmail.com","heebak6@gmail.com"]}

import pandas as pd
df=pd.DataFrame(people)
print(df)

filt=(df["last"]=="kunale")
print(df.loc[filt])
    #OR
print(df.loc[df["last"]=="kunale"])

	#filt=df["name"]=="anajli" or df["last"]=="sonavane"
	#print(df.loc[filt])

	#add one more column to dataframe
df.loc[:,["country"]]=["india","united states","united kingdom","united states","getmany"]
print(df)
	
	#delete email column
df.drop(["email"],axis=1,inplace=True)
print(df)
	
	#add programming language column
df.loc[:,["programming"]]=["python;sql","c;c++;java","java;c;python","c#;ruby;r","java;python"]
print(df)

countries=["india","united states"]
filt1=df["country"].isin(countries)
print(df.loc[filt1,["name","country"]])

filt2=df["programming"].str.contains("python")
print(df.loc[filt2,["programming","name"]])
	#OR
print(df[filt2])

filt3=(df["name"]=="anjali") | (df["last"]=="jatrate")
print(df.loc[filt3])