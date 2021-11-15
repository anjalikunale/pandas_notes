	# Working with dates and time series data
import pandas as pd

df=pd.DataFrame({"Date":["2021-03-13 08-PM","2021-03-13 07-PM","2021-03-13 06-PM","2021-03-13 05-PM","2021-03-13 04-PM"],
								"Symbol":["ETHUSD","ETHUSD","ETHUSD","ETHUSD","ETHUSD"],
								"Open":[129.94,119.51,124.47,124.08,124.85],
								"High":[131.82,132.08,124.84,127.42,129.51],
								"Low":[126.71,126.56,119.51,121.55,124.08],
								"close":[129.56,124.08,121.23,122.08,124.08]})
								
print(df)

df.to_csv("pandas9.csv")
df2=pd.read_csv("pandas9.csv")
print(df2)

 #access specific data
print(df2.loc[0,"Date"])
 #acees it's day name
 #it will give an error as it is a string 
#print(df2.loc[0,"Date"].day_name())
 #it will also give an error bcz this format is unknown for pandas
#df2["Date"]=pd.to_datetime(df2["Date"])
df2["Date"]=pd.to_datetime(df2["Date"],format="%Y-%m-%d %I-%p")

 #now you can access day name bcz date is converted into datetime
print(df2.loc[0,"Date"].day_name())

print(df2["Date"])

print(df2["Date"].dt.day_name())