import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta='C:\\Users\\Usuario\\OneDrive\\Escritorio\\python\\Curso_udemy\\dia 9\\proyecto\\Mi_Gran_Directorio'    #print('it´s working bro')

mi_patron = r'N\D{3}-\d{5}'

hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []

def buscadora(ruta,patron):
    for direccion,carpetas,archivos in os.walk(ruta):
        for arch in archivos:
            archivs=Path(direccion,arch)
            archiv=open(archivs,'r')
            archivo=archiv.read()
            
            if re.search(patron,archivo):
                archivos_encontrados.append(arch)
                list_text=list(re.search(patron,archivo).span())
                #print(list_text)
                num1=list_text[0]
                num2=list_text[1]
                nros_encontrados.append(archivo[num1:num2])
    tuple_text=zip(archivos_encontrados,nros_encontrados)
    for texto,documento in tuple_text:
        print(f'en el archivo {texto}--se encontró {documento}')
        print('*'*50,'')
    print(f'patrones encontrados  {len(nros_encontrados)}')
                

patron=r'N\D{3}-\d{5}'          
buscadora(ruta,patron)