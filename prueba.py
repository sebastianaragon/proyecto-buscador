from importlib.resources import path
import re
import os
import time
import datetime
from pathlib import Path
import math


inicio = time.time()

ruta='C:\\Users\\Usuario\\OneDrive\\Escritorio\\python\\Curso_udemy\\dia 9\\proyecto\\Mi_Gran_Directorio\\Directorio_1\\Directorio_1A'    #print('it´s working bro')

mi_patron = r'N\D{3}-\d{5}'
archivos_encontrados=[]
texto_encontrado=[]

este_arch=Path(ruta,'archivo3.txt')
este_archivo=open(este_arch,'r')
arch=este_archivo.read()
print(type(arch))
print(re.search(mi_patron,arch).span())
if re.search(mi_patron,arch):
    archivos_encontrados.append(arch)
    #index=re.search(mi_patron,arch).span()
    list_text=list(re.search(mi_patron,arch).span())
    num1=list_text[0]
    num2=list_text[1]
    print(arch)
    print (arch[num1:num2])
    #print(list(index))
    #print(arch[258:268])
    #texto_encontrado.append(arch[str(re.search(mi_patron,arch).span())])
    #print(f'se ha encontrado {texto_encontrado} en {archivos_encontrados}')
    
//how to become string to inter?
    