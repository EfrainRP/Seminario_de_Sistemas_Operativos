import math,re,time,random,keyboard,os, threading
pausa = threading.Event()
end = False #END Thread
key_i = False
key_e = False
key_p = False
key_n = False
key_b = False

class Process:
    def __init__(self,id):
        self.process_id = id    #ID
        self.time = random.randint(6, 18)  #TME
        self.time_arrival = 0 #Time of Arrival
        self.completion_time = 0 #Completion Time
        self.return_time = 0  #Return time
        self.response_time = 0  #Response time
        self.band_response = False  #Band response time
        self.wait_time = 0 #Wait time 
        self.time_run = 0   #Time running = TT
        self.blocked_time = 0 #Blocked time

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
        return f'ID: {self.process_id} TME: {self.time} TT : {self.time_run} {self.opString} = {self.result} TL : {self.time_arrival} TF : {self.completion_time} TR : {self.return_time} TRES : {self.response_time} TW : {self.wait_time} BAND : {self.band_response} BT : {self.blocked_time}'


#---------------------------------------------------------------------------------------------------------
#CONSOLE

def console(elementos,quantum):
    global key_i,key_e,key_p,end,key_n,process,key_b,new
    lis = []      #Procesos Terminados
    contador = 0  #Contador global
    grupito = []  #Grupo de 5 procesos
    count = 0     #Process Count
    process = len(elementos) #Processes
    pos_fila = 11 #pos_fila process
    bloqueados = [(0),(0),(0),(0),(0)] #Procesos Bloqueados
    quantum_time = quantum #Current Quantum 

    def printListos(element, fila): #Funcion para imprimir con formato los listos
        imprimir_en_posicion(fila, 0,' ' + resize_string(str(element.process_id),5)+'\t '+ resize_string(str(element.time),4)+ '\t ' + resize_string(str(element.time_run),4))
        
    def resize_string(input_string, new_size): #Resize string for table
        if new_size < len(input_string):
            return input_string[:new_size] #Cut the string until new_size
        elif new_size > len(input_string):
            return input_string + ' ' * (new_size - len(input_string)) #Fill out the input_string to have new len of string
        else:
            return input_string
    
    def cantOcupados(): #Funcion de validacion de arreglo de bloqueados
        vacio=0
        for b in bloqueados:
            if b == 0:
                vacio +=1
        ocupados = 5-vacio
        return ocupados
        
    def bloqueado(proceso,pos_fila):   #Estado bloqueado
            global new
            TT = 0
            if pos_fila == 11: #Primer bloqueado
                index = 0 #ID process
            elif pos_fila == 12: #Segundo bloqueado
                index = 1 #ID process
                
            elif pos_fila == 13: #Tercer bloqueado
                index = 2 #ID process
            elif pos_fila == 14: #Cuarto bloqueado
                index = 3 #ID process
            else:           #Quinto bloqueado
                index = 4 #ID process
            while TT != 8:  #Tiemp de 8 seg
                pausa.wait() #Detiene temporalmente al subproceso
                TT += 1
                proceso.blocked_time = TT
                bloqueados[index] = proceso #Contador actual del proceso bloqueado
                imprimir_en_posicion(pos_fila, 90, f'\t\t>ID: {proceso.process_id} TT--> {proceso.blocked_time} ')
                #imprimir_en_posicion(pos, 70, f' < TT {bloqueados[index]} > ')  
                time.sleep(0.5)
            imprimir_en_posicion(pos_fila, 90,  ' '*40) #Limpiar
            if TT == 8:  #Si transcurren 8 seg
                #imprimir_en_posicion(18, 80, f' < Proceso añadido {proceso} >')  #Muestra el proceso añadido
                proceso.blocked_time = 0 #Reinicia el contador de bloqueado 
                if len(grupito) > 3: #Si el grupo ya es mayor o = 5
                    new += 1
                    elementos.append(proceso)
                    imprimir_en_posicion(0, 80, f' < N° Procesos nuevos: {new} > ') #Imprime 
                    limpiar(3,8)    #Limpia las filas en actuales
                else:
                    grupito.append(proceso)
                bloqueados[index] = (0) #Reinicia el tiempo de bloqueo para un nuevo bloqueado
                
                limpiar(3,8)    #Limpia las filas en actuales
                fila = 3
                for element in grupito:       #Actualiza el actual grupo de procesos
                    printListos(element,fila) #Funcion para impresion con formato
                    fila += 1             
        
    def limpiar(inicial,final):   #Limpia por consola
        for row in range(inicial,final):
            imprimir_en_posicion(row, 0,' ' * 100)

    def imprimir_en_posicion(fila, columna, mensaje):  #Imprime por la posicion mencionada
        # Usar caracteres de escape ANSI para posicionar el cursor
        print(f"\033[{fila};{columna}H{mensaje}", flush=True)
    
    def tecla_b(): #Key b Process Table
                    os.system('cls')
                    imprimir_en_posicion(0, 30, '\t\t\t  < Tabla de Procesos > ')
                    imprimir_en_posicion(3, 0, '-------------------- < Nuevos > --------------------')
                    imprimir_en_posicion(4, 0, '>ID\t>TME\t>Operación\t\t\t\tTL\tTS\tTE')
                    table_row = 5
                    for nuevo in elementos:  #Nuevos 
                        wait_tim = (contador-nuevo.time_run) #Tiempo de espera actual
                        imprimir_en_posicion(table_row, 1, f'{resize_string(" "+str(nuevo.process_id),4)}\t{resize_string(" "+str(nuevo.time),4)}\t{resize_string(" "+str(nuevo.opString),15)}\t\t\t\t{resize_string(" "+str(nuevo.time_arrival),4)}\t{resize_string(" "+str(nuevo.time_run),4)}\t{resize_string(" "+str(wait_tim),4)}') 
                        table_row += 1
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '-------------------- < Listos > -----------------------')
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '>ID\t>TME\t>Operación\t\t\t\tTL\tTS\tTE\tTRES')
                    table_row += 1
                    for element in grupito:
                        wait_tim = (contador-element.time_run) #Tiempo de espera actual
                        imprimir_en_posicion(table_row, 1, f'{resize_string(" "+str(element.process_id),4)}\t{resize_string(" "+str(element.time),4)}\t{resize_string(" "+element.opString,15)}\t\t\t\t{resize_string(str(element.time_arrival),4)}\t{resize_string(str(element.time_run),4)}\t{resize_string(str(wait_tim),4)}\t{resize_string(str(element.response_time),4)}')
                        table_row +=1 
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '-------------------- < Ejecución > --------------------')
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '>ID\t>TME\t>Operación\t\t\t\tTL\tTS\tTE\tTRES')
                    table_row += 1
                    wait_tim = (contador-ejecucion.time_run) #Tiempo de espera actual
                    imprimir_en_posicion(table_row, 0, f'{resize_string(" "+str(ejecucion.process_id),4)}\t{" "+resize_string(str(ejecucion.time),4)}\t{" "+resize_string(ejecucion.opString,15)}\t\t\t{resize_string(str(ejecucion.time_arrival),4)}\t{resize_string(str(ejecucion.time_run),4)}\t{resize_string(str(wait_tim),4)}\t{resize_string(str(ejecucion.response_time),4)}')
                    if bloqueados[4] != 0 and bloqueados[3] != 0 and bloqueados[2] != 0 and bloqueados[1] != 0 and bloqueados[4] != 0:
                        imprimir_en_posicion(table_row, 0, f' '*300)
                    table_row += 2
                    #imprimir_en_posicion(10, 90, f'{bloqueados}')
                    imprimir_en_posicion(table_row, 0, '-------------------- < Bloqueados > -------------------')
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '>ID\tRestante\t>Operación\t\t\tTL\tTS\tTE\tTRES')
                    table_row += 1
                    total_TT = 8 #Maximo transcurrido
                    for blocked in bloqueados:
                        if blocked != 0:
                            wait_tim = (contador-blocked.time_run) #Tiempo de espera actual
                            imprimir_en_posicion(table_row, 1, f'{resize_string(" "+str(blocked.process_id),4)}\t{resize_string(" " + str(total_TT-blocked.blocked_time),8)}\t{resize_string(" "+blocked.opString,15)}\t\t\t{resize_string(str(blocked.time_arrival),4)}\t{resize_string(str(blocked.time_run),4)}\t{resize_string(str(wait_tim),4)}\t{blocked.response_time}')
                            table_row += 1
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '-------------------- < Terminados > -------------------')
                    table_row += 1  
                    imprimir_en_posicion(table_row, 0, '>ID\t>Operacion\t>Resultado\t\t\tTL\tTF\tTR\tTRES\tTE\tTS')
                    table_row += 1
                    for terminados in lis:
                        imprimir_en_posicion(table_row, 1, f'{resize_string(" "+str(terminados.process_id),4)}\t{resize_string(" "+terminados.opString,15)}\t{resize_string(" "+str(terminados.result),8)}\t\t\t{resize_string(str(terminados.time_arrival),4)}\t{resize_string(str(terminados.completion_time),4)}\t{resize_string(str(terminados.return_time),4)}\t{resize_string(str(terminados.response_time),4)}\t{resize_string(str(terminados.wait_time),4)}\t{resize_string(str(terminados.time_run),4)}')
                        table_row += 1
                    #imprimir_en_posicion(1, 90, f'{bloqueados}') 
                    pausa.clear() #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    os.system('cls')
                    imprimir_en_posicion(0, 80, f' < N° Procesos nuevos: {new} > ')
                    imprimir_en_posicion(0, 0, '-------------------------- < Listos > -------------------------')
                    imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT')
                    imprimir_en_posicion(2, 85, f' < Contador: {contador} >')  #Muestra el contador
                    fila_b = 3
                    for element in grupito:       #Actualiza la actual cola
                        printListos(element,fila_b)
                        fila_b += 1
                    imprimir_en_posicion(8, 0, '-------------------- < Proceso en ejecución > --------------------')
                    imprimir_en_posicion(9, 0, f'                                       ')
                    imprimir_en_posicion(10, 0, f'-ID: {ejecucion.process_id}')
                    imprimir_en_posicion(11, 0, f'-Operacion-> {ejecucion.opString}')
                    imprimir_en_posicion(12, 0, f'-Tiempo MXE: {ejecucion.time}')
                    imprimir_en_posicion(13, 0, f'-Tiempo TRA: {ejecucion.time_run}            ')
                    imprimir_en_posicion(14, 0, '                 ')  #Limpia antes de mostrar
                    imprimir_en_posicion(14, 0, f'-Tiempo RES: {ejecucion.time-ejecucion.time_run}        ')
                    imprimir_en_posicion(16, 1, '------------------------- < Terminados > --------------------------')
                    imprimir_en_posicion(17, 1, '>ID\t>Operacion\t>Resultado\t\t\tTL\tTF\tTR\tTRES\tTE\tTS')
                    fila_term_b = 18       
                    for terminados in lis:   #Muestra cada uno de los procesos terminados
                        idString = resize_string(' ' + str(terminados.process_id),4)
                        operationString = resize_string(terminados.opString,15)
                        resultString = resize_string(' ' + str(terminados.result),8)
                        time_arrival = resize_string(str(terminados.time_arrival),4)
                        completion_time = resize_string(str(terminados.completion_time),4)
                        return_time = resize_string(str(terminados.return_time),4)
                        response_time = resize_string(str(terminados.response_time),4)
                        wait_time = resize_string(str(terminados.wait_time),4)
                        time_run = resize_string(str(terminados.time_run),4)
                        imprimir_en_posicion(fila_term_b, 1, f'{idString}\t{operationString}\t{resultString}\t\t\t{time_arrival}\t{completion_time}\t{return_time}\t{response_time}\t{wait_time}\t{time_run}')
                        fila_term_b += 1
                    pausa.set()   #Despausa los subprocesos
                    imprimir_en_posicion(7, 90, f'\t\t< CONTINUANDO >')  #Muestra el contador
                    imprimir_en_posicion(8, 90, '                                       ')  
        
    if len(elementos) > 5: #Procesos mayores a 5
        for i in range(5): #Toma los primeros 5 procesos 
            initial = elementos.pop(0)
            initial.time_arrival = contador  #Tiempo de llegada de los primeros 5 procesos 
            grupito.append(initial)    
        new = process-5 #New Process
    else: #Procesos menores a 6
        for i in range(len(elementos)): #Toma todos lox procesos 
            initial = elementos.pop(0)
            initial.time_arrival = contador  #Tiempo de llegada de todos los procesos
            grupito.append(initial)  
        new = process-len(grupito) #New Process

    while count != process:    #Mientras haya procesos pendientes
        #-------------------------------------------------------------------------------
        while count != process:               #Se muestra cada elemento del grupo
            interrupted = False
            imprimir_en_posicion(0, 80, f' < N° Procesos nuevos: {new} > ')
            imprimir_en_posicion(0, 0, '-------------------------- < Listos > -------------------------')
            imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT')
            if len(grupito) == 0:      #Si el grupo esta vacio (todos estan bloqueados) no se muestra nada por consola
                contador += 1
                imprimir_en_posicion(2, 85, f' < Contador: {contador} >')  #Muestra el contador
                imprimir_en_posicion(3, 85, f' < Quantum: {quantum_time} >')  #Muestra el Quantum
                limpiar(9,15)   #Limpia las filas en ejecucion
                time.sleep(0.5)
                if key_p == True:
                #if keyboard.is_pressed('p'):  # Verifica si la tecla "p" ha sido presionada
                    imprimir_en_posicion(7, 90, '                                      ')  #Limpia antes de mostrar
                    imprimir_en_posicion(8, 90, '                                      ')  #Limpia antes de mostrar
                    imprimir_en_posicion(7, 90, f'\t\t< PAUSA >')  #Muestra el contador
                    #imprimir_en_posicion(16, 90, f'\t\t{bloqueados}')  #Imprime
                    
                    pausa.clear()  #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    pausa.set()    #Despausa los subprocesos
                    imprimir_en_posicion(7, 90, '                                       ')  #Limpia antes de mostrar
                    imprimir_en_posicion(7, 90, f'\t\t< CONTINUANDO >')  #Muestra el contador
                    key_p = False
                if key_b == True:
                    tecla_b()
                    key_b = False
                if key_n == True:
                    process+=1
                    new_process = (Process(process)) #Crea un nuevo proceso 
                    new_process.time_arrival = contador          

                    if (cantOcupados() + len(grupito)) < 4 :        #Si hay menos de 5 procesos en cola
                        if len(grupito) < 4:
                            grupito.append(new_process) #Agrega a la cola
                        else:
                            elementos.append(new_process)
                            
                    else: #Si hay mas de 5 procesos en la cola
                        elementos.append(new_process) #Agrega a nuevos
                        new += 1 
                    imprimir_en_posicion(0, 80, f' < N° Procesos nuevos: {new} > ') #Imprime 
                       
                    #imprimir_en_posicion(5, 90, f'\t\t{new_process.process_id}') #Mensaje para determinar el ID del nuevo proceso
                    key_n = False
                continue
            else:
                ejecucion = grupito.pop(0) #Sino, obtiene el mas reciente del grupito para mostrar
                #imprimir_en_posicion(13, 80, f'{ejecucion.band_response}')  #Muestra el contador
                if ejecucion.band_response == False:
                    ejecucion.response_time = (contador-ejecucion.time_arrival) #Tiempo de respuesta 
                    ejecucion.band_response = True
            limpiar(3,8)    #Limpia las filas en actuales
            fila = 3
            for element in grupito:       #Actualiza la actual cola
                printListos(element,fila)
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
                if quantum_time <= 0: #SI el quantum es 0 
                    interrupted = True
                    if len(grupito) < 5:        #Si hay menos de 5 procesos en cola
                            grupito.append(ejecucion) #Agrega a la cola
                    else: #Si hay mas de 5 procesos en la cola
                        elementos.append(ejecucion) #Agrega a nuevos
                        new += 1
                    quantum_time = quantum #Reinicia el quantum
                    imprimir_en_posicion(0, 80, f' < N° Procesos nuevos: {new} > ') #Imprime 
                    limpiar(3,8)    #Limpia las filas en actuales
                    fila = 3
                    for element in grupito:       #Actualiza la actual cola
                        imprimir_en_posicion(fila, 0,f' {element.process_id}\t  {element.time}\t  {element.time_run}')
                        fila += 1    
                    break  
                ejecucion.time_run += 1
                imprimir_en_posicion(13, 0, f'-Tiempo TRA: {ejecucion.time_run}            ')
                imprimir_en_posicion(14, 0, '                 ')  #Limpia antes de mostrar
                imprimir_en_posicion(14, 0, f'-Tiempo RES: {ejecucion.time-ejecucion.time_run}        ')
                contador += 1
                quantum_time -= 1
                ejecucion.wait_time += 1
                imprimir_en_posicion(2, 85, f' < Contador: {contador} >')  #Muestra el contador
                imprimir_en_posicion(3, 85, f' < Quantum: {quantum_time} >')  #Muestra el Quantum
                time.sleep(0.5)
                if key_i == True:
                    #if keyboard.is_pressed('i'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < INTERRUPCION >')  #Muestra el contado
                    quantum_time = quantum #Reinicia el quantum
                    t = threading.Thread(target=bloqueado, args=(ejecucion,pos_fila,)) #Subproceso bloqueados
                    t.start() 
                    pausa.set()
                    if pos_fila == 15:  #Reinicio de bloqueados
                        pos_fila = 11
                    else:
                        pos_fila += 1
                    imprimir_en_posicion(9, 90, ' '*40)  #Limpia antes de mostrar
                    imprimir_en_posicion(9, 90, f'\t\t< BLOQUEADO >')  #Muestra el contador
                    #elementos.append(ejecucion)
                    interrupted = True
                    key_i = False
                    break
                if key_e == True:
                    #if keyboard.is_pressed('e'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < ERROR >')  #Muestra el contador
                    ejecucion.result = 'Error'
                    key_e = False
                    quantum_time = quantum #Reinicia el quantum
                    break
                if key_p == True:
                    #if keyboard.is_pressed('p'):  # Verifica si la tecla "p" ha sido presionada
                    imprimir_en_posicion(7, 90, ' '*40)  #Limpia antes de mostrar
                    imprimir_en_posicion(8, 90, ' '*40)  #Limpia antes de mostrar
                    #imprimir_en_posicion(10, 90, ' '*40)  #Limpia antes de mostrar
                    imprimir_en_posicion(7, 90, f'\t\t< PAUSA >')  #Muestra el contador
                    #imprimir_en_posicion(16, 90, f'\t\t{bloqueados}')  #Imprime
                    pausa.clear() #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    pausa.set()   #Despausa los subprocesos
                    imprimir_en_posicion(7, 90, ' '*40)  #Limpia antes de mostrar
                    imprimir_en_posicion(7, 90, f'\t\t< CONTINUANDO >')  #Muestra el contador
                    imprimir_en_posicion(8, 90, ' '*40)  #Limpia antes de mostrar
                    key_p = False
                if key_n == True:
                    process+=1
                    new_process = (Process(process)) #Crea un nuevo proceso 
                    new_process.time_arrival = contador          

                    if (cantOcupados() + len(grupito)) < 4 :        #Si hay menos de 5 procesos en cola
                        if len(grupito) < 4:
                            grupito.append(new_process) #Agrega a la cola
                        else:
                            elementos.append(new_process)
                            
                    else: #Si hay mas de 5 procesos en la cola
                        elementos.append(new_process) #Agrega a nuevos
                        new += 1 
                    imprimir_en_posicion(0, 80, f' < N° Procesos nuevos: {new} > ') #Imprime 
                    limpiar(3,8)    #Limpia las filas en actuales
                    fila = 3
                    for element in grupito:       #Actualiza la actual cola
                        printListos(element, fila)
                        fila += 1    
                    #imprimir_en_posicion(5, 90, f'\t\t{new_process.process_id}') #Mensaje para determinar el ID del nuevo proceso
                    key_n = False
                       
                    key_n = False
                if key_b == True:
                    tecla_b()
                    key_b = False  
                
            if not interrupted:      #Si no se interrumpio 
                ejecucion.completion_time = contador  #Tiempo de finalizacion
                ejecucion.return_time = (ejecucion.completion_time-ejecucion.time_arrival) #Tiempo de retorno
                ejecucion.wait_time = (ejecucion.return_time-ejecucion.time_run) #Tiempo de espera
                lis.append(ejecucion)
                imprimir_en_posicion(16, 1, '------------------------- < Terminados > --------------------------')
                imprimir_en_posicion(17, 1, '>ID\t>Operacion\t>Resultado\t\t\tTL\tTF\tTR\tTRES\tTE\tTS')                
                count += 1
                if len(elementos) != 0:
                    next = elementos.pop(0) #Se añade el proximo proceso
                    next.time_arrival = contador     #Tiempo de llegada 
                    grupito.append(next)
                if new != 0:
                    new -= 1
                fila_term = 18
                for terminados in lis:   #Muestra cada uno de los procesos terminados
                    idString = resize_string(' ' + str(terminados.process_id),4)
                    operationString = resize_string(' ' + terminados.opString,15)
                    resultString = resize_string(' ' + str(terminados.result),8)
                    time_arrival = resize_string(str(terminados.time_arrival),4)
                    completion_time = resize_string(str(terminados.completion_time),4)
                    return_time = resize_string(str(terminados.return_time),4)
                    response_time = resize_string(str(terminados.response_time),4)
                    wait_time = resize_string(str(terminados.wait_time),4)
                    time_run = resize_string(str(terminados.time_run),4)
                    imprimir_en_posicion(fila_term, 1, f'{idString}\t{operationString}\t{resultString}\t\t\t{time_arrival}\t{completion_time}\t{return_time}\t{response_time}\t{wait_time}\t{time_run}')
                    fila_term += 1
            else:                    #Si hay interrupcion 
                continue
            #limpiar(16,100) #Limpia los terminados
        
        limpiar(9,15)   #Limpia las filas en ejecucion al terminar el programa
        limpiar(2,8)    #Limpia las filas en actuales
    imprimir_en_posicion(18+len(lis), 1, '') #"Posiciona el cursor" para que se imprima al final del programa
    end = True
    print('Press Enter to finish')

