# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:56:20 2022

@author: lucas
"""
import pandas as pd
from itertools import combinations 

df = pd.read_excel("resultadosmega.xlsx")

df['Data'] = pd.to_datetime(df['Data'], format="%d/%m/%Y")

dataframe = df["resultado 1"].value_counts()

df2 = pd.DataFrame(dataframe)

df2 = df2.rename(columns={'resultado 1': 'numeroocorrencias'})

totalocorrencias1 = df2['numeroocorrencias'].sum()

df2['incidencia'] = df2.apply(lambda row: row.numeroocorrencias / totalocorrencias1, axis = 1)

# resultado 2

dataframe2 = df["Resultado 2"].value_counts()

df3 = pd.DataFrame(dataframe2)

df3 = df3.rename(columns={'Resultado 2': 'numeroocorrencias'})

df3['incidencia'] = df3.apply(lambda row: row.numeroocorrencias / totalocorrencias1, axis = 1)

# resultado 3

dataframe3 = df["Resultado 3"].value_counts()

df4 = pd.DataFrame(dataframe3)

df4 = df4.rename(columns={'Resultado 3': 'numeroocorrencias'})

df4['incidencia'] = df4.apply(lambda row: row.numeroocorrencias / totalocorrencias1, axis = 1)

# resultado 4

dataframe4 = df["Resultado 4"].value_counts()

df5 = pd.DataFrame(dataframe4)

df5 = df5.rename(columns={'Resultado 4': 'numeroocorrencias'})

df5['incidencia'] = df5.apply(lambda row: row.numeroocorrencias / totalocorrencias1, axis = 1)

# resultado 5

dataframe5 = df["Resultado 5"].value_counts()

df6 = pd.DataFrame(dataframe5)

df6 = df6.rename(columns={'Resultado 5': 'numeroocorrencias'})

df6['incidencia'] = df6.apply(lambda row: row.numeroocorrencias / totalocorrencias1, axis = 1)

# resultado 6

dataframe6 = df["Resultado 6"].value_counts()

df7 = pd.DataFrame(dataframe6)

df7 = df7.rename(columns={'Resultado 6': 'numeroocorrencias'})

df7['incidencia'] = df7.apply(lambda row: row.numeroocorrencias / totalocorrencias1, axis = 1)


#listas

lista = list(df2.index)
lista1 = lista[:1]


listb = list(df3.index)
lista2 = listb[:1]

listc = list(df4.index)
lista3 = listc[:1]

listd = list(df5.index)
lista4 = listd[:1]

liste = list(df6.index)
lista5 = liste[:1]

listf = list(df7.index)
lista6 = listf[:1]


listafinal = lista1 + lista2 + lista3 + lista4 + lista5 + lista6


comb = combinations(listafinal, 6)


for i in list(comb):
    print (i)

# probabilidade

listprob1 = list(df2['incidencia'])
lista11 = listprob1[0]

listprob2 = list(df3['incidencia'])
lista22 = listprob2[0]

listprob3 = list(df4['incidencia'])
lista33 = listprob3[0]

listprob4 = list(df5['incidencia'])
lista44 = listprob4[0]

listprob5 = list(df6['incidencia'])
lista55 = listprob5[0]

listprob6 = list(df7['incidencia'])
lista66 = listprob6[0]

probabilidade = lista11 * lista22 * lista33 * lista44 * lista55 * lista66




print(df2['incidencia'].plot(kind='bar'))
               
print(totalocorrencias1)

print(probabilidade)
