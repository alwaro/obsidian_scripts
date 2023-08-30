#!/usr/bin/env python3
# #####################################################################
#    SCRIPT PARA CREAR INDICES EN NOTAS MARKDOWN (OBSIDIAN FORMAT)     
# -------------------------------------------------------------------  
#  Dado que  obsidian ahora mismo no soporta  plugins hechos en python   
#  al menos, de forma  nativa, he optado por crear un script adicional  
#  para  que, pasando la ruta al fichero de la nota,  genere un indice  
#  con sus distinto  niveles y  enlaces internos, que es incrustado al   
#  inicio de la misma nota.                                            
#                                                                      
#  MODO DE USO:                                                        
#  python crearIndiceObsidian.py C:\ruta\a\la\nota.md
#  python crearIndiceObsidian.py "C:\ruta\a\la\nota con espacios.md"
#    
#  En linux, con permiso de ejecucion, se puede  ejecutar directamente
# --------------------------------------------------------------------  
#  WHO           WHEN       WHAT                                       
#  ------------- ---------- ------------------------------------------  
#  Alvaro Anaya  2023-08-15  Creacion  del script. No se hacen cambios
#                            en la nota. El indice  se  muestra en  la 
#                            pantalla formateado para hacer copy/paste 
#  Alvaro Anaya  2023-08-19  V2. No muestra index sino que lo incrusta 
#                            en la nota, al inicio                    
# #####################################################################

import os
import sys


def generarIndice(fichero):
    """ Metodo procesador de fichero y generador de indice """
    indice = '\n**INDICE**\n\n'
    f = open(fichero, 'r', encoding='utf-8')
    for linea in f.readlines():
        if linea.startswith('#'):
            print('Detectado titulo en linea:' + linea) #debug
            nivelEntrada = linea.count('#') - 1
            item = linea.replace('#','').replace('\n','')
            indice += nivelEntrada*'    ' + '[[#'+ item + ']]\n'
        else:
            pass

    f.close()
    return indice


def escribirIndice(bloqueIndice, fichero):
    """ Metodo para escribir el indice en la nota """
    with open(fichero, 'r+', encoding='utf-8') as f:
        contenido = f.read()
        f.seek(0, 0)
        f.write(bloqueIndice + '\n' + contenido)


if __name__ == '__main__':
    # Comprobamos que haya un argumento como minimo
    if len(sys.argv) < 2:
        print('Es obligatorio indicar un fichero de texto en formato MD para crear un indice')
        print('Ejemplos:\n    ' + sys.argv[0] + ' nota1.md\n    ' + sys.argv[0] + ' /ruta/nota2.txt\n')
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('ERROR:\n    ' + sys.argv[1] + ' no es un fichero o no puede leerse\n')
        sys.exit(1)

    fichero = sys.argv[1]
    escribirIndice(generarIndice(fichero),fichero)
