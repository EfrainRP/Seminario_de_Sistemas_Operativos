import math,re,time,random,keyboard,os, threading
pausa = threading.Event()
end = False #END Thread
key_i = False
key_e = False
key_p = False

class Process:
    def __init__(self,id):
        self.process_id = id    #ID
        self.time = random.randint(8, 16)  #TME
        
        self.time_arrival = 0 #Time of Arrival
        self.completion_time = 0 #Completion Time
        self.return_time = 0  #Return time
        self.response_time = 0  #Response time
        self.band_response = False  #Band response time
        self.wait_time = 0 #Wait time 
        self.time_run = 0   #Time running = TT

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
        return f'ID: {self.process_id} TME: {self.time} TT : {self.time_run} {self.opString} = {self.result} TL : {self.time_arrival} TF : {self.completion_time} TR : {self.return_time} TRES : {self.response_time} TW : {self.wait_time} BAND : {self.band_response}'


#---------------------------------------------------------------------------------------------------------
#CONSOLE



def console(elementos):
    global key_i,key_e,key_p,end
    lis = []      #Procesos Terminados
    contador = 0  #Contador global
    grupito = []  #Grupo de 5 procesos
    count = 0     #Process Count
    process = len(elementos) #Processes
    posBloqueo = 9

    def resize_string(input_string, new_size): #Resize string for table
        if new_size < len(input_string):
            return input_string[:new_size] #Cut the string until new_size
        elif new_size > len(input_string):
            return input_string + ' ' * (new_size - len(input_string)) #Fill out the input_string to have new len of string
        else:
            return input_string
        
    def bloqueado(proceso,pos):   #Estado bloqueado
            TT = 0
            
            while TT != 8:  #Tiempo de 8 seg
                pausa.wait() #Detiene temporalmente al subproceso
                TT += 1
                #imprimir_en_posicion(0, 70, f' < TT {TT} > ')
                imprimir_en_posicion(9, 70, f' < Bloqueados > ')
                imprimir_en_posicion(pos, 74, f'ID: {proceso.process_id}  TT {TT}  ')
                time.sleep(0.5)
            if TT == 8:  #Si transcurren 8 seg
                #imprimir_en_posicion(18, 80, f' < Proceso añadido {proceso} >')  #Muestra el proceso añadido
                grupito.append(proceso)
                limpiar(3,8)    #Limpia las filas en actuales
                imprimir_en_posicion(pos,70, " "*15)    #Limpia las filas en bloqueados
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
        
    if len(elementos) > 5: #Procesos mayores a 5
        for i in range(5): #Toma los primeros 5 procesos 
           initial = elementos.pop(0)
           initial.time_arrival = contador  #Tiempo de llegada de los primeros 5 procesos 
           grupito.append(initial)    
        new = process-5 #New Process
    else: #Procesos menores a 6
        for i in range(len(elementos)): #Toma todos los procesos 
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
                imprimir_en_posicion(6, 80, f' < Contador: {contador} >')  #Muestra el contador
                #limpiar(9,15)   #Limpia las filas en ejecucion
                for row in range(9,15):
                    imprimir_en_posicion(row, 0, " "*15)  #Limpia
                time.sleep(0.5)
                if key_p == True:
                #if keyboard.is_pressed('p'):  # Verifica si la tecla "p" ha sido presionada
                    imprimir_en_posicion(16, 80, " "*15)  #Limpia antes de mostrar
                    imprimir_en_posicion(14, 80, f' < PAUSA >       ')  #Imprime 
                    imprimir_en_posicion(14, 80, "  "*15)  #Limpia antes de mostrar
                    pausa.clear()  #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    pausa.set()    #Despausa los subprocesos
                    imprimir_en_posicion(16, 80, f' < CONTINUANDO >')  #Imprime 
                    imprimir_en_posicion(14, 80, "  "*15)  #Limpia antes de mostrar
                    key_p = False
                continue
            else:
                ejecucion = grupito.pop(0) #Sino, obtiene el mas reciente del grupito para mostrar
                #mprimir_en_posicion(13, 80, f'{ejecucion.band_response}')  
                if ejecucion.band_response == False:
                    ejecucion.response_time = (contador-ejecucion.time_arrival) #Tiempo de respuesta 
                    ejecucion.band_response = True
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
            imprimir_en_posicion(9, 0, " "*15)
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
                ejecucion.wait_time += 1
                imprimir_en_posicion(6, 80, f' < Contador: {contador} >')  #Muestra el contador
                time.sleep(0.5)
                if key_i == True:
                    #if keyboard.is_pressed('i'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < INTERRUPCION >')  #Muestra el contado
                    if posBloqueo<=13:
                        posBloqueo+=1
                    else:
                        posBloqueo= 10
                    t = threading.Thread(target=bloqueado, args=(ejecucion,posBloqueo)) #Subproceso bloqueados
                    t.daemon= True
                    t.start() 
                    pausa.set()
                    imprimir_en_posicion(16, 80, '                 ')  #Limpia antes de mostrar
                    #imprimir_en_posicion(14, 80, f' < BLOQUEADO >')  #Muestra el contador
                    #elementos.append(ejecucion)
                    interrupted = True
                    key_i = False
                    break
                if key_e == True:
                    #if keyboard.is_pressed('e'):  # Verifica si la tecla "e" ha sido presionada
                    #imprimir_en_posicion(14, 80, f' < ERROR >')  #Muestra el contador
                    ejecucion.result = 'Error'
                    key_e = False
                    break
                if key_p == True:
                    #if keyboard.is_pressed('p'):  # Verifica si la tecla "p" ha sido presionada
                    imprimir_en_posicion(16, 80, '                 ')  #Limpia antes de mostrar
                    imprimir_en_posicion(14, 80, f' < PAUSA >')  #Muestra el contador
                    pausa.clear() #Pausa los subprocesos
                    keyboard.wait("c") #Espera una "c"
                    pausa.set()   #Despausa los subprocesos
                    imprimir_en_posicion(14, 80, "  "*15)  #Limpia antes de mostrar 
                    imprimir_en_posicion(16, 80, f' < CONTINUANDO >')  #Muestra el contador
                    imprimir_en_posicion(14, 80, '                 ')  #Limpia antes de mostrar
                    key_p = False
                
            if not interrupted:      #Si no se interrumpio 
                ejecucion.completion_time = contador  #Tiempo de finalizacion
                ejecucion.return_time = (ejecucion.completion_time-ejecucion.time_arrival) #Tiempo de retorno
                ejecucion.wait_time = (ejecucion.return_time-ejecucion.time_run) #Tiempo de espera
                lis.append(ejecucion)
                imprimir_en_posicion(16, 1, '------------------------- < Terminados > --------------------------')
                imprimir_en_posicion(17, 1, '>ID\t\t>Operacion\t\t\t>Resultado\tTL\tTF\tTR\tTRES\tTE\tTS')
                count += 1
                if len(elementos) != 0:
                    next = elementos.pop(0) #Se añade el proximo proceso
                    next.time_arrival = contador     #Tiempo de llegada 
                    grupito.append(next)
                if new != 0:
                    new -= 1
                fila_term = 18
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
                    imprimir_en_posicion(fila_term, 1, f'{idString}{operationString}{resultString}{time_arrival}{completion_time}{return_time}{response_time}{wait_time}{time_run}')
                    fila_term += 1
            else:                    #Si hay interrupcion 
                continue
            #limpiar(16,100) #Limpia los terminados
        
        for row in range(9,15):
            imprimir_en_posicion(row, 0, " "*15)  #Limpia las filas en ejecucion al terminar el programa
        limpiar(2,8)    #Limpia las filas en actuales
    imprimir_en_posicion(18+len(lis), 1, '') #"Posiciona el cursor" para que se imprima al final del programa
    end = True
    print('Press Enter to finish')

def key():  #Key thread
    global key_i,key_e,key_p,key_c,end
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
        if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
            print("<Finished process>")
    
def main():
    subkey = threading.Thread(target=key) #Key thread
    subkey.daemon=True
    subkey.start() #Key thread start
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

    #input('Press enter')
    os.system('cls')
    console(listProcess)
    
if __name__ == "__main__":
    main()
