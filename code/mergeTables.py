# Importamos las librerías necesarias:
import pandas as pd
import os
import gc
import time

checkedFiles = []

# Iteramos para cada csv en el directorio
for file in os.listdir():
    if file.endswith(".csv"):
        tableName = file.split(".")[0]
        # Si no se ha revisado...
        if tableName not in checkedFiles:
            
            # Tomamos el identificador de las tablas, que será el año:
            identificador = tableName[-4:]

            # Tomamos las tablas de ese año (Accidentes, Casualities y Vehicles):
            identifiedTables = [t for t in os.listdir() if identificador in t]
            print(identificador)
            if len(identifiedTables) != 3:
                print(tableName)
                continue

            # Ordenamos la lista:
            identifiedTables.sort()
            
            # Unimos y guardamos en un csv            
            merged = merged.merge(vehicles, how = "outer", on = "Accident_Index")

            merged.to_csv(str(identificador) + ".csv", sep = ";", index = False,
                          mode = "a")
            
            # Definimos como revisadas las tablas utilizadas
            for tableChecked in identifiedTables:
                checkedFiles += [tableChecked]
