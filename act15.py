import math,re,time,random,keyboard,os, threading, pickle
from termcolor import colored
pausa = threading.Event()
end = False #END Thread
key_i = False
key_e = False
key_p = False
key_n = False
key_b = False
key_s = False
key_r = False

class Process:
    def __init__(self,id):
        self.process_id = id    #ID
        self.time = random.randint(20, 40)  #TME
        self.time_arrival = 0 #Time of Arrival
        self.completion_time = 0 #Completion Time
        self.return_time = 0  #Return time
        self.response_time = 0  #Response time
        self.band_response = False  #Band response time
        self.wait_time = 0 #Wait time 
        self.time_run = 0   #Time running = TT
        self.blocked_time = 0 #Blocked time
        self.size = random.randint(6, 26)  #Process Size

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
        return f'ID: {self.process_id} TME: {self.time} TT : {self.time_run} {self.opString} = {self.result} TL : {self.time_arrival} TF : {self.completion_time} TR : {self.return_time} TRES : {self.response_time} TW : {self.wait_time} BAND : {self.band_response} BT : {self.blocked_time} SIZE : {self.size}'


#---------------------------------------------------------------------------------------------------------
#CONSOLE



def console(elementos,quantum):
    global key_i,key_e,key_p,end,key_n,process,key_b,new,key_s,key_r
    lis = []      #Procesos Terminados
    memory = []   #System memory 
    contador = 0  #Contador global
    grupito = []  #Grupo de 5 procesos
    count = 0     #Process Count
    process = len(elementos) #Processes
    pos_fila = 3 #pos_fila process
    bloqueados = [(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0)] #Procesos Bloqueados
    quantum_time = quantum
    new = 0      #Actual processes
    suspended = []  #Processes suspended 
    recuperados = [] 
    
    for i in range(40): #Declaration Memory
        memory.append([0,0,"---"]) #List = [Size,ID,State]
    with open("suspendidos.pkl", 'wb'):  #Initially empty the file
            pass
 
    def ocuparMemoria(size,id,state):
        #Ocupa espacios en la memoria 
        libres = 0
        frames = math.ceil(size / 5) #Cantidad de marcos a ocupar donde size es el tamaño de proceso
        if((size % 5) != 0): #Si el tamaño del ultimo frame es distinto a 5 (1-4/5)
            frame = size % 5 
        else:              #Todos los frames son del mismo tamaño (5/5)
            frame = 5
        for i in range(len(memory)): #Valida cuantos espacios libres hay en memoria 
            if(memory[i][1] == 0):
                libres += 1
        #print(libres)
        if((libres - frames) >= 0): #Si el proceso cabe en memoria (cantidad de frames)
            ocupados = 0 #Marcos ocupados 
            for i in range(len(memory)): #Se recorre la memoria
                    if(memory[i][1] == 0):
                        memory[i][0] = 5  #Size default
                        memory[i][1] = id
                        memory[i][2] = state
                        ocupados += 1    
                        if(ocupados == frames):
                            memory[i][0] = frame #Actualiza el tamaño de ultimo fram
                            return True;
        else:
            return False;
    
    def desocuparMemoria(id):
        #Desocupa espacios en la memoria 
        for i in range(len(memory)): #Se recorre la memoria 
            if(memory[i][1] == id): #Se busca las coincidencias del ID en memoria del terminado para liberar espacio 
                memory[i][0] = 0
                memory[i][1] = 0
                memory[i][2] = "---"
    
    def paginacion(): #Paginacion 
            #Se imprime la estructura de la paginacion
            for i in range(1,15): #Limpia las columnas 1-15 desde la columuna 65 en adelante (paginacion)
                imprimir_en_posicion(i, 65, f' '*135) #Marcos columna 65
            imprimir_en_posicion(0, 65, f'\033[32mMarco\033[0m   Size    ID     EST') #Marcos columna 65
            imprimir_en_posicion(0, 100, f'\033[32mMarco\033[0m   Size    ID     EST') #Marcos columna 100
            imprimir_en_posicion(0, 135, f'\033[32mMarco\033[0m   Size    ID     EST') #Marcos columna 135
            for i in range(1,45): #IMP Paginacion 
                if i <= 15:
                    if i <= 9:
                        imprimir_en_posicion(i+1, 65, f'\033[33m|0{i}|\033[0m    {memory[i-1][0]}/5     {memory[i-1][1]}      {memory[i-1][2]}     \033[32m|\033[0m') #Marco 1-9
                    else:
                        imprimir_en_posicion(i+1, 65, f'\033[33m|{i}|\033[0m    {memory[i-1][0]}/5     {memory[i-1][1]}      {memory[i-1][2]}     \033[32m|\033[0m') #Marco 10-15
                elif i > 15 and i <= 30:
                    imprimir_en_posicion(i-14, 100, f'\033[33m|{i}|\033[0m    {memory[i-1][0]}/5     {memory[i-1][1]}      {memory[i-1][2]}     \033[32m|\033[0m') #Marco 16-30
                else:
                    if i > 40:
                        imprimir_en_posicion(i-28, 135, f'\033[33m|{i}|\033[0m    0/5     S/D    \033[38;5;208mS.O\033[0m     \033[32m|\033[0m') #S.O Recerved = Marco 41-44
                    else:
                        imprimir_en_posicion(i-28, 135, f'\033[33m|{i}|\033[0m    {memory[i-1][0]}/5     {memory[i-1][1]}      {memory[i-1][2]}     \033[32m|\033[0m') #Marco 31-40


    def resize_string(input_string, new_size): #Resize string for table
        if new_size < len(input_string):
            return input_string[:new_size] #Cut the string until new_size
        elif new_size > len(input_string):
            return input_string + ' ' * (new_size - len(input_string)) #Fill out the input_string to have new len of string
        else:
            return input_string
        
    def bloqueado(proceso,pos_fila):   #Estado bloqueado
            global new,key_s
            TT = 0
            for i in range(len(memory)):   #Actualiza el estado del proceso bloquedo en memoria 
                    if(memory[i][1] == proceso.process_id):
                        memory[i][2] = "\033[91mBlo\033[0m"
            paginacion()    #Actualiza la paginacion 
            imprimir_en_posicion(0, 0, '\033[38;5;208m-------------------------- < Listos > -------------------------\033[0m')
            imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT\t>Size')
            if pos_fila == 3: #Primer bloqueado
                index = 0 #ID process
            elif pos_fila == 4: #Segundo bloqueado
                index = 1 #ID process
            elif pos_fila == 5: #Tercer bloqueado
                index = 2 #ID process
            elif pos_fila == 6: #Cuarto bloqueado
                index = 3 #ID process
            elif pos_fila == 7: #5 bloqueado
                index = 4 #ID process
            elif pos_fila == 8: #C6 bloqueado
                index = 5 #ID process
            elif pos_fila == 9: #7 bloqueado
                index = 6 #ID process
            elif pos_fila == 10: #8 bloqueado
                index = 7 #ID process
            elif pos_fila == 11: #9 bloqueado
                index = 8 #ID process
            elif pos_fila == 12: #10 bloqueado
                index = 9 #ID process
            elif pos_fila == 13: #11 bloqueado
                index = 10 #ID process
            elif pos_fila == 14: #12 bloqueado
                index = 11 #ID process
            else:           #13 bloqueado
                index = 12 #ID process
            while TT != 8:  #Tiemp de 8 seg
                pausa.wait() #Detiene temporalmente al subproceso
                TT += 1
                if key_s == True: #Al detectar la tecla s
                    for i in range(len(memory)):       #Cambia el estado del proceso bloqueado a "Suspendido"
                        if proceso.process_id == memory[i][1]:
                            memory[i][2] = "\033[91mSus\033[0m"
                    paginacion()
                    suspended.append(proceso)
                    with open('suspendidos.pkl', 'wb') as archivo: #Archivo binario en modo escritura 
                          pickle.dump(suspended, archivo) #Almacena en el archivo el proceso suspendido 
                    key_s = False
                    imprimir_en_posicion(pos_fila, 35, f' '*30) #Limpiar
                    return
                    #x = 80
                    #for s in suspended:
                    #    imprimir_en_posicion(35, x, f'{s.process_id}') #Limpiar
                    #    x+=5
                proceso.blocked_time = TT
                bloqueados[index] = proceso #Contador actual del proceso bloqueado
                imprimir_en_posicion(pos_fila, 35, f'\t\t>ID: {proceso.process_id} TT-->{proceso.blocked_time} ')
                
                #imprimir_en_posicion(pos, 70, f' < TT {bloqueados[index]} > ')  
                time.sleep(0.5)
            imprimir_en_posicion(pos_fila, 35, f' '*30) #Limpiar
            if TT == 8:  #Si transcurren 8 seg
                #imprimir_en_posicion(18, 80, f' < Proceso añadido {proceso} >')  #Muestra el proceso añadido
                proceso.blocked_time = 0 #Reinicia el contador de bloqueado 
            
                for i in range(len(memory)):   #Actualiza el estado del proceso bloquedo en memoria 
                    if(memory[i][1] == proceso.process_id):
                        memory[i][2] = "\033[94;1mLis\033[0m"
                paginacion()    #Actualiza la paginacion 
                imprimir_en_posicion(0, 0, '\033[38;5;208m-------------------------- < Listos > -------------------------\033[0m')
                imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT\t>Size')
                grupito.append(proceso)
                bloqueados[index] = (0) #Reinicia el tiempo de bloqueo para un nuevo bloquead
                fila = 3
                for element in grupito:       #Actualiza el actual grupo de procesos
                    imprimir_en_posicion(fila, 0,f' {element.process_id}\t  {element.time}\t  {element.time_run}\t {element.size}')
                    fila += 1             
        
    def limpiar(inicial,final):   #Limpia por consola
        for row in range(inicial,final):
            imprimir_en_posicion(row, 0,' ' * 100)

    def imprimir_en_posicion(fila, columna, mensaje):  #Imprime por la posicion mencionada
        # Usar caracteres de escape ANSI para posicionar el cursor
        print(f"\033[{fila};{columna}H{mensaje}", flush=True)
    
    def tecla_r():
        if os.path.getsize('suspendidos.pkl') != 0: #Si contiene procesos suspendidos 
                        with open('suspendidos.pkl', 'rb') as archivo:  #Abre el archivo binario en modo lectura 
                            suspendidos_recuperados = pickle.load(archivo)
                            recuperado = suspendidos_recuperados.pop(0)
                            #imprimir_en_posicion(22, 90, f'ID {recuperado.process_id}')  #Muestra el contador
                            for i in range(len(memory)):
                                    if recuperado.process_id == memory[i][1]:
                                        memory[i][2] = "\033[94;1mLis\033[0m"
                            paginacion()
                            grupito.append(recuperado)
                            if len(suspendidos_recuperados) != 0:   #Si aun hay recuperados, los regresa al archivo 
                                with open('suspendidos.pkl', 'wb') as archivo:
                                    pickle.dump(suspendidos_recuperados, archivo)
                                    #if len(suspended != 0):
                                    suspended.pop(0)
                            else:                       #Sino, vacia el archivo 
                                with open("suspendidos.pkl", 'wb'):  
                                    #imprimir_en_posicion(23, 90, f'vaciado')
                                    #if len(suspended != 0):
                                    suspended.pop(0)
                                    pass
    def tecla_n():
            global process
            process +=1
            new_process = (Process(process)) #Crea un nuevo proceso 
            new_process.time_arrival = contador     
            while True: #Ocupa inicialmente la Memoria
                    initial = new_process
                    band = ocuparMemoria(initial.size,initial.process_id,"\033[94;1mLis\033[0m")
                    if band == True:
                        initial.time_arrival = contador  #Tiempo de llegada de los primeros 5 procesos 
                        grupito.append(initial)   
                        break
                    else:
                        elementos.append(initial)
                        new = len(elementos)
                        imprimir_en_posicion(18, 30, f' < N° Procesos nuevos: {new} > ')
                        break   
    
    def tecla_b(): #Key b Process Table
                    os.system('cls')
                    imprimir_en_posicion(0, 21, '\033[32m> Tabla de Procesos \033[0m')
                    imprimir_en_posicion(2, 0, '\033[94;1m------------------------------------------------------------ < Nuevos > ------------------------------------------------------------\033[0m')
                    imprimir_en_posicion(3, 0, '>ID\t\t>TME\t\t\tOperación\t\tSize')
                    table_row = 4
                    for nuevo in elementos:  #Nuevos 
                        imprimir_en_posicion(table_row, 1, f'{nuevo.process_id}\t\t{nuevo.time}\t\t\t{nuevo.opString}\t\t{nuevo.size}') 
                        table_row += 1
                    imprimir_en_posicion(table_row, 0, '\033[38;5;208m------------------------------------------------------------ < Listos > ------------------------------------------------------------\033[0m')
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '>ID\t\t>TME\t\t\tOperación\t\tSize\t\tTL\t\tTS\t\tTE\t\tTRES')
                    table_row += 1
                    for element in grupito:
                        wait_tim = (contador-element.time_run) #Tiempo de espera actual
                        imprimir_en_posicion(table_row, 1, f'{element.process_id}\t\t{element.time}\t\t\t{element.opString}\t\t{element.size}\t\t{element.time_arrival}\t\t{element.time_run}\t\t{wait_tim}\t\t{element.response_time}') 
                        table_row +=1 
                    imprimir_en_posicion(table_row, 0, '\033[33m------------------------------------------------------------ < Ejecución > ------------------------------------------------------------\033[0m')
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '>ID\t\t>TME\t\t\tOperación\t\tSize\t\tTL\t\tTS\t\tTE\t\tTRES')
                    table_row += 1
                    wait_tim = (contador-ejecucion.time_run) #Tiempo de espera actual
                    imprimir_en_posicion(table_row, 0, f'{ejecucion.process_id}\t\t{ejecucion.time}\t\t\t{ejecucion.opString}\t\t{ejecucion.size}\t\t{ejecucion.time_arrival}\t\t{ejecucion.time_run}\t\t{wait_tim}\t\t{ejecucion.response_time}')
                    if bloqueados[4] != 0 and bloqueados[3] != 0 and bloqueados[2] != 0 and bloqueados[1] != 0 and bloqueados[4] != 0:
                        imprimir_en_posicion(table_row, 0, f' '*300)
                    table_row += 1
                    #imprimir_en_posicion(10, 90, f'{bloqueados}')
                    imprimir_en_posicion(table_row, 0, '\033[91m------------------------------------------------------------ < Bloqueados > ------------------------------------------------------------\033[0m')
                    table_row += 1
                    imprimir_en_posicion(table_row, 0, '>ID\t\tRestante\t\tOperación\t\tSize\t\tTL\t\tTS\t\tTE\t\tTRES')
                    table_row += 1
                    total_TT = 8 #Maximo transcurrido
                    for blocked in bloqueados:
                        if blocked != 0:
                            wait_tim = (contador-blocked.time_run) #Tiempo de espera actual
                            imprimir_en_posicion(table_row, 1, f'{blocked.process_id}\t\t{total_TT-blocked.blocked_time}\t\t\t{blocked.opString}\t\t{blocked.size}\t\t{blocked.time_arrival}\t\t{blocked.time_run}\t\t{wait_tim}\t\t{blocked.response_time}')
                            table_row += 1
                    imprimir_en_posicion(table_row, 0, '\033[32m------------------------------------------------------------ < Terminados > ------------------------------------------------------------\033[0m')
                    table_row += 1  
                    imprimir_en_posicion(table_row, 0, '>ID\t\t>Operacion\t\t\t>Resultado\tSize\tTL\tTF\tTR\tTRES\tTE\tTS')
                    table_row += 1
                    for terminados in lis:
                        imprimir_en_posicion(table_row, 1, f'{terminados.process_id}\t\t{terminados.opString}\t\t\t{terminados.result}\t\t{terminados.size}\t{terminados.time_arrival}\t{terminados.completion_time}\t{terminados.return_time}\t{terminados.response_time}\t{terminados.wait_time}\t{terminados.time_run}')
                        table_row += 1
                    #imprimir_en_posicion(1, 90, f'{bloqueados}') 
                    pausa.clear() #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    os.system('cls')
                    imprimir_en_posicion(18, 30, f' < N° Procesos nuevos: {new} > ')
                    imprimir_en_posicion(0, 0, '\033[38;5;208m-------------------------- < Listos > -------------------------\033[0m')
                    imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT')
                    imprimir_en_posicion(19, 35, f' < Contador: {contador} >')  #Muestra el contador
                    fila_b = 3
                    for element in grupito:       #Actualiza la actual cola
                        imprimir_en_posicion(fila_b, 0,f' {element.process_id}\t  {element.time}\t  {element.time_run}\t  {element.size}')
                        fila_b += 1
                    imprimir_en_posicion(16, 0, '-\033[33m-------------------- < Proceso en Ejecución > -----------------\033[0m')
                    imprimir_en_posicion(17, 0, f'                                       ')
                    imprimir_en_posicion(18, 0, f'-ID: {ejecucion.process_id}')
                    imprimir_en_posicion(19, 0, f'-Operacion-> {ejecucion.opString}')
                    imprimir_en_posicion(20, 0, f'-Tiempo MXE: {ejecucion.time}')
                    imprimir_en_posicion(21, 0, f'-Tiempo TRA: {ejecucion.time_run}            ')
                    imprimir_en_posicion(22, 0, '                 ')  #Limpia antes de mostrar
                    imprimir_en_posicion(22, 0, f'-Tiempo RES: {ejecucion.time-ejecucion.time_run}        ')
                    imprimir_en_posicion(24, 1, '\033[32m---------------------------------------------------- < Terminados > ----------------------------------------------------\033[0m')
                    imprimir_en_posicion(25, 1, '>ID\t\t>Operacion\t\t\t>Resultado\tTL\tTF\tTR\tTRES\tTE\tTS\tSize')
                    fila_term_b = 26       
                    for terminados in lis:   #Muestra cada uno de los procesos terminados
                        idString = resize_string(' ' + str(terminados.process_id),18)
                        operationString = resize_string(terminados.opString,32)
                        resultString = resize_string(' ' + str(terminados.result),14)
                        time_arrival = resize_string(' ' + str(terminados.time_arrival),7)
                        completion_time = resize_string(' ' + str(terminados.completion_time),8)
                        return_time = resize_string(' ' + str(terminados.return_time),8)
                        response_time = resize_string(' ' + str(terminados.response_time),8)
                        wait_time = resize_string(' ' + str(terminados.wait_time),8)
                        time_run = resize_string(' ' + str(terminados.time_run),8)
                        size = resize_string(' ' + str(terminados.size),8)
                        imprimir_en_posicion(fila_term_b, 1, f'{idString}{operationString}{resultString}{time_arrival}{completion_time}{return_time}{response_time}{wait_time}{time_run}{size}')
                        fila_term_b += 1
                    pausa.set()   #Despausa los subprocesos
                    imprimir_en_posicion(2, 35, f'\t\t< CONTINUANDO >')  #Muestra el contador
                    #imprimir_en_posicion(8, 90, '                                       ')  
                      
 
 
 
 
    while count != process:    #Mientras haya procesos pendientes
        #-------------------------------------------------------------------------------
        while (len(grupito) >= 0):               #Se muestra cada elemento del grupo
            interrupted = False
            limpiar(17,23)
            if key_r == True:     #Al detectar una tecla R
                tecla_r()
                key_r = False
            if key_n == True:   
                tecla_n()
                key_n = False
            while True: #Agrega procesos a la memoria 
                if len(elementos) != 0: #Si hay elementos en nuevos
                   initial = elementos.pop(0)
                   band = ocuparMemoria(initial.size,initial.process_id,"\033[94;1mLis\033[0m") #Se asigna memoria al proceso
                   if band == True:
                       initial.time_arrival = contador  #Tiempo de llegada de los primeros 5 procesos 
                       grupito.append(initial)   
                   else: #Si el proceso no cabe en memoria, regresa a nuevos
                       elementos.insert(0,initial)
                       break         
                else:
                    break
            new = len(elementos)
            paginacion()
            imprimir_en_posicion(18, 30, f' < N° Procesos nuevos: {new} > ')
            imprimir_en_posicion(0, 0, '\033[38;5;208m-------------------------- < Listos > -------------------------\033[0m')
            imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT\t>Size')
            if len(grupito) == 0:      #Si el grupo esta vacio (todos estan bloqueados) no se muestra nada por consola
                contador += 1
                imprimir_en_posicion(19, 35, f' < Contador: {contador} >')  #Muestra el contador
                imprimir_en_posicion(20, 35, f' < Quantum: {quantum_time} >')  #Muestra el contador
                imprimir_en_posicion(21, 35, f' '*30)  #Muestra el contad
                if(len(elementos) > 0):
                    imprimir_en_posicion(21, 35, f' \033[32m> Next:\033[0m {elementos[0].process_id} \033[32mSize:\033[0m \033[33m{elementos[0].size}\033[0m')  #Muestra el contad
                else:
                    imprimir_en_posicion(21, 35, f' \033[32m> Next:\033[0m -- \033[32mSize:\033[0m -  ')  #Muestra el contad
                for i in range(9,16): #Limpia las filas 9-16
                    imprimir_en_posicion(i, 0, f' '*30) 
                time.sleep(0.5)
                if key_p == True:
                #if keyboard.is_pressed('p'):  # Verifica si la tecla "p" ha sido presionada
                    #imprimir_en_posicion(10, 90, '                                      ')  #Limpia antes de mostrar
                    imprimir_en_posicion(2, 35, '                    ')  #Limpia antes de mostrar
                    imprimir_en_posicion(2, 35, f'\t\t< PAUSA >')  #Muestra el contador
                    #imprimir_en_posicion(16, 90, f'\t\t{bloqueados}')  #Imprime
                    
                    pausa.clear()  #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    pausa.set()    #Despausa los subprocesos
                    imprimir_en_posicion(2, 35, f'\t\t< CONTINUANDO >')  #Muestra el contador
                    #imprimir_en_posicion(8, 90, '                                       ')  #Limpia antes de mostrar
                    key_p = False
                if key_b == True:
                    tecla_b()
                    key_b = False
                continue
            else:
                ejecucion = grupito.pop(0) #Sino, obtiene el mas reciente del grupito para mostrar
                for i in range(len(memory)):   #Actualiza el estado del proceso en ejecucion actual en memoria 
                    if(memory[i][1] == ejecucion.process_id):
                        memory[i][2] = "\033[33mEje\033[0m"
                paginacion()    #Actualiza la paginacion 
                imprimir_en_posicion(0, 0, '\033[38;5;208m-------------------------- < Listos > -------------------------\033[0m')
                imprimir_en_posicion(2, 0, '>ID\t>TME\t>TT\t>Size')
                #imprimir_en_posicion(13, 80, f'{ejecucion.band_response}')  #Muestra el contador
                if ejecucion.band_response == False:
                    ejecucion.response_time = (contador-ejecucion.time_arrival) #Tiempo de respuesta 
                    ejecucion.band_response = True
    
            for i in range(3,16): #Limpia las filas 3-16
                imprimir_en_posicion(i, 0, f' '*30) 
            fila = 3
            for element in grupito:       #Actualiza la actual cola
                imprimir_en_posicion(fila, 0,f' {element.process_id}\t  {element.time}\t  {element.time_run}\t {element.size}')
                fila += 1
            '''if len(grupito) > 3: #Interrupcion para ver cuantos entran en el grupito (entran 4)
                input(' ')'''
            #--------------------------------------------------------------------------------------------------------
            #limpiar(8,13)   #Limpia las filas en ejecucion
            imprimir_en_posicion(16, 0, '\033[33m-------------------- < Proceso en ejecución > -----------------\033[0m')
            imprimir_en_posicion(18, 0, f' '*25)
            imprimir_en_posicion(18, 0, f'\033[33m-ID: {ejecucion.process_id}\033[0m       >Size: \033[32m{ejecucion.size}\033[0m')
            imprimir_en_posicion(19, 0, f'-Operacion-> {ejecucion.opString}')
            imprimir_en_posicion(20, 0, f'-Tiempo MXE: {ejecucion.time}')
            #TT = ejecucion.time_run
            imprimir_en_posicion(21, 0, '                 ')  #Limpia antes de mostrar
            while  ejecucion.time_run < ejecucion.time:
                if quantum_time <= 0: #SI el quantum es 0 
                    interrupted = True
                    for i in range(len(memory)):   #Actualiza el estado del proceso en ejecucion actual en memoria
                        if(memory[i][1] == ejecucion.process_id):
                            memory[i][2] = "\033[94;1mLis\033[0m"
                    grupito.append(ejecucion) #Agrega a la cola
                    #else: #Si hay mas de 5 procesos en la cola
                    #    elementos.append(ejecucion) #Agrega a nuevos
                    #    new += 1
                    quantum_time = quantum #Reinicia el quantum
                    '''
                    imprimir_en_posicion(18, 30, f' < N° Procesos nuevos: {new} > ') #Imprime 
                    if len(elementos) != 0:
                        last = elementos.pop(0)
                        if (ocuparMemoria(last.size,last.process_id,"\033[94;1mLis\033[0m") == True):
                            imprimir_en_posicion(18, 80, f' < Se ocupo espacio > ') #Imprime 
                            paginacion()
                        else:
                            elementos.insert(0,last)
                    '''
                    limpiar(3,15)
                    fila = 3
                    for element in grupito:       #Actualiza la actual cola
                        imprimir_en_posicion(fila, 0,f' {element.process_id}\t  {element.time}\t  {element.time_run}\t  {element.size}')
                        fila += 1    
                    break  
                ejecucion.time_run += 1
                imprimir_en_posicion(21, 0, f'-Tiempo TRA: {ejecucion.time_run}            ')
                imprimir_en_posicion(22, 0, '                 ')  #Limpia antes de mostrar
                imprimir_en_posicion(22, 0, f'-Tiempo RES: {ejecucion.time-ejecucion.time_run}        ')
                contador += 1
                quantum_time -= 1
                ejecucion.wait_time += 1
                imprimir_en_posicion(19, 35, f' < Contador: {contador} >')  #Muestra el contador
                imprimir_en_posicion(20, 35, f' < Quantum: {quantum_time} >')  #Muestra el contad
                imprimir_en_posicion(18, 30, f' < N° Procesos nuevos: {new} > ')
                imprimir_en_posicion(21, 35, f' '*30)  #Muestra el contad
                if(len(elementos) > 0):
                    imprimir_en_posicion(21, 35, f' \033[32m> Next:\033[0m {elementos[0].process_id} \033[32mSize:\033[0m \033[33m{elementos[0].size}\033[0m')  #Muestra el contad
                else:
                    imprimir_en_posicion(21, 35, f' \033[32m> Next:\033[0m -- \033[32mSize:\033[0m -  ')  #Muestra el contad
                time.sleep(0.5)
                if key_i == True:
                    #if keyboard.is_pressed('i'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < INTERRUPCION >')  #Muestra el contado
                    quantum_time = quantum #Reinicia el quantum
                    t = threading.Thread(target=bloqueado, args=(ejecucion,pos_fila,)) #Subproceso bloqueados
                    t.start() 
                    pausa.set()
                    if pos_fila == 15:  #Reinicio de bloqueados
                        pos_fila = 3
                    else:
                        pos_fila += 1
                    imprimir_en_posicion(2, 35, '                      ')  #Limpia antes de mostrar
                    imprimir_en_posicion(2, 35, f'\t\t< BLOQUEADO >')  #Muestra el contador
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
                    #imprimir_en_posicion(8, 90, '                                      ')  #Limpia antes de mostrar
                    imprimir_en_posicion(2, 35, '                     ')  #Limpia antes de mostrar
                    imprimir_en_posicion(2, 35, f'\t\t< PAUSA >')  #Muestra el contador
                    #imprimir_en_posicion(16, 90, f'\t\t{bloqueados}')  #Imprime
                    pausa.clear() #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    pausa.set()   #Despausa los subprocesos
                    imprimir_en_posicion(2, 35, f'\t\t< CONTINUANDO >')  #Muestra el contador
                    #imprimir_en_posicion(8, 90, '                                       ')  #Limpia antes de mostrar
                    key_p = False
                if key_n == True:   
                    tecla_n()
                    ''' 
                    for element in elementos: #Comprueba si el proceso en memoria esta en nuevos
                        for i in range(len(memory)):
                                #imprimir_en_posicion(24, 85, f' < Elementos : {element.process_id} > ') #Imprime 
                                #imprimir_en_posicion(29, 85, f' < Memoria : {memory[i][1]} > ') #Imprime 
                                if(element.process_id == memory[i][1]):
                                    imprimir_en_posicion(20, 85, f' < N° Repetido : {element.process_id} > ') #Imprime 
                                    desocuparMemoria(element.process_id)       #Si esta en nuevos, el proceso no esta en memoria   
                                    break 
                    '''
                    #imprimir_en_posicion(10, 90, f'\t\t{new_process.process_id}')
                    key_n = False
                if key_b == True:
                    tecla_b()
                    key_b = False  
                if key_s == True:
                    key_s = False
                if key_r == True:
                    tecla_r()
                    key_r = False
                
            if not interrupted:      #Si no se interrumpio 
                ejecucion.completion_time = contador  #Tiempo de finalizacion
                ejecucion.return_time = (ejecucion.completion_time-ejecucion.time_arrival) #Tiempo de retorno
                ejecucion.wait_time = (ejecucion.return_time-ejecucion.time_run) #Tiempo de espera
                desocuparMemoria(ejecucion.process_id) #Desocupa todos los frames relacionados con el proceso que terminó
                lis.append(ejecucion)
                imprimir_en_posicion(24, 1, '\033[32m---------------------------------------------------- < Terminados > ----------------------------------------------------\033[0m')
                imprimir_en_posicion(25, 1, '>ID\t\t>Operacion\t\t\t>Resultado\tTL\tTF\tTR\tTRES\tTE\tTS\tSize')
                count += 1
               # if len(elementos) != 0:  #Añade nuevos procesos a memoria 
                #    next = elementos[0]
                 #   band = ocuparMemoria(next.size,next.process_id,"Lis")
                  #  if band == True:
                   #     elementos.pop(0)
                    #   grupito.append(next)
                if new != 0:
                    new -= 1
                fila_term = 26
                for terminados in lis:   #Muestra cada uno de los procesos terminados
                    idString = resize_string(' ' + str(terminados.process_id),18)
                    operationString = resize_string(terminados.opString,32)
                    resultString = resize_string(' ' + str(terminados.result),14)
                    time_arrival = resize_string(' ' + str(terminados.time_arrival),7)
                    completion_time = resize_string(' ' + str(terminados.completion_time),8)
                    return_time = resize_string(' ' + str(terminados.return_time),8)
                    response_time = resize_string(' ' + str(terminados.response_time),8)
                    wait_time = resize_string(' ' + str(terminados.wait_time),8)
                    time_run = resize_string(' ' + str(terminados.time_run),8)
                    size = resize_string(' ' + str(terminados.size),8)
                    imprimir_en_posicion(fila_term, 1, f'{idString}{operationString}{resultString}{time_arrival}{completion_time}{return_time}{response_time}{wait_time}{time_run}{size}')
                    fila_term += 1
                if os.path.getsize('suspendidos.pkl') == 0: #Si el archivo esta vacio
                    if(len(grupito) == 0):                  #Y ademas, el grupito esta vacio
                        paginacion()
                        break                               #Termina el programa
            else:                    #Si hay interrupcion 
                continue
            #limpiar(16,100) #Limpia los terminados
        break
    imprimir_en_posicion(18+len(lis), 1, '') #"Posiciona el cursor" para que se imprima al final del programa
    end = True
    
    print('Press Enter to finish')

def key():  #Key thread
    global key_i,key_e,key_p,key_n,end,key_b,key_s,key_r
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
        if event.event_type == keyboard.KEY_DOWN and event.name == 's':
            #print("Suspended")
            key_s = True
        if event.event_type == keyboard.KEY_DOWN and event.name == 'r':
            #print("Return")
            key_r = True
        #if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
            #print("<Finished process>")
    
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
    
 
    for i in listProcess:
        print(i.print())
    #input('Press enter')
    os.system('cls')
    console(listProcess,quantum)
    
if __name__ == "__main__":
    main()
