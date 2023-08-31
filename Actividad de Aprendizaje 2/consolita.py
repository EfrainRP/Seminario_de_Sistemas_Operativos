import math
import re
from queue import Queue
import time, os

def validationID():
    id = input("Introduzca la ID: ")
    while not re.match("^[1-9]+\d*$", id) and id not in dictProcess:#Verificate if the ID is repeated and use expresion regular for numbres from 1 to infinity
        id = input("\tID INVALIDA\nIntroduzca nueva ID: ")

    return id

def opValidator(opN,N):
        while not re.match(r'^[+-]?\d+$', opN):  #We use a expresion regular to validate the string for real numbers
            opN = input(f'\tCifra invalida\tIntroduzca NUEVAMENTE la #{N} cifra: ')
        return opN

def operation():
    op1 = input("\tOPERACION\nIntroduzca la primera cifra: ")
    op1 = int(opValidator(op1,1))
    op2 = input("Introduzca la segunda cifra: ")
    op2 = int(opValidator(op2,2))

    op = input("Introduzca la operacion a realizar: ")
    while not re.match(r'^[+\-*/%]+$', op): #We use a expresion regular to validate the string for operators
            op = input("Introduzca NUEVAMENTE la operacion a realizar: ")

    if op == "+":
        result = op1+op2
        return result,f'{op1}+{op2}={result}'
    elif op == "-":
        result = op1-op2
        return result,f'{op1}-{op2}={result}'
    elif op == "*":
        result = op1*op2
        return result,f'{op1}*{op2}={result}'
    elif op == "/": # / (division)
        try: #Exception of 0 as divisor
            result = op1/op2
        except ZeroDivisionError:
            print("No se puede dividir entre cero :(\n\tIngrese nuevos valores")
            while op2 == 0:
                op2 = input("Introduzca NUEVAMENTE la segunda cifra: ")
                op2 = int(opValidator(op2,2))
            result = op1/op2
        return result,f'{op1}/{op2}={result}'
    elif op =="%":
        try: #Exception of 0 as divisor
            result = op1%op2
        except ZeroDivisionError:
            print("No se puede dividir entre cero :(\n\tIngrese nuevos valores")
            while op2 == 0:
                op2 = input("Introduzca NUEVAMENTE la segunda cifra: ")
                op2 = int(opValidator(op2,2))
            result = op1%op2
        return result,f'{op1}%{op2}={result}'

def inputProcess(actual_batch):
        nombre = input("Introduzca un nombre: ")
        while not re.match("^[a-zA-Z]+\s?[a-zA-Z]*$", nombre): #We use a expresion regular to validate the string
            nombre = input("Introduzca NUEVAMENTE un nombre: ")

        id = validationID()
        result,opString = operation()
        time = input("Introduzca el tiempo aproximado: ")
        while not re.match("^[1-9]+\d*$", time):  #We use a expresion regular to validate the string for time
            time = input("Introduzca NUEVAMENTE el tiempo aproximado: ")

        dictProcess[id] = (nombre,opString,result,int(time),actual_batch)  #we can elimate varible 'opString', only show the operation as string



#---------------------------------------------------------------------------------------------------------
#CONSOLE

def console(dic,batch):
    cola = Queue() #Lotes en espera
    lis = []      #Lotes Terminados
    lotes = batch     #Variable que indica la cantidad de lotes por realizar
    contador = 0  #Contador global

    def limpiar(inicial,final):   #Limpia por consola
        for row in range(inicial,final):
            imprimir_en_posicion(row, 0,'                                                                            ')

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
        limpiar(7,13)   #Limpia las filas en ejecucion al terminar el programa

def main():
    #dic = {1:('Yeremy','122+122',144,4,1), 2:('Gera','2+2',4,4,1), 3:('Lupi','8-3',5,4,1),4:('Lupi','4x2',8,4,1),
    #    5:('Dadan','10/2',1,4,1),6:('Armando','12%2',0,4,2),7:('Uriel','7+7',14,4,2),8:('Violeta','8+8',16,4,2),
    #    9:('Juan','11-5',6,4,2),10:('Raul','10+10',20,4,2),11:('Fabiola','8+8',16,4,3),12:('Sara','5+4',9,4,3),}
    dictProcess = {}
    process = input("Introduzca la cantidad de procesos a realizar: ")
    while not re.match("^[1-9]+\d*$", process):
        process = input("Introduzca NUEVAMENTE la cantidad de procesos a realizar: ")
    process = int(process)
    batch = math.ceil(process/5) #we need to round out
    actual_batch = 1             #Actual batch running
    count_batch = 1              #Batch count
    #print(batch)
    while process >= 1:
        print(f'Proceso {process}')
        inputProcess(actual_batch)
        os.system('cls')
        if count_batch == 5:
            actual_batch += 1
            count_batch = 0
        process = process-1
        count_batch += 1
    print(dictProcess)


    input('Press enter')
    os.system('cls')
    console(dictProcess,batch)

if __name__ == "__main__":
    main()
