import math,re,time,random,keyboard,os, threading
pausa = threading.Event()

class Process:
    def __init__(self,id):
        self.process_id = id    #ID
        self.time = random.randint(20, 40)  #TME
        self.time_run = 0   #Time running

        result,self.opString = self._operation()  #OperationStr
        self.result = round(result,4)   #Result
    
    def _operation(self):
        def opValidator():
            opN = random.randint(-9999, 9999)
            return opN
        
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
    
    def print(self): #Regresa los tributos como cadena
        return f'ID: {self.process_id} TME: {self.time} TT : {self.time_run} {self.opString} = {self.result}'


#---------------------------------------------------------------------------------------------------------
#CONSOLE

def console(elementos):
    lis = []      #Procesos Terminados
    contador = 0  #Contador global
    grupito = []  #Grupo de 5 procesos
    count = 0     #Process Count
    process = len(elementos) #Processes
    new = process-5 #New Process

    def resize_string(input_string, new_size): #Resize string for table
        if new_size < len(input_string):
            return input_string[:new_size] #Cut the string until new_size
        elif new_size > len(input_string):
            return input_string + ' ' * (new_size - len(input_string)) #Fill out the input_string to have new len of string
        else:
            return input_string
        
    def bloqueado(proceso):   #Estado bloqueado
            TT = 0
            while TT != 8:  #Tiempo de 8 seg
                pausa.wait() #Detiene temporalmente al subproceso
                TT += 1
                imprimir_en_posicion(0, 70, f' < TT {TT} > ')
                time.sleep(1)
            if TT == 8:  #Si transcurren 8 seg
                #imprimir_en_posicion(18, 80, f' < Proceso añadido {proceso} >')  #Muestra el proceso añadido
                grupito.append(proceso)
                limpiar(3,8)    #Limpia las filas en actuales
                fila = 3
                for element in grupito:       #Actualiza el actual grupo de procesos
                    imprimir_en_posicion(fila, 0,f' {element.process_id}\t  {element.time}\t  {element.time_run}')
                    fila += 1
                    
        
    def limpiar(inicial,final):   #Limpia por consola
        for row in range(inicial,final):
            imprimir_en_posicion(row, 0,' ' * 100)

    def imprimir_en_posicion(fila, columna, mensaje):  #Imprime por la posicion mencionada
        # Usar caracteres de escape ANSI para posicionar el cursor
        print(f"\033[{fila};{columna}H{mensaje}", flush=True)
    
    for i in range(5): #Toma los primeros 5 procesos 
        initial = elementos.pop(0)
        grupito.append(initial)    
   
    while count != process:    #Mientras haya procesos pendientes
        #-------------------------------------------------------------------------------
        while count != process:               #Se muestra cada elemento del grupo
            interrupted = False
            imprimir_en_posicion(0, 80, f' < N° Procesos nuevos: {new} > ')
            imprimir_en_posicion(0, 0, '-------------------------- < Listos > -------------------------')
            imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT')
            if len(grupito) == 0:      #Si el grupo esta vacio (todos estan bloqueados) no se muestra nada por consola
                contador += 1
                imprimir_en_posicion(8, 80, f' < Contador: {contador} >')  #Muestra el contador
                limpiar(9,15)   #Limpia las filas en ejecucion
                time.sleep(0.1)
                if keyboard.is_pressed('p'):  # Verifica si la tecla "p" ha sido presionada
                    imprimir_en_posicion(16, 80, '                 ')  #Limpia antes de mostrar
                    imprimir_en_posicion(14, 80, f' < PAUSA >')  #Imprime 
                    pausa.clear()  #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    pausa.set()    #Despausa los subprocesos
                    imprimir_en_posicion(16, 80, f' < CONTINUANDO >')  #Imprime 
                    imprimir_en_posicion(14, 80, '                 ')  #Limpia antes de mostrar
                continue
            else:
                ejecucion = grupito.pop(0) #Sino, obtiene el mas reciente del grupito para mostrar 
            limpiar(3,8)    #Limpia las filas en actuales
            fila = 3
            for element in grupito:       #Actualiza la actual cola
                imprimir_en_posicion(fila, 0,f' {element.process_id}\t  {element.time}\t  {element.time_run}')
                fila += 1
            '''if len(grupito) > 3: #Interrupcion para ver cuantos entran en el grupito (entran 4)
                input(' ')'''
            #--------------------------------------------------------------------------------------------------------
            limpiar(8,13)   #Limpia las filas en ejecucion
            imprimir_en_posicion(8, 0, '-------------------- < Proceso en ejecución > --------------------')
            imprimir_en_posicion(9, 0, f'                                       ')
            imprimir_en_posicion(10, 0, f'-ID: {ejecucion.process_id}')
            imprimir_en_posicion(11, 0, f'-Operacion-> {ejecucion.opString}')
            imprimir_en_posicion(12, 0, f'-Tiempo MXE: {ejecucion.time}')
            #TT = ejecucion.time_run
            imprimir_en_posicion(13, 0, '                 ')  #Limpia antes de mostrar
            while  ejecucion.time_run < ejecucion.time:
                ejecucion.time_run += 1
                imprimir_en_posicion(13, 0, f'-Tiempo TRA: {ejecucion.time_run}            ')
                imprimir_en_posicion(14, 0, '                 ')  #Limpia antes de mostrar
                imprimir_en_posicion(14, 0, f'-Tiempo RES: {ejecucion.time-ejecucion.time_run}        ')
                contador += 1
                imprimir_en_posicion(8, 80, f' < Contador: {contador} >')  #Muestra el contador
                time.sleep(0.1)
                if keyboard.is_pressed('i'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < INTERRUPCION >')  #Muestra el contado
                    t = threading.Thread(target=bloqueado, args=(ejecucion,)) #Subproceso bloqueados
                    t.start() 
                    pausa.set()
                    imprimir_en_posicion(16, 80, '                 ')  #Limpia antes de mostrar
                    imprimir_en_posicion(14, 80, f' < BLOQUEADO >')  #Muestra el contador
                    #elementos.append(ejecucion)
                    interrupted = True
                    break
                if keyboard.is_pressed('e'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < ERROR >')  #Muestra el contador
                    ejecucion.result = 'Error'
                    break
                if keyboard.is_pressed('p'):  # Verifica si la tecla "p" ha sido presionada
                    imprimir_en_posicion(16, 80, '                 ')  #Limpia antes de mostrar
                    imprimir_en_posicion(14, 80, f' < PAUSA >')  #Muestra el contador
                    pausa.clear() #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    pausa.set()   #Despausa los subprocesos
                    imprimir_en_posicion(16, 80, f' < CONTINUANDO >')  #Muestra el contador
                    imprimir_en_posicion(14, 80, '                 ')  #Limpia antes de mostrar
                
            if not interrupted:      #Si no se interrumpio 
                lis.append(ejecucion)
                imprimir_en_posicion(16, 1, '------------------------- < Terminados > --------------------------')
                imprimir_en_posicion(17, 1, '>ID\t\t>Operacion\t\t\t>Resultado')
                count += 1
                if len(elementos) != 0:
                    next = elementos.pop(0) #Se añade el proximo proceso
                    grupito.append(next)
                if new != 0:
                    new -= 1
                fila_term = 18
                for terminados in lis:   #Muestra cada uno de los procesos terminados
                    idString = resize_string(' ' + str(terminados.process_id),18)
                    operationString = resize_string(terminados.opString,32)
                    resultString = resize_string(' ' + str(terminados.result),14)
                    imprimir_en_posicion(fila_term, 1, f'{idString}{operationString}{resultString}')
                    fila_term += 1
            else:                    #Si hay interrupcion 
                continue
            #limpiar(16,100) #Limpia los terminados
        
        limpiar(9,15)   #Limpia las filas en ejecucion al terminar el programa
        limpiar(2,8)    #Limpia las filas en actuales
    imprimir_en_posicion(18+len(lis), 1, '') #"Posiciona el cursor" para que se imprima al final del programa

def main():
    os.system('cls')
    
    process = input("Introduzca la cantidad de procesos a realizar: ")
    while not re.match("^[1-9]+\d*$", process):
        process = input("Introduzca NUEVAMENTE la cantidad de procesos a realizar: ")
    process = int(process)
    
    os.system('cls')
    listProcess = []
    for count_process in range(1,process+1):
        listProcess.append(Process(count_process))

    #print(listProcess)
    
    for i in listProcess:
        print(i.print())

    input('Press enter')
    os.system('cls')
    console(listProcess)

if __name__ == "__main__":
    main()
