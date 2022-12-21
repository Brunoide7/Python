#TKinter: Creación básica de ventana simple

import tkinter as tk
from tkinter import ttk #Esto para los widgets.


ventana = tk.Tk()   #Creamos un objeto usando la clase tk.


ventana.geometry('600x400') # Tamaño de la ventana: 600px=ancho, 400px=alto

ventana.title('Nueva ventana')  #Modificamos el nombre de la ventana.

ventana.iconbitmap('icono.ico') #Agregamos icono a nuestra app, pero sin especificar ruta porque está en la misma carpeta que el archivo .py

def evento_click():    #Creamos el método evento_click.
    boton1.config(text='Boton presionado')          #Cambia el texto del botón.
    print ('Ejecución del evento_click')            #Muestra en la terminal.
    boton2= ttk.Button(ventana,text="Nuevo botón")  #Con esta y la sig línea, al presionar el boton1, se crea un nuevo botón.
    boton2.pack()
    
boton1=ttk.Button(ventana,text='Dar click', command=evento_click) #creamos un botón con el padre ventana (donde se va a mostrar el botón).

boton1.pack()   #Con esto mostramos el botón en la ventana. Sin esto no se vería el botón.

ventana.mainloop() #Esto nos permite visualizar nuestra ventana con las config (esta línea la ejecutamos al final para que se muestre las configuraciones).



