from queue import Queue
import time, os

dic = {1:('Yeremy','122+122',222222,4,1), 2:('Gera','2+2',4,4,1), 3:('Lupi','3+3',4,4,1),4:('Lupi','4+4',4,4,1),
    5:('Dadan','5+5',4,4,1),6:('Armando','6+6',4,4,2),7:('Uriel','7+7',4,4,2),8:('Violeta','8+8',4,4,2),
    9:('Juan','8+8',4,4,2),10:('Raul','8+8',4,4,2),11:('Fabiola','8+8',4,4,3),12:('Sara','8+8',4,4,3),}
cola = Queue() #Lotes en espera
lis = []      #Lotes Terminados
lotes = 3     #Variable que indica la cantidad de lotes por realizar
contador = 0  #Contador global 

def limpiar(inicial,final):   #Limpia por consola
    for row in range(inicial,final):
        imprimir_en_posicion(row, 0,'                                                                      ')

def imprimir_en_posicion(fila, columna, mensaje):  #Imprime por la posicion mencionada
    # Usar caracteres de escape ANSI para posicionar el cursor
    print(f"\033[{fila};{columna}H{mensaje}", flush=True)

while lotes != 0:    #Mientras haya lotes pendientes
    elementos = list(dic.items())
    total_elementos = len(elementos)
    for x in range(0, total_elementos, 5):  #Se hacen grupos de un maximo de 5
        grupo = elementos[x:x+5]
        cola.put(grupo)
    grupito = cola.get()
    #-------------------------------------------------------------------------------
    while len(grupito) != 0:               #Se muestra cada elemento del grupo
        imprimir_en_posicion(0, 80, f' < N° Lotes Pendiantes: {lotes-1} > ')
        imprimir_en_posicion(0, 0, '                     < Lote actual > --------------------')
        imprimir_en_posicion(1, 0, '>ID\t>TME')
        ejecucion = grupito.pop(0)
        limpiar(2,6)    #Limpia las filas en actuales
        fila = 2
        for element in grupito:       #Actualiza la actual cola
            imprimir_en_posicion(fila, 0,f'{element[0]}\t{element[1][3]}')
            fila += 1
        #--------------------------------------------------------------------------------------------------------
        limpiar(6,11)   #Limpia las filas en ejecucion
        imprimir_en_posicion(6, 0, '-------------------- < Proceso en ejecución > --------------------')
        imprimir_en_posicion(7, 0, f'>Programador: {ejecucion[1][0]}')
        imprimir_en_posicion(8, 0, f'-ID: {ejecucion[0]}')
        imprimir_en_posicion(9, 0, f'-Operacion-> {ejecucion[1][1]}')
        imprimir_en_posicion(10, 0, f'-Tiempo MXE: {ejecucion[1][3]}')
        TT = 0
        while TT < ejecucion[1][3]:
            TT += 1
            imprimir_en_posicion(11, 0, f'-Tiempo TRA: {TT}')
            imprimir_en_posicion(12, 0, '                 ')  #Limpia antes de mostrar
            imprimir_en_posicion(12, 0, f'-Tiempo RES: {ejecucion[1][3]-TT}')
            contador += 1
            imprimir_en_posicion(8, 80, f' -Contador: {contador} ')  #Muestra el contador
            time.sleep(1)
        lis.append(ejecucion)
        #limpiar(16,100) #Limpia los terminados
        imprimir_en_posicion(13, 1, '-------------------- < Terminados > --------------------')
        imprimir_en_posicion(14, 1, '>ID\t\t>Operacion\t\t>Resultado\t-NL')
        fila_term = 15
        for terminados in lis:   #Muestra cada uno de los procesos terminadt\tos
            imprimir_en_posicion(fila_term, 1, f'{terminados[0]}\t\t{terminados[1][1]}\t\t\t{terminados[1][2]}\t\t{terminados[1][4]}')
            fila_term += 1
    lotes -= 1

