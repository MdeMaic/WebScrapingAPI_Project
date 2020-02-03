#IMPORTs
import pandas as pd
import re
from functions import requestJSON

print("Cleaning the initial dataset and matching country names...")
df = pd.read_csv("../INPUT/HDI_country_ranking_2019.csv",sep=";")
df = df.rename(columns={
                        "HDI rank":"HDIrank"
})

#Replace "," by "." and make them float values.
numcol = ["HDI","LifeExpectancy","ExpectedSchoolingYears","MeanSchoolingYears"]
for i in numcol:
    df[i]=df[i].str.replace(',','.')
    df[i] = pd.to_numeric(df[i])

#Remove european thousand DOT from GNIperCapita
for i in df.GNIperCapita:
    if i > 100:
        df = df.replace({'GNIperCapita': i}, i/1000)
#Remove dot
df.GNIperCapita = df.GNIperCapita * 1000
#Cast
df = df.astype({'GNIperCapita': 'int32'})

#ensure HDI < 1
for i in df['HDI']:
    if i < 1:
        df = df.replace({'HDI': i}, i*1000)

df.HDI = df.HDI/1000
df.HDI = df.HDI.round(3)
#Cast
df = df.astype({'HDIrank':'str', 'LastYearRank':'str'})

df.to_csv("../OUTPUT/HDIrank2019_00_initialClean.csv")

## Matching missing names between both sources
countries = requestJSON('https://restcountries.eu/rest/v2/all')
lista_name = [cm["name"] for cm in countries]

def missedCountries():
    found=[]
    for ind,value in enumerate(df.Country):
        for elem in lista_name:
            if value == elem:
                found.append(ind)
    nofound=[]
    for i in range(189):
        if i not in found:
            nofound.append(i)
    noname=[]
    for i in nofound:
        noname.append(df.Country[i])
    
    if len(nofound) == 0:
        return "No values lost"
    else:
        return list(zip(nofound,noname))

nocountries = missedCountries()

def countryMatch(regex,lst):
    chances=[]
    for i in lst:
        if re.match(f"{regex}",i):
            chances.append(i)
    return chances

countryMatch("\wong.+",lista_name)

#Matching the list of missed country names using countryMatch function

lst = ['Hong Kong','United Kingdom of Great Britain and Northern Ireland','United States of America', 'Czech Republic','Macedonia (the former Yugoslav Republic of)','Palestine, State of','Swaziland','Tanzania, United Republic of']
for i in range(len(lst)):
    df = df.replace({'Country': nocountries[i]}, lst[i])

now = missedCountries()
if now == "No values lost":
    df.to_csv("../OUTPUT/HDIrank2019_01_countryNameClean.csv")
    print("Cleaned successfully in 'HDIrank2019_01_countryNameClean.csv'")
else:
    print(now, "Check the cleaning data")