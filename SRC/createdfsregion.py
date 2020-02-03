#IMPORTs
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import Image
from functions import requestJSON


df = pd.read_csv("../OUTPUT/HDIrank2019_02_mergedDataframes.csv")
df = df.drop(columns="Unnamed: 0")

region = df.groupby("region").mean().drop(columns = ["HDIrank","LastYearRank"]).round(2)


gni = region.GNIperCapita.plot.bar(title="GNI per Capita", figsize=(8,9))
figgni = gni.get_figure()
figgni.savefig("../OUTPUT/region_GNIperCapita.png",bbox='tight')

pop = region.population.plot.bar(title="Population")
figpop = pop.get_figure()
figpop.savefig("../OUTPUT/region_population.png",bbox='tight')

ages = region.population.plot.bar(title="Life Expectancy")
figages = ages.get_figure()
figages.savefig("../OUTPUT/region_lifeExpectancy.png",bbox='tight')

index_reg = df.loc[:, ['Category','region']]
index_cat = pd.get_dummies(index_reg["Category"])
count = pd.concat([index_reg, index_cat], axis=1).reindex(index_reg.index)
count = count.loc[:, ['region','VERY HIGH HDI','HIGH HDI','MEDIUM HDI','LOW HDI']]
countdf = count.groupby("region").sum()
countdf["Total"] = index_reg.groupby("region").count()
newcol = ["HDI VeryHigh","HDI High","HDI medium","HDI Low"]
col = list(countdf.columns)
for ind,i in enumerate(newcol):
    countdf[i] = (countdf[col[ind]]/countdf["Total"]).round(2)

final = countdf.loc[:, ["HDI VeryHigh","HDI High","HDI medium","HDI Low"]]
end = final.plot.bar(title="HDI Distribution",stacked=True,color=["green","steelblue","orange","orangered"], figsize=(8,9))
fig = end.get_figure()
fig.savefig("../OUTPUT/region_HDIdistribution.png")