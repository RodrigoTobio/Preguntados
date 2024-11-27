lista_diccionarios = [{'usuario': 'Marcos', 'puntaje': '10', 'tiempo': ' 30'}, {'usuario': 'Juan', 'puntaje': '4', 'tiempo': ' 30'}]

def convertir_lista_diccionarios_a_csv(lista_diccionarios: list, path: str):
    """
    ¿Qué hace? -> Convierte una lista de diccionarios a un archivo CSV.
    ¿Qué parámetros acepta?
        - lista_diccionarios: list -> Lista de diccionarios que se quiere guardar en CSV.
        - path: str -> Ruta donde se guardará el archivo CSV.
    ¿Qué retorna? -> None
    """
    if len(lista_diccionarios) > 0:
        encabezados = lista_diccionarios[0].keys()

        with open(path, mode='w', encoding='utf-8', newline='') as archivo:
            archivo.write(','.join(encabezados) + '\n')
            for diccionario in lista_diccionarios:
                fila = []
                for i in diccionario.values():
                    fila.append(i)
                archivo.write(','.join(fila) + '\n')











# lista_ranking = [{'usuario': 'Beto', 'puntaje': '2100', 'tiempo': ' 30'},
#                 {'usuario': 'Marcos', 'puntaje': '2800', 'tiempo': ' 30'},
#                 {'usuario': 'Eduardo', 'puntaje': '2300', 'tiempo': ' 30'}]

# def buscar_menor_puntaje_ranking(lista: list) -> int:
#     min_valor = int(lista[0]['puntaje'])
#     indice_menor_valor = 0
#     for i in range(1,len(lista)):
#         if int(lista[i]['puntaje']) < min_valor:
#             min_valor = int(lista[i]['puntaje'])
#             indice_menor_valor = i

#     return min_valor, indice_menor_valor

# def modificar_ranking(lista: list, datos_jugador: dict):
#     min_valor, indice_min_valor = buscar_menor_puntaje_ranking(lista)

#     if int(datos_jugador['puntaje']) < min_valor:
#         lista[indice_min_valor] = datos_jugador

#     return lista





