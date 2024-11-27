from package.funciones_generales import *

def traer_datos_configuraciones():
    lista = convertir_csv_a_lista_diccionarios('csv/configuraciones.csv')

    print(lista)

traer_datos_configuraciones()




