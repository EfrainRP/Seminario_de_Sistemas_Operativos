from termcolor import colored
import random, time,os,keyboard,threading
exit = False

def key():  #Key thread
    global exit
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "esc":
            exit = True
            break
            
def imprimir_en_posicion(fila, columna, mensaje):  #Imprime por la posicion mencionada
        # Usar caracteres de escape ANSI para posicionar el cursor
        print(f"\033[{fila};{columna}H{mensaje}", flush=True)

def contenedor():  #Muestra el contenedor
        colum = 2
        for pos in range(20):
            imprimir_en_posicion(10,colum, '__')
            imprimir_en_posicion(11,colum, f'{pos+1}')
            colum += 5

subkey = threading.Thread(target=key) #Key thread
subkey.start() #Key thread start

cont = [] #Contenedor
os.system('cls')

producer_work = colored('< El productor esta trabajando. >       ',"green") #Estado trabajando
consumer_work = colored('< El consumidor esta trabajando. >     ',"green") 

producer_sleep = colored('< El productor esta durmiendo. >      ',"red")  #Estado durmiendo
consumer_sleep = colored('< El consumidor esta durmiendo. >     ',"red")

producer_try = colored('< El productor intentó producir. >      ',"yellow") #Estado esperando
consumer_try = colored('< El consumidor intentó consumir. >     ',"yellow")

colum = 2 #Producidos
pos = 2 #Consumidos
consumidor = random.randint(4,7) #Consumidor
productor = random.randint(4,7) #Productor

contenedor() #Show the container 
while not exit:
    imprimir_en_posicion(6,1, f'>Productor: {productor}')
    imprimir_en_posicion(7,1, f'>Consumidor: {consumidor}')
    band = random.randint(0,1) #Turn Band 0 = Productor, 1 = Consumidor 
    if band == 0: #Turno del productor
        imprimir_en_posicion(6,70, producer_work)
        imprimir_en_posicion(7,70, consumer_sleep)
        producidos = 0
        while (producidos < productor): #Elementos a producir 
            if exit:
                break
            elif  len(cont) == 20: #Si el contenedor (buffer) esta lleno, no se puede producir 
                imprimir_en_posicion(6,70, producer_try)
                productor = (productor-producidos)
                producer = True
                imprimir_en_posicion(6,1, f'>Productor: {productor}')
                time.sleep(2)
                break
            else:  #Caso en el que el contenedor tenga espacios libres para producir 
                producidos += 1
                imprimir_en_posicion(6,20, f' '*20)
                imprimir_en_posicion(6,20, f'[{producidos}]')
                producer = False
                imprimir_en_posicion(9,colum, '$')
                cont.append('$')
                imprimir_en_posicion(3,10, f' '*30)
                imprimir_en_posicion(3,1, f'>Contenedor: {len(cont)}')
                time.sleep(1)
                colum += 5
                if colum == 102:
                    colum = 2     
        if producer == False: #Si el contenedor (buffer) no esta lleno, el productor obtiene otro valor aleatorio
            productor = random.randint(4,7) #Productor
    else: #Turno del consumidor 
        imprimir_en_posicion(6,70, producer_sleep)
        imprimir_en_posicion(7,70, consumer_work)
        consumidos  = 0
        while (consumidos < consumidor): #Elementos a consumir 
            if exit:
                break
            elif len(cont) == 0: #Si el contenedor (buffer) esta vacío, no se puede consumir 
                imprimir_en_posicion(7,70, consumer_try)
                consumidor = (consumidor-consumidos)
                consumer = True
                imprimir_en_posicion(7,1, f'>Consumidor: {consumidor}')
                time.sleep(2)
                break
            else: #Caso en que el contenedor tenga elementos por consumir 
                consumidos += 1
                imprimir_en_posicion(7,20, f' '*20)
                imprimir_en_posicion(7,20, f'[{consumidos}]')
                consumer = False
                imprimir_en_posicion(9,pos, ' ')
                cont.pop()
                imprimir_en_posicion(3,10, f' '*30)
                imprimir_en_posicion(3,1, f'>Contenedor: {len(cont)}')
                time.sleep(1)
                pos += 5
                if pos == 102:
                    pos = 2    
        if consumer == False: #Si el contenedor (buffer) no esta vacío, el consumidor obtiene otro valor aleatorio
             consumidor = random.randint(4,7) #Consumidor
