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

    #Function where the data is updated
    def actualizar_tabla(self):
        # Update the data in the table
        global act, lot_pend, contador_global, TT, programmer
        programmer = 'Vicentenario'
        self.tabla = ttk.Treeview(root, columns=("ID'", "TME", f"Programador: {programmer}", "ID", "Operación", "Resultado"), show="headings")
        self.tabla.heading("ID'", text="ID'")
        self.tabla.heading("TME", text="TME")
        self.tabla.heading(f"Programador: {programmer}", text=f"Programador: {programmer}")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Operación", text="Operación")
        self.tabla.heading("Resultado", text="Resultado")
        self.tabla.place(x=50, y=100, width=1200, height=230)

        #Scrollbar in the interface
        scroll_y = ttk.Scrollbar(root, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll_y.set)
        scroll_y.place(x=1250, y=87, height=250)
        #Global variables to update data 
        act += 1
        lot_pend += 1
        contador_global += 3
        TT +=1
        op = '2+2' #Examp
        TME = 5
        RES = TME
        #Dictionary items grouped by 5
        elementos = list(dic.items())
        total_elementos = len(elementos)

        for i in range(0, total_elementos, 5):
            grupo = elementos[i:i+5]
            print("Grupo:", grupo)                #Group contains a maximum of 5 processes from the dictionary
            lis.append(grupo)                     #Add a maximum of 5 processes to the list
            for i in range(len(lis[0])):          #Show each of the elements separately
                 print(lis[0][i])
            lis.clear()                           #The list is cleared and then it adds 5 different processes.

        datos = [
            [f'{act}', 1, f"-ID usuario: \t{2}", 1, "2+2", 4],
            [2, 2, f"-Operación: \t{op}", 1, "3+2", 4],
            [3, 3, f"-Tiempo MXE: \t{TME}", 1, "4+2", 4],
            [4, 4, f"-Tiempo TRA: \t{TT}", 1, "5+2", 4],
            [5, 5, f"-Tiempo RES: \t{RES}", 1, "6+2", 4],
        ]
        # Schedule the next update after 5 seconds in the table
        self.root.after(5000, self.actualizar_tabla)
        time.sleep(1)
        #Update N. batch pending
        self.lotes_pendientes.set(f"-No. lotes pendientes: {lot_pend}")
        #Update global counter
        self.contador.set(f"Contador: {contador_global}")
        #Add a line to the End of batch table
        datos.append(["--", "--", f"-Fin Lote: {1}", "--", "----", "--"],)
        #Add a new row to the table
        datos.append(["--", "--", "-------------", 10, "10+10", 20],)
        #Updates the ELAPSED row
        datos.pop(3)
        datos.insert(3,[4, 4, f"-Tiempo TRA: \t{TT}", 1, "5+2", 4],)
        #update the remaining row
        datos.pop(4)
        datos.insert(4,[4, 4, f"-Tiempo RES: \t{TME-TT}", 1, "5+2", 4],)

        # Clears the current items from the table
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insert the new data into the table
        for fila in datos:
            self.tabla.insert("", "end", values=fila)

        #When reaching the end of processes...
        if act == total+1:
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
    dic = {1:('Yeremy','1+1',2,1), 2:('Gera','2+2',4,1),3:('Lois','3+3',27,1),4:('Jared','4+4',7,1),5:('Carmen','5+5',41,1),
    6:('Yeremy','1+1',2,1),7:('Yeremy','1+1',2,1),}

    lis = []             #List of running processes
    total = process      #Total processes
    act = 0              #Current process counter
    lot_pend =3          #Pending batch counter
    contador_global = 0  #Program timer
    TT = 0               #Time elapsed
    programmer = ''      #Name var

    root = tk.Tk() 
    app = TablaInterfaz(root)
    root.mainloop()

