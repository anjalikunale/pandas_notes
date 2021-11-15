		#sorting in pandas

import pandas as pd	
df=pd.DataFrame({"name":["anjali","sakshi","sejal","suchita"],
									"last":["kunale","jatrate","shaha","jatrate"],
									"city":["achaler","narande","solapur","benglore"]})

	#sort by columns valuse
(df.sort_values(by=["last","name"],ascending=[False,True],inplace=True))
print(df)

 #sort by index
#(df.reset_index(drop=True,inplace=True))
print(df.sort_index(ascending=False))
print(df)

	#sort by values
print(df["city"].sort_values(ascending=True))