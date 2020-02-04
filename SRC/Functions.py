#IMPORTs
import pandas as pd
import numpy as np
import matplotlib as plt
import re
from bs4 import BeautifulSoup
import json
import requests
from IPython.display import Image
import os

#Request API function
def requestJSON(url):
    res = requests.get(url)
    if res.status_code != 200:
        print(res.text)
        raise ValueError("Bad Response")
    return res.json()

#Cleaning function. Merge API and DATASET.
def missedCountries(df):
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



