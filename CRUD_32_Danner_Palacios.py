from tkinter import *
from tkinter import ttk

from mysql.connector import cursor
import demo_database

window = Tk()
window.geometry("1100x1000")
frame_app = Frame(window, width=1200, height=600, )
window.title('Mostrar Registros')
my_table = ttk.Treeview(window)
frame_app.pack()




# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
cuenta = IntVar()
nombre = StringVar()
monto = IntVar()


def crear_registro():
# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
# Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
    cuenta = entry_nombre.get()
    nombre = entry_edad.get()
    monto = entry_apellido.get()
    
    
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
    db_demo = demo_database.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
    db_demo.insert_db(cuenta, nombre, monto)




import mysql.connector
connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")

cursor = connection.cursor()
cursor.execute("SELECT CUENTA ,NOMBRE, MONTO  FROM TBL_USUARIOS")


     
    
    
my_table = ttk.Treeview(window)
    

registro=0
for fila in cursor:
    registro=registro+1
    print(str(registro) + "-"+str(fila))
      
    cuenta = fila[0]
    nombre = fila[1]
    monto = fila[2]
    
    my_table.insert(parent="", index="end", iid=registro, text=str(registro),
        values=(cuenta, nombre, monto))
connection.close() 


        # Define Our Columns 
my_table['columns'] = ('CUENTA', 'NOMBRE', 'MONTO')

        # Formate Our Columns
my_table.column('#0', width=120, minwidth=50)
my_table.column('CUENTA', anchor=W, width=120)
my_table.column('NOMBRE', anchor=W, width=120)
my_table.column('MONTO', anchor=W, width=120)


        # Create Headings
my_table.heading('CUENTA', text='CUENTA', anchor=W)
my_table.heading('NOMBRE', text='NOMBRE COMPLETO', anchor=W)
my_table.heading('MONTO', text='MONTO', anchor=W)


        # Pack to the screen
my_table.place(x=400, y=350)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=900, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=900, height=120)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=1150, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="",
              font=("Century Gothic", "14"),
              bg=("orange"),
              width=83)
              
title.place(x=0, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="TRANSFERCLOUD", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=350, y=10)
title2 = Label(frame_title, 
              text="*Todos los campos son obligartorios*", 
              font=("Century Gothic", "14"),
              justify=LEFT)
title2.place(x=300, y=50)


# Widgets dentro del contender OPTIONS
frame_form = Frame(frame_options, width=350, height=450, bg="orange")
frame_form.place(x=5, y=5)
label_nombre = Label(frame_form, 
              text="N° DE CUENTA:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="orange")
label_nombre.place(x=30, y=30)
entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_nombre.place(x=30, y=70)

label_edad = Label(frame_form, 
              text="NOMBRE COMPLETO:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="orange")
label_edad.place(x=30, y=100)
entry_edad = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_edad.place(x=30, y=140)

label_apellido = Label(frame_form, 
              text="MONTO:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="orange")
label_apellido.place(x=30, y=170)
entry_apellido = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_apellido.place(x=30, y=210)







button_agregar = Button(frame_form, text="REGISTRAR", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_registro)
button_agregar.place(x=110, y=350)

window.mainloop()
