#IMPORTs
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image
from functions import requestJSON


df = pd.read_csv("../OUTPUT/HDIrank2019_02_mergedDataframes.csv")
df = df.drop(columns="Unnamed: 0")

no_top = list(range(10,179))
lst=[]
for i in range(189):
    if i in no_top:
        lst.append(False)
    else:
        lst.append(True)

df['inlst'] = lst
top = df[df['inlst']==True]
top = top.reset_index(drop=True)
top = top.drop(columns="inlst")
top_mean = top.groupby(['Category']).mean().drop(columns = ["HDIrank","LastYearRank"]).T.round(2)

top.to_csv("../OUTPUT/HDIrank2019_03_TopUpandDown.csv")
top_mean.to_csv("../OUTPUT/HDIrank2019_04_TopUpandDownMean.csv")
