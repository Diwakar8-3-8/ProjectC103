import pandas as pd
import plotly.express as pe

df=pd.read_csv("data.csv")
fig=pe.bar(df,x="Country",y="InternetUsers")
fig.show()