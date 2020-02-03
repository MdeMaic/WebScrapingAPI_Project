#IMPORTs
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import Image
from SRC.functions import requestJSON
from fpdf import FPDF

def createRegion():

    df = pd.read_csv("OUTPUT/HDIrank2019_02_mergedDataframes.csv")
    df = df.drop(columns="Unnamed: 0")

    reg = df.groupby("region").mean().drop(columns = ["HDIrank","LastYearRank"]).T.round(2)

    print(reg)

    region = reg.T
    print("\nGenerating images....")
    gni = region.GNIperCapita.plot.bar(title="GNI per Capita", figsize=(8,9))
    figgni = gni.get_figure()
    figgni.savefig("OUTPUT/region_GNIperCapita.png",bbox='tight')

    pop = region.population.plot.bar(title="Population")
    figpop = pop.get_figure()
    figpop.savefig("OUTPUT/region_population.png",bbox='tight')

    ages = region.population.plot.bar(title="Life Expectancy")
    figages = ages.get_figure()
    figages.savefig("OUTPUT/region_lifeExpectancy.png",bbox='tight')

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
    fig.savefig("OUTPUT/region_HDIdistribution.png")
    print("\nImages created succesfully :)\n")
    
    pdf = FPDF('P','mm','A4')
    pdf.add_page()
    font_type = ('Arial', 'B', 16)
    num_col = len(reg.columns)
    w,h=190,277
    pdf.set_font(*font_type)
    pdf.set_text_color(0)
    pdf.set_draw_color(0)
    pdf.cell(w,10,'Datos Acumulados',1,1,'C')
    pdf.set_line_width(0.2)
    for col in reg.columns:
        pdf.cell(w/num_col,10,col,1,0,'C')
    pdf.ln()
    pdf.set_fill_color(243,95,95)
    font_type = ('Arial', '', 12)
    pdf.set_font(*font_type)

    for _,row in reg.iterrows():
        fill = 0
        if row["country"] in european_countries:
            fill = 1
        # iterating columns
        for value in reg.columns:
            pdf.cell(w/num_col,10,fit_word(row[value],w/num_col,font_type),1,0,'C',fill)
        pdf.ln()
    pdf.output("archivo.pdf",'F')
    
    return "Happy"

def filterRegion(min,max):
    
    df = pd.read_csv("OUTPUT/HDIrank2019_02_mergedDataframes.csv")
    df = df.drop(columns="Unnamed: 0")

    reg = df.groupby("subregion").mean().drop(columns = ["HDIrank","LastYearRank"]).round(2).sort_values("HDI")
    reg = reg.loc[:, ['HDI','LifeExpectancy','GNIperCapita','population']]
    reg_filtered = reg[reg["HDI"]>=float(min)]
    reg_filtered = reg_filtered[reg_filtered["HDI"]<=float(max)]
    reg_filtered

    print("----------------------- HDI between:",min,"&",max,"------------------------")
    print(reg_filtered)
    print("---------------------------------------------------------------------------")
    return reg_filtered

    
    pdf = FPDF('P','mm','A4')
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 16)
    