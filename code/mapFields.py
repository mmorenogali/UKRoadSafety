import pandas as pd
import os
import gc
import time
import xlrd

# Ahora procesaremos los datos de tal modo que convertiremos los
# datos numéricos categóricos en las categorías que se muestran en 
# el archivo "variable lookup.xls"


# Leemos los datos unidos:
allData = pd.read_csv("allData.csv",sep = ";")

# Leemos también el archivo con las variables. Cada pestaña es el nombre de 
# la columna, y tiene dos campos: code y label. Lo que queremos hacer es
# reemplazar los valores de code por los de label en cada columna:
xls = xlrd.open_workbook(r'variable lookup.xls', on_demand=True)

# Tomamos todos los nombres de las columnas:
columnasXls = xls.sheet_names()

# El único problema es que los nombres de las páginas están separados por 
# espacios y los del dataset por "_". También por minúsculas. Lo cambiaremos:
columnasXlsCompare = [c.replace(" ","_").lower() for c in columnasXls]

# Iteraremos para cada columna del dataframe
for columnaDf in allData.columns:

    # Si la columna es alguna de las columnas de las pestañas...
    if columnaDf.lower() in columnasXlsCompare:
        print(columnaDf.lower())

        # Cargamos la página en concreto:
        try:
            sheet = pd.read_excel("variable lookup.xls",
                                sheet_name = columnaDf.replace("_"," ").strip(),
                                        )
        except:
            sheet = pd.read_excel("variable lookup.xls",
                                sheet_name = columnaDf
                                        )

        sheet.columns = [c.lower() for c in sheet.columns]

        # Creamos el diccionario:
        diccionario = {sheet["code"].iloc[i]: sheet["label"].iloc[i] for i in range(len(sheet["label"]))}
        print(diccionario)
        # Y cambiamos los valores:
        allData = allData.replace({columnaDf:diccionario})
        

# Guardamos:
allData.to_csv("processed.csv", sep = ";", index = False)

# Liberamos memoria
del allData
gc.collect()

# Leemos el dataset preprocesado
processed = pd.read_csv("processed.csv", sep = ";")

# Tomamos una muestra:
sample = processed.head(5000)

# Y lo guardamos.
sample.to_csv("sample.csv", sep = ";", index = False)

# En este útimo script realizaremos la exploración de las variables del dataset:
# Mostraremos las dimensiones del dataset:
print(processed.shape)

campos = pd.DataFrame(processed.columns)

campos.to_csv("campos.csv", sep = ";")

