from tkinter import *
import os
import subprocess
from os import system as cmd
import threading
import time
import sys

#Variable de ventana
window = Tk()

f = open("flow_type.txt", "w")
f.write("")
f.close()

#Parametros ventana
window.title("Core IoT")
window.geometry('800x600')

#Funciones de botones
def iniciar():
    subprocess.run('node-red-start')
       
def start_NRED(): 
    print ("Node-RED iniciado")
    NodeRed_stop.pack()
    NodeRed_start.pack_forget()
    RASP_button.pack()
    SIGFOX_button.pack()
    x=threading.Thread(target = iniciar)
    x.start()
    
def RASP():
    AWS_button.pack()
    IBM_button.pack()
    UBI_button.pack()
    SIGFOX_button.pack()
    RASP_button.pack_forget()
    SERIAL_button.pack_forget()

def SIGFOX():
    print("Sigfox")
    AWS_button.pack_forget()
    IBM_button.pack_forget()
    UBI_button.pack_forget()
    SIGFOX_button.pack_forget()
    RASP_button.pack()
    SERIAL_button.pack()

    
def apagar():
    subprocess.run('node-red-stop')
    
def stop_NRED():
    print ("Node-RED apagado")
    NodeRed_stop.pack_forget()
    AWS_button.pack_forget()
    IBM_button.pack_forget()
    UBI_button.pack_forget()
    RASP_button.pack_forget()
    SIGFOX_button.pack_forget()
    SERIAL_button.pack_forget()
    NodeRed_start.pack()
    subprocess.run('node-red-stop')
    y=threading.Thread(target = apagar)
    y.start()

def AWS():
    f = open("flow_type.txt", "w")
    f.write("AWS")
    f.close()
    
def IBM():
    f = open("flow_type.txt", "w")
    f.write("IBM")
    f.close()

def UBI():
    f = open("flow_type.txt", "w")
    f.write("Ubidots")
    f.close()

def SERIAL():
    f = open("flow_type.txt", "w")
    f.write("Sigfox")
    f.close()

    
#Elementos

welcome = Label(window, text="Bienvenido a Core IoT", font=("Arial Bold", 25))

NodeRed_start = Button(window, text="Iniciar Node-RED", command=start_NRED, bg = "white", activebackground = "green")
NodeRed_stop = Button(window, text="Apagar Node-RED", command=stop_NRED, bg = "white", activebackground = "red")
AWS_button = Button(window, text="AWS", command=AWS, bg = "yellow", activebackground = "green")
IBM_button = Button(window, text="IBM", command=IBM, bg = "blue", activebackground = "green")
UBI_button = Button(window, text="Ubidots", command=UBI, bg = "orange", activebackground = "green")
RASP_button = Button(window, text="Raspberry", command=RASP, bg = "red", activebackground = "green")
SIGFOX_button = Button(window, text="Sigfox", command=SIGFOX, bg = "blue", activebackground = "green")
SERIAL_button = Button(window, text="Enviar temperatura", command=SERIAL, bg = "blue", activebackground = "green")


#Inicializa elementos
welcome.pack()
NodeRed_start.pack()
window.mainloop()