def key():  #Key thread
    global key_i,key_e,key_p,key_n,end,key_b
    new_process = []
    while not end:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'i':
            #print("INTERRUMPED")
            key_i = True
        if event.event_type == keyboard.KEY_DOWN and event.name == 'e':
            #print("ERROR")
            key_e = True
        if event.event_type == keyboard.KEY_DOWN and event.name == 'p':
            #print("PAUSE")
            key_p = True
        if event.event_type == keyboard.KEY_DOWN and event.name == 'n':
            #print("NEW")
            key_n = True
        if event.event_type == keyboard.KEY_DOWN and event.name == 'b':
            #print("Table")
            key_b = True
        #if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
         #   print("<Finished process>")
    
def main():
    global process
    subkey = threading.Thread(target=key) #Key thread
    subkey.start() #Key thread start
    os.system('cls')
    process = input("Introduzca la cantidad de procesos a realizar: ")
    while not re.match("^[1-9]+\d*$", process):
        process = input("Introduzca NUEVAMENTE la cantidad de procesos a realizar: ")
    process = int(process)
    
    quantum = input("Introduzca el QUANTUM: ")
    while not re.match("^[1-9]+\d*$", quantum):
        quantum = input("Introduzca NUEVAMENTE el QUANTUM: ")
    quantum = int(quantum)
    
    os.system('cls')
    listProcess = []
    for count_process in range(1,process+1):
        listProcess.append(Process(count_process))

    #print(listProcess)
    
    for i in listProcess:
        print(i.print())

    #input('Press enter')
    os.system('cls')
    console(listProcess,quantum)
    
if __name__ == "__main__":
    main()
