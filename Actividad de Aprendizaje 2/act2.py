import math
import re

dictProcess = {}

def validationID(): 
    id = int(input("Introduzca la ID: "))
    flag = True
    
    while flag:    
        if (id not in dictProcess) and (id > 0): #Verificate if the ID is repeated
            flag = False
        else:
            id = int(input("\tID INVALIDA\nIntroduzca nueva ID: "))
    return id

#def TO DO validate the op1 and op2

def operation():
    op1 = int(input("\tOPERACION\nIntroduzca la primera cifra: "))
    op2 = int(input("Introduzca la segunda cifra: "))
    op = input("Introduzca la operacion a realizar: ")    

    while op != '+' and op != '-' and op != '*' and op != '/': #Operators validations
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
    else: # / (division)
        try: #Exception of 0 as divisor
            result = op1/op2
        except ZeroDivisionError:
            print("No se puede dividir entre cero :(\n\tIngrese nuevos valores")
            while op2 == 0:
                op1 = int(input("\nIntroduzca NUEVAMENTE la primera cifra: "))
                op2 = int(input("Introduzca NUEVAMENTE la segunda cifra: ")) 
            result = op1/op2
        return result,f'{op1}/{op2}={result}'
    
def inputProcess():
        nombre = str(input("Introduzca un nombre: "))
        while not re.match("^[a-zA-Z]+\s?[a-zA-Z]*$", nombre): #We use a expresion regular to validate the string
            nombre = str(input("Introduzca NUEVAMENTE un nombre: ")) 

        id = validationID()
        result,opString = operation() 
        time = int(input("Introduzca el tiempo aproximado: "))
        while time <= 0: 
            time = int(input("Introduzca NUEVAMENTE el tiempo aproximado: "))

        dictProcess[id] = (nombre,opString,result,time)  #we can elimate varible 'opString', only show the operation as string
    #except ValueError:
     #   print('\tProceso no registrado :(\n\tValor no aceptado')
        

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
process = input("Introduzca la cantidad de procesos a realizar: ")
while not re.match("^[\d]+$", process) or process == "0":
    process = input("Introduzca NUEVAMENTE la cantidad de procesos a realizar: ")
    
process = int(process)
batch = math.ceil(process/5) #we need to round out
print(batch)

while process >= 1:
    print(f'Proceso {process}')
    inputProcess()
    process = process-1


print(dictProcess)
