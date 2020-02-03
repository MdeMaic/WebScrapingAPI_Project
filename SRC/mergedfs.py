import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from bs4 import BeautifulSoup
import json
import requests
from IPython.display import Image
import os
from functions import requestJSON

print('Merging dataset and API in the same Dataframe...')
df1 = pd.read_csv("../OUTPUT/HDIrank2019_01_countryNameClean.csv")
df1 = df1.drop(columns="Unnamed: 0")

countries = requestJSON('https://restcountries.eu/rest/v2/all')
df2 = pd.DataFrame(countries)
col=['topLevelDomain','callingCodes', 'altSpellings' ,'latlng', 'demonym', 'area', 'gini', 'timezones', 'borders','nativeName', 'numericCode', 'currencies', 'languages', 'translations','regionalBlocs', 'cioc']
df2 = df2.drop(columns=col)

in_lst=[]
for name in df2.name:
    if name in list(df1.Country):
        in_lst.append(True)
    else:
        in_lst.append(False)
df2["In_lst"]=in_lst
df2 = df2[df2["In_lst"]==True]

df2 = df2.sort_values("name").reset_index(drop=True)
df1 = df1.sort_values("Country").reset_index(drop=True)
df = pd.concat([df1, df2], axis=1).reindex(df1.index)

if not df['Country'].equals(df['name']):
    print("FAIL, Country names are not cleaned.")
else:

    df = df.drop(columns=["name","In_lst"])
    df = df.sort_values("HDIrank").reset_index(drop=True)
    df.to_csv("../OUTPUT/HDIrank2019_02_mergedDataframes.csv")
    print("DataFrame: 'HDIrank2019_02_mergedDataframes.csv' created succesfully ")