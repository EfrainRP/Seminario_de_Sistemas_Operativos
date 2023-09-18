import math,re,time,random,keyboard,os
from queue import Queue
#Process validation
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
        while op2 == 0:
            op2 = int(opValidator())
        result = op1/op2
        return result,f'{op1} / {op2}'
    elif op =="%":
        while op2 == 0:
            op2 = int(opValidator())
        result = op1%op2
        return result,f'{op1} % {op2}'

def inputProcess(dictProcess,actual_batch,id):
        time = random.randint(20, 40) 
        result,opString = operation()

        dictProcess[id] = [0,opString,round(result,4),int(time),actual_batch]  #we can elimate varible 'opString', only show the operation as string

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
            interrupted = False
            imprimir_en_posicion(0, 80, f' < N° Lotes Pendientes: {lotes-1} > ')
            imprimir_en_posicion(0, 0, '-------------------------- < Lote actual > -------------------------')
            imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT')
            ejecucion = grupito.pop(0)
            limpiar(3,7)    #Limpia las filas en actuales
            fila = 3
            for element in grupito:       #Actualiza la actual cola
                imprimir_en_posicion(fila, 0,f' {element[0]}\t  {element[1][3]}\t  {element[1][0]}')
                fila += 1
            '''if len(grupito) > 3: #Interrupcion para ver cuantos entran en el grupito (entran 4)
                input(' ')'''
            #--------------------------------------------------------------------------------------------------------
            limpiar(8,13)   #Limpia las filas en ejecucion
            imprimir_en_posicion(8, 0, '-------------------- < Proceso en ejecución > --------------------')
            imprimir_en_posicion(9, 0, f'                                       ')
            imprimir_en_posicion(10, 0, f'-ID: {ejecucion[0]}')
            imprimir_en_posicion(11, 0, f'-Operacion-> {ejecucion[1][1]}')
            imprimir_en_posicion(12, 0, f'-Tiempo MXE: {ejecucion[1][2]}')
            #TT = ejecucion[1][0]
            imprimir_en_posicion(13, 0, '                 ')  #Limpia antes de mostrar
            while  ejecucion[1][0] < ejecucion[1][3]:
                ejecucion[1][0] += 1
                imprimir_en_posicion(13, 0, f'-Tiempo TRA: {ejecucion[1][0]}')
                imprimir_en_posicion(14, 0, '                 ')  #Limpia antes de mostrar
                imprimir_en_posicion(14, 0, f'-Tiempo RES: {ejecucion[1][3]-ejecucion[1][0]}')
                contador += 1
                imprimir_en_posicion(8, 80, f' < Contador: {contador} >')  #Muestra el contador
                time.sleep(0.1)
                if keyboard.is_pressed('i'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < INTERRUPCION >')  #Muestra el contado
                    grupito.append(ejecucion)
                    interrupted = True
                    break
                if keyboard.is_pressed('e'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < ERROR >')  #Muestra el contador
                    ejecucion[1][2] = 'Error'
                    break
                if keyboard.is_pressed('p'):  # Verifica si la tecla "p" ha sido presionada
                    imprimir_en_posicion(16, 80, '                 ')  #Limpia antes de mostrar
                    imprimir_en_posicion(14, 80, f' < PAUSA >')  #Muestra el contador
                    keyboard.wait("c") #Espera una "c"
                    imprimir_en_posicion(16, 80, f' < CONTINUANDO >')  #Muestra el contador
                    imprimir_en_posicion(14, 80, '                 ')  #Limpia antes de mostrar
                
            if not interrupted:      #Si no se interrumpio 
                lis.append(ejecucion)
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
            else:                    #Si hay interrupcion 
                continue
            #limpiar(16,100) #Limpia los terminados
        lotes -= 1
        limpiar(9,15)   #Limpia las filas en ejecucion al terminar el programa
        limpiar(2,7)    #Limpia las filas en actuales
        imprimir_en_posicion(fila_term, 1, ' ') #"Posiciona el cursor" para que se imprima al final del programa
        
    # Registra una función de devolución de llamada para eventos de teclado
  
def main():
    os.system('cls')
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
    '''x =0
    for i in dictProcess:
        x += dictProcess[i][3]
    print('tiempo: ',x)'''

    input('Press enter')
    os.system('cls')
    console(dictProcess,batch)

if __name__ == "__main__":
    main()
