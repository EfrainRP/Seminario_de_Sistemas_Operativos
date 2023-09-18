from mainwindow import *
from proceso import *
import sys, os, re

def inputData():
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

    input('Press enter')
    os.system('cls')


if __name__ == "__main__":
    inputData()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())