from queue import Queue
import time, os


dic = {1:('Yeremy','1+1',2,4), 2:('Gera','2+2',4,22), 3:('Lupi','3+3',4,33),4:('Lupi','4+4',4,44),
    5:('Dadan','5+5',4,55),6:('Armando','6+6',4,66),7:('Uriel','7+7',4,77),8:('Eyes','8+8',4,77),}
cola = Queue() #Espera
lis = []      #Terminados
lotes = 2
finished = 0

def imprimir_en_posicion(fila, columna, mensaje):
    # Usar caracteres de escape ANSI para posicionar el cursor
    print(f"\033[{fila};{columna}H{mensaje}", flush=True)

while lotes != 0:
    elementos = list(dic.items())
    total_elementos = len(elementos)
    for x in range(0, total_elementos, 5):  #Se hacen grupos de un maximo de 5
        grupo = elementos[x:x+5]
     #print("Grupo:"(, grupo)
        cola.put(grupo)

    grupito = cola.get()
    while len(grupito) != 0:               #Se muestra cada elemento del grupo
        imprimir_en_posicion(0, 0, '-------------------- < Lote actual > --------------------')
        ejecucion = grupito.pop(0)

        for row in range(2,6):        #Limpia cada fila de la cola
            imprimir_en_posicion(row, 0,'                                                                  ')
        fila = 2
        for element in grupito:       #Actualiza la actual cola
            imprimir_en_posicion(fila, 0,element)
            fila += 1
        imprimir_en_posicion(6, 0, '-------------------- < Proceso en ejecución > --------------------')
        imprimir_en_posicion(7, 0, ejecucion)
        imprimir_en_posicion(8, 0, ejecucion)
        imprimir_en_posicion(9, 0, ejecucion)
        imprimir_en_posicion(10, 0, ejecucion)
        imprimir_en_posicion(11, 0, ejecucion)
        imprimir_en_posicion(12, 0, ejecucion)
        lis.append(ejecucion)
        time.sleep(3)
        imprimir_en_posicion(13, 1, '-------------------- < Terminados > --------------------')
        fila_term = 14
        for terminados in lis:   #Muestra cada uno de los procesos terminados
            imprimir_en_posicion(fila_term, 1, terminados)
            fila_term += 1
    lotes -= 1
