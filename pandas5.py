	# Add/Remove rows and columns
import pandas as pd	
df=pd.DataFrame({"name":["anjali","sakshi","sejal"],
									"last":["kunale","jatrate","shaha"],
									"city":["achaler","narande","solapur"]})

df["full name"]=df["name"]+" "+df["last"]
df.drop(columns=["name","last"],inplace=True)
print(df)

df[["first","last"]]=(df["full name"].str.split(" ",expand=True))

	#add new row
print(df.append({"first":"shreya"},ignore_index=True))
print(df)


	#add new data frame / two new rows
df2=pd.DataFrame({"first":["shreya","neha"],
			"last":["jadhav","upase"],
			"city":["pandharpur","shegaon"]})
			
print(df.append(df2,ignore_index=True))
df=df.append(df2,ignore_index=True)
print(df)

	#remove rows
print(df.drop(index=[3,2]))

filt=((df["first"]=="shreya") | (df["first"]=="neha"))
print(df.drop(index=df.loc[filt].index))

