import math
import re

dictProcess = {}

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
    while not re.match(r'^[+\-*/]+$', op): #We use a expresion regular to validate the string for operators
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
                op2 = input("Introduzca NUEVAMENTE la segunda cifra: ")
                op2 = int(opValidator(op2,2))
            result = op1/op2
        return result,f'{op1}/{op2}={result}'
    
def inputProcess():
        nombre = input("Introduzca un nombre: ")
        while not re.match("^[a-zA-Z]+\s?[a-zA-Z]*$", nombre): #We use a expresion regular to validate the string
            nombre = input("Introduzca NUEVAMENTE un nombre: ")

        id = validationID()
        result,opString = operation() 
        time = input("Introduzca el tiempo aproximado: ")
        while not re.match("^[1-9]+\d*$", time):  #We use a expresion regular to validate the string for time
            time = input("Introduzca NUEVAMENTE el tiempo aproximado: ")

        dictProcess[id] = (nombre,opString,result,int(time))  #we can elimate varible 'opString', only show the operation as string

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
process = input("Introduzca la cantidad de procesos a realizar: ")
while not re.match("^[1-9]+\d*$", process):
    process = input("Introduzca NUEVAMENTE la cantidad de procesos a realizar: ")
    
process = int(process)
batch = math.ceil(process/5) #we need to round out
print(batch)

while process >= 1:
    print(f'Proceso {process}')
    inputProcess()
    process = process-1


print(dictProcess)
