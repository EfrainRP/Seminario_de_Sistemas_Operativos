import math
import re
from queue import Queue
import time, os
import random

def opValidator():
        opN = random.randint(-9999, 9999)
        return opN

def operation():
    op1 = int(opValidator())
    op2 = int(opValidator())

    operador = ['+', '-', '*', '/', '%']
    
    op = random.choice(operador)
    
    if op == "+":
        result = op1+op2
        return result,f'{op1} + {op2}'
    elif op == "-":
        result = op1-op2
        return result,f'{op1} - {op2}'
    elif op == "*":
        result = op1*op2
        return result,f'{op1} * {op2}'
    elif op == "/": # / (division)
        ''' try: #Exception of 0 as divisor
            result = op1/op2
        except ZeroDivisionError:
            print("No se puede dividir entre cero :(\n\tIngrese nuevos valores")
        '''
        while op2 == 0:
            op2 = int(opValidator())
        result = op1/op2
        return result,f'{op1} / {op2}'
    elif op =="%":
        ''' try: #Exception of 0 as divisor
            result = op1%op2
        except ZeroDivisionError:
            print("No se puede dividir entre cero :(\n\tIngrese nuevos valores")
        '''
        while op2 == 0:
            op2 = int(opValidator())
        result = op1%op2
        return result,f'{op1} % {op2}'

def inputProcess(dictProcess,actual_batch,id):
        time = random.randint(6, 18) 
        result,opString = operation()

        dictProcess[id] = (opString,round(result,4),int(time),actual_batch)  #we can elimate varible 'opString', only show the operation as string

#---------------------------------------------------------------------------------------------------------
#CONSOLE

def console(dic,batch):
    cola = Queue() #Lotes en espera
    lis = []      #Lotes Terminados
    lotes = batch     #Variable que indica la cantidad de lotes por realizar
    contador = 0  #Contador global

    def resize_string(input_string, new_size): #Resize string for table
        if new_size < len(input_string):
            return input_string[:new_size] #Cut the string until new_size
        elif new_size > len(input_string):
            return input_string + ' ' * (new_size - len(input_string)) #Fill out the input_string to have new len of string
        else:
            return input_string

    def limpiar(inicial,final):   #Limpia por consola
        for row in range(inicial,final):
            imprimir_en_posicion(row, 0,' ' * 100)

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
            imprimir_en_posicion(0, 80, f' < N° Lotes Pendientes: {lotes-1} > ')
            imprimir_en_posicion(0, 0, '-------------------------- < Lote actual > -------------------------')
            imprimir_en_posicion(2, 0, '>ID\t>TME')
            ejecucion = grupito.pop(0)
            limpiar(3,7)    #Limpia las filas en actuales
            fila = 3
            for element in grupito:       #Actualiza la actual cola
                imprimir_en_posicion(fila, 0,f' {element[0]}\t  {element[1][3]}')
                fila += 1
            '''if len(grupito) > 3: #Interrupcion para ver cuantos entran en el grupito (entran 4)
                input(' ')'''
            #--------------------------------------------------------------------------------------------------------
            limpiar(8,13)   #Limpia las filas en ejecucion
            imprimir_en_posicion(8, 0, '-------------------- < Proceso en ejecución > --------------------')
            imprimir_en_posicion(9, 0, f'>Programador: {ejecucion[1][0]}')
            imprimir_en_posicion(10, 0, f'-ID: {ejecucion[0]}')
            imprimir_en_posicion(11, 0, f'-Operacion-> {ejecucion[1][1]}')
            imprimir_en_posicion(12, 0, f'-Tiempo MXE: {ejecucion[1][3]}')
            TT = 0
            while TT < ejecucion[1][3]:
                TT += 1
                imprimir_en_posicion(13, 0, f'-Tiempo TRA: {TT}')
                imprimir_en_posicion(14, 0, '                 ')  #Limpia antes de mostrar
                imprimir_en_posicion(14, 0, f'-Tiempo RES: {ejecucion[1][3]-TT}')
                contador += 1
                imprimir_en_posicion(8, 80, f' < Contador: {contador} >')  #Muestra el contador
                time.sleep(1)
            lis.append(ejecucion)
            #limpiar(16,100) #Limpia los terminados
            imprimir_en_posicion(16, 1, '------------------------- < Terminados > --------------------------')
            imprimir_en_posicion(17, 1, '>ID\t\t>Operacion\t\t\t>Resultado\t>NL')
            fila_term = 18
            for terminados in lis:   #Muestra cada uno de los procesos terminadt\tos
                idString = resize_string(' ' + str(terminados[0]),18)
                operationString = resize_string(terminados[1][1],32)
                resultString = resize_string(' ' + str(terminados[1][2]),14)
                NL_String = resize_string(' ' + str(terminados[1][4]),4)
                imprimir_en_posicion(fila_term, 1, f'{idString}{operationString}{resultString}{NL_String}')
                fila_term += 1
        lotes -= 1
        limpiar(9,15)   #Limpia las filas en ejecucion al terminar el programa
        limpiar(2,7)    #Limpia las filas en actuales
        imprimir_en_posicion(fila_term, 1, ' ') #"Posiciona el cursor" para que se imprima al final del programa
        

def main():
    os.system('cls')
    '''
    dictProcess = {1:('Yeremy','122+122',144,4,1), 2:('Gera','2+2',4,4,1), 3:('Lupi','8-3',5,4,1),4:('Lupi','4x2',8,4,1),
        5:('Dadan','10/2',1,4,1),6:('Armando','12%2',0,4,2),7:('Uriel','7+7',14,4,2),8:('Violeta','8+8',16,4,2),
        9:('Juan','11-5',6,4,2),10:('Raul','10+10',20,4,2),11:('Fabiola','8+8',16,4,3),12:('Sara','5+4',9,4,3),}
    process = 12
    '''
    dictProcess = {}
    process = input("Introduzca la cantidad de procesos a realizar: ")
    while not re.match("^[1-9]+\d*$", process):
        process = input("Introduzca NUEVAMENTE la cantidad de procesos a realizar: ")
    process = int(process)
    
    batch = math.ceil(process/5) #we need to round out
    actual_batch = 1             #Actual batch running
    count_batch = 1              #Batch count
    count_process = 1            #Process count
    id = 1                       #ID Count
    #print(batch)
    os.system('cls')
    while count_process <= process:
        inputProcess(dictProcess, actual_batch, id)
        if count_batch == 5:
            actual_batch += 1
            count_batch = 0
        count_batch += 1
        count_process += 1
        id += 1
    print(dictProcess)
    input('')
    '''x =0
    for i in dictProcess:
        x += dictProcess[i][3]
    print('tiempo: ',x)'''

    input('Press enter')
    os.system('cls')
    console(dictProcess,batch)

if __name__ == "__main__":
    main()
