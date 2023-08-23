import math

dictProcess = {}

def validationID(): 
    id = int(input("Introduzca la ID: "))
    flag = True
    while flag:    
        if id not in dictProcess: #Verificate if the ID is repeated
            flag = False
        else:
            id = input("\tID REPETIDA\nIntroduzca nueva ID: ")
    return id

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
            print("No se puede dividir entre cero :(\n\tIntente de nuevo")
            while op2 == 0:
                op1 = int(input("\nIntroduzca nuevamente la primera cifra: "))
                op2 = int(input("Introduzca la segunda cifra: ")) 
            result = op1/op2
        return result,f'{op1}/{op2}={result}'
    
def inputProcess():
    try:
        id = validationID()
        result,opString = operation() 
        time = int(input("Introduzca el tiempo aproximado: "))
        while time <= 0: 
            time = int(input("Introduzca NUEVAMENTE el tiempo aproximado: "))

        dictProcess[id] = (opString,result,time)  #we can elimate varible 'opString', only show the operation as string
    except ValueError:
        print('\tProceso no registrado :(\n\tValor no aceptado')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    process = int(input("Introduzca la cantidad de procesos a realizar: "))
    batch = math.ceil(process/5) #we need to round out
    print(batch)

    while process > 0:
        inputProcess()
        process = process-1

except ValueError:
    print('\tValor no aceptado\nVuelva intentarlo despues')

print(dictProcess)
