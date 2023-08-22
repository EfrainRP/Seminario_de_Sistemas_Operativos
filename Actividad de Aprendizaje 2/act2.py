listProcess = []

def validation(id): # TO DO
    if id in listProcess:
        print( )

def operation(op, op1,op2):
    if op == "+":
        return op1+op2
    elif op == "-":
        return op1-op2
    elif op == "*":
        return op1*op2
    else: # / (division)   TO DO
        return op1/op2

process = input("Introduzca la cantidad de procesos a realizar: ")
batch = process/5 #we need to round out


while batch > 0:
    id = input("Introduzca la ID: ")
    op1 = input("OPERACION\nIntroduzca primera cifra: ")
    op2 = input("Introduzca la segunda cifra: ")
    op = input("Introduzca la operacion a realizar: ")
    time = input("Introduzca el tiempo aproximado: ")
