import tkinter as tk
from tkinter import messagebox

# Lista para guardar tareas (texto, estado)
tareas = []

# Función para actualizar la lista visual
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for i, (texto, completado) in enumerate(tareas):
        if completado:
            lista_tareas.insert(tk.END, f"✔ {texto}")
            lista_tareas.itemconfig(i, fg="gray")
        else:
            lista_tareas.insert(tk.END, f"✗ {texto}")
            lista_tareas.itemconfig(i, fg="black")

# Añadir tarea
def agregar_tarea(event=None):
    texto = entrada.get()
    if texto.strip() == "":
        messagebox.showwarning("Advertencia", "Ingrese una tarea")
        return
    tareas.append((texto, False))
    entrada.delete(0, tk.END)
    actualizar_lista()

# Marcar como completada
def completar_tarea(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        texto, _ = tareas[indice]
        tareas[indice] = (texto, True)
        actualizar_lista()
    except:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")

# Eliminar tarea
def eliminar_tarea(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Botones
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.pack(pady=10)

# Atajos de teclado
ventana.bind('<Return>', agregar_tarea)      # Enter
ventana.bind('<c>', completar_tarea)         # tecla c
ventana.bind('<Delete>', eliminar_tarea)     # tecla delete
ventana.bind('<Escape>', lambda e: ventana.destroy())  # cerrar app

# Ejecutar aplicación
ventana.mainloop()
