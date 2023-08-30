import math
import re
import tkinter as tk
from tkinter import ttk
import time

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
#----------------------------------------------------------------------------------------------------------------------
#INTERFACE CODE

class TablaInterfaz:
    def __init__(self, root):
        # ... Código de inicialización ...
        self.root = root
        self.root.geometry("1300x410")
        self.root.title("Tabla")
        #Label, actualizacion de Lotes pendientes
        self.lotes_pendientes = tk.StringVar()
        self.lotes_pendientes.set(f"-No lotes pendientes: 0")
        self.label = tk.Label(root, textvariable=self.lotes_pendientes, font=("Arial", 18))
        self.label.pack()

        #Jump between labels
        self.jump = tk.Label(root, text="")
        self.jump.pack()
        #Label batches worked
        self.lotes_trabajados = tk.Label(root, text="-Lotes trabajados")
        self.lotes_trabajados.place(x=210, y=55)
        #Label running process
        self.proceso_en_ejecucion = tk.Label(root, text=">Proceso en ejecución", fg='green')
        self.proceso_en_ejecucion.place(x=490, y=55)
        #Label finished
        self.terminados = tk.Label(root, text="-Terminados",fg='red')
        self.terminados.place(x=920, y=55)
        #Table in interface
        self.tabla = ttk.Treeview(root, columns=("ID'", "TME", f"Programador: {programmer}", "ID", "Operación", "Resultado"), show="headings")
        #Label counter
        self.contador = tk.StringVar()
        self.contador.set(f"Contador: 0")
        self.label = tk.Label(root, textvariable=self.contador, font=("Arial", 18), fg="blue")
        self.label.place(x=560,y=350)
        # Create a function that updates the data and the table
        self.actualizar_tabla()

    def update(self,f1,f2,f3,f4,f5):   #Actualiza los tiempos de TT y RES 
        datos = [f1,f2,f3,f4,f5]
        for item in self.tabla.get_children():
            self.tabla.delete(item)
                # Insert the new data into the table
        for fila in datos:
            self.tabla.insert("", "end", values=fila)

    def displayUI(self, elementos, count, actual):
        global TT,contador_global,lot_pend
        #print('Grupito: ',elementos)
        print(f'Mi elemento: {elementos[actual][1][0]}')
        input('')
        #Actualiza el N° Lotes pendientes
        self.lotes_pendientes.set(f"-No. lotes pendientes: {lot_pend}")
        self.tabla = ttk.Treeview(root, columns=("ID'", "TME", f"Programador: {elementos[actual][1][0]}", "ID", "Operación", "Resultado"), show="headings")
        self.tabla.heading("ID'", text="ID'")
        self.tabla.heading("TME", text="TME")
        self.tabla.heading(f"Programador: {elementos[actual][1][0]}", text=f"Programador: {elementos[actual][1][0]}")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Operación", text="Operación")
        self.tabla.heading("Resultado", text="Resultado")
        self.tabla.place(x=50, y=100, width=1200, height=230)

        #Scrollbar in the interface
        scroll_y = ttk.Scrollbar(root, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll_y.set)
        scroll_y.place(x=1250, y=87, height=250)

        # Clears the current items from the table



        datos = [
                [f'{elementos[count][0]}', f'{elementos[count][1][3]}', f"-ID usuario: \t{elementos[actual][0]}", 0, "2+2", 0],
                [f'{elementos[count+1][0]}', f'{elementos[count+1][1][3]}', f"-Operación: \t{elementos[actual][1][1]}", 0, "3+2", 0],
                [f'{elementos[count+2][0]}', f'{elementos[count+2][1][3]}', f"-Tiempo MXE: \t{elementos[actual][1][3]}", 0, "4+2", 0],
                [f'{elementos[count+3][0]}', f'{elementos[count+3][1][3]}', f"-Tiempo TRA: \t{TT}", 0, "5+2", 0],
                [f'{elementos[count+4][0]}', f'{elementos[count+4][1][3]}', f"-Tiempo RES: \t{elementos[actual][1][3]-1}", 0, "6+2", 0]]
        input('')

        for i in range(elementos[actual][1][3]):  #Actualiza el tiempo TRA Y RES
            self.update([f'{elementos[count][0]}', f'{elementos[count][1][3]}', f"-ID usuario: \t{elementos[actual][0]}", 0, "2+2", 0],
            [f'{elementos[count+1][0]}', f'{elementos[count+1][1][3]}', f"-Operación: \t{elementos[actual][1][1]}", 0, "3+2", 0],
            [f'{elementos[count+2][0]}', f'{elementos[count+2][1][3]}', f"-Tiempo MXE: \t{elementos[actual][1][3]}", 0, "4+2", 0],
            [f'{elementos[count+3][0]}', f'{elementos[count+3][1][3]}', f"-Tiempo TRA: \t{TT}", 0, "5+2", 0],
            [f'{elementos[count+4][0]}', f'{elementos[count+4][1][3]}', f"-Tiempo RES: \t{elementos[actual][1][3]-TT}", 0, "6+2", 0])
            TT += 1
            input('Press to update')

        #Actualiza el contador global por cada proceso en ejecucion
        contador_global = contador_global+elementos[actual][1][3]
        self.contador.set(f"Contador: {contador_global}")

        datos.append(["--", "--", "-------------", 10, "10+10", 20],)

        #datos.pop(3)
        #datos.insert(3,[0, 0, f"-Tiempo TRA: \t{TT}", 1, "5+2", 0],)

        #update the remaining row
        #datos.pop(4)
        #datos.insert(4,[0, 0, f"-Tiempo RES: \t{elementos[actual][1][3]-TT}", 1, "5+2", 0],)

        #for item in self.tabla.get_children():
        #    self.tabla.delete(item)
        # Insert the new data into the table
        #for fila in datos:
        #    self.tabla.insert("", "end", values=fila)
    #Function where the data is updated
    def actualizar_tabla(self):
        #Global variables to update data
        global lot_pend,TT
        #Variable to update ejecution process
        actual = 0
        TT = 1
        lis = [] #Ejecution process
        #Dictionary items grouped by 5
        elementos = list(dic.items())
        total_elementos = len(elementos)
        count = 0
        for x in range(0, total_elementos, 5):
            lot_pend -= 1
            grupo = elementos[x:x+5]
            print("Grupo:", grupo)                #Group contains a maximum of 5 processes from the dictionary
            lis.append(grupo)                     #Add a maximum of 5 processes to the list
            if len(lis[0]) < 5:                 #Valida que siempre haya grupos de 5
                if 5-len(lis[0]) == 1:          #y al haber menos, los completa como espacios en "0"
                    lis[0].append((0,(0,0,0,0)))
                if 5-len(lis[0]) == 2:
                    lis[0].append((0,(0,0,0,0)))
                    lis[0].append((0,(0,0,0,0)))
                if 5-len(lis[0]) == 3:
                    for it in range(3):
                        lis[0].append((0,(0,0,0,0)))
                if 5-len(lis[0]) == 4:
                    for it in range(4):
                        lis[0].append((0,(0,0,0,0)))
            print(f'MI lista actual es: ',lis)
            for i in range(len(lis[0])):          #Show each of the elements separately
                print(lis[0][i])
                self.displayUI(lis[0],count,actual)
                if actual == 4:   #Contador de procesos en ejecución
                    actual = 0    #Reinicia el contador en ejecucion por cada grupo
                else:
                    actual += 1
                TT = 1           #Reinicia el contador de transcurrido por cada proceso en ejecucion
            lis.clear()                           #The list is cleared and then it adds 5 different processes.

        #Updat table 
        self.root.after(5000, self.actualizar_tabla)
        time.sleep(1)
        #Add a line to the End of batch table
        datos.append(["--", "--", f"-Fin Lote: {1}", "--", "----", "--"],)
        #Add a new row to the table
        datos.append(["--", "--", "-------------", 10, "10+10", 20],)
        #When reaching the end of processes...
        if lot_pend == 0:
            exit()

if __name__ == "__main__":
    '''
    dictProcess = {}
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
    input('Press enter')
    '''
    #Example Dict
    dic = {1:('Yeremy','1+1',2,4), 2:('Gera','2+2',4,22), 3:('Lupi','3+3',4,33),4:('Lupi','4+4',4,44),
    5:('Dadan','5+5',4,55),6:('Armando','6+6',4,66),7:('Uriel','7+7',4,77),}

    batch = math.ceil(7/5)

    lot_pend = batch          #Pending batch counter
    contador_global = 0      #Program timer
    programmer = ''          #Table variable

    root = tk.Tk()
    app = TablaInterfaz(root)
    root.mainloop()

