import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


empresa_df = pd.DataFrame(columns=['Rut', 'Nombre', 'Giro', 'Representante Legal', 'Fecha de constitucion','antiguedad'])
persona_df = pd.DataFrame(columns=['Rut', 'Nombre', 'Segundo Nombre', 'Apellido Paterno', 'Apellido Materno', 'Fecha de Nacimiento'])

def opcion():
    seleccion = seleccion_var.get()
    if seleccion == 1:
        etiqueta.config(text="Opción empresa.")
        boton_enviar.config(command=abrir_ventana_empresa)
    elif seleccion == 2:
        etiqueta.config(text="Opción persona natural.")
        boton_enviar.config(command=abrir_ventana_persona_natural)

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    fecha_nac = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    edad = fecha_actual.year - fecha_nac.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day))
    return edad

def calcular_antiguedad(fecha_constitucion):
    fecha_actual = datetime.now()
    fecha_const = datetime.strptime(fecha_constitucion, '%d/%m/%Y')
    antiguedad = (fecha_actual - fecha_const).days
    return antiguedad


def abrir_ventana_empresa():
    ventana_empresa = tk.Toplevel()
    ventana_empresa.title("Formulario Empresa")
    
    def on_button_click():
        empresa_df.loc[len(empresa_df)] = {
            'Rut': rut.get(),
            'Nombre': nombre.get(),
            'Giro': giro.get(),
            'Representante Legal': representante.get(),
            'Fecha de constitucion': f"{fecha_nacimiento_day.get()}/{fecha_nacimiento_month.get()}/{fecha_nacimiento_year.get()}"
        }
        
        fecha_constitucion = f"{fecha_nacimiento_day.get()}/{fecha_nacimiento_month.get()}/{fecha_nacimiento_year.get()}"
        antiguedad = calcular_antiguedad(fecha_constitucion)
        
        messagebox.showinfo("Información", f"Información agregada con éxito!\n\nRut: {rut.get()}\nNombre: {nombre.get()}\nGiro: {giro.get()}\nRepresentante Legal: {representante.get()}\nFecha de constitucion: {fecha_nacimiento_day.get()}/{fecha_nacimiento_month.get()}/{fecha_nacimiento_year.get()}\nAntigüedad: {antiguedad} días")
        
        rut.delete(0, tk.END)
        nombre.delete(0, tk.END)
        giro.delete(0, tk.END)
        representante.delete(0, tk.END)
        fecha_nacimiento_day.set(1)
        fecha_nacimiento_month.set(1)
        fecha_nacimiento_year.set(2000)
        
    rut = ttk.Entry(ventana_empresa, width=30)
    nombre = ttk.Entry(ventana_empresa, width=30)
    giro = ttk.Entry(ventana_empresa, width=30)
    representante = ttk.Entry(ventana_empresa, width=30)
    fecha_nacimiento_day = tk.IntVar(value=1)
    fecha_nacimiento_month = tk.IntVar(value=1)
    fecha_nacimiento_year = tk.IntVar(value=1900)
    
    ttk.Label(ventana_empresa, text="Rut:").grid(row=0, column=0, padx=10, pady=5)
    rut.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(ventana_empresa, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
    nombre.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(ventana_empresa, text="Giro").grid(row=2, column=0, padx=10, pady=5)
    giro.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(ventana_empresa, text="Representante Legal :").grid(row=3, column=0, padx=10, pady=5)
    representante.grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(ventana_empresa, text="Fecha de constitucion:").grid(row=5, column=0, padx=10, pady=5)
    ttk.Spinbox(ventana_empresa, from_=1, to=31, textvariable=fecha_nacimiento_day, width=5).grid(row=5, column=1, padx=(10, 0), pady=5, sticky='w')
    ttk.Spinbox(ventana_empresa, from_=1, to=12, textvariable=fecha_nacimiento_month, width=5).grid(row=5, column=1, padx=(70, 0), pady=5, sticky='w')
    ttk.Spinbox(ventana_empresa, from_=1900, to=2100, textvariable=fecha_nacimiento_year, width=7).grid(row=5, column=1, padx=(140, 10), pady=5, sticky='w')

    ttk.Button(ventana_empresa, text="Enviar", command=on_button_click).grid(row=6, column=0, columnspan=2, pady=20)

def abrir_ventana_persona_natural():
    ventana_persona_natural = tk.Toplevel()
    ventana_persona_natural.title("Formulario Persona Natural")
    
    def on_button_click():
        global df
        persona_df.loc[len(persona_df)] = {
            'Rut': rut.get(),
            'Nombre': nombre.get(),
            'Segundo Nombre': segundo_nombre.get(),
            'Apellido Paterno': apellido_paterno.get(),
            'Apellido Materno': apellido_materno.get(),
            'Fecha de Nacimiento': f"{fecha_nacimiento_day.get()}/{fecha_nacimiento_month.get()}/{fecha_nacimiento_year.get()}"
        }
        
        fecha_nacimiento = f"{fecha_nacimiento_day.get()}/{fecha_nacimiento_month.get()}/{fecha_nacimiento_year.get()}"
        edad = calcular_edad(fecha_nacimiento)
    
        messagebox.showinfo("Información", f"Información agregada con éxito!\n\nRut: {rut.get()}\nNombre: {nombre.get()}\nSegundo Nombre: {segundo_nombre.get()}\nApellido Paterno: {apellido_paterno.get()}\nApellido Materno: {apellido_materno.get()}\nFecha de Nacimiento: {fecha_nacimiento_day.get()}/{fecha_nacimiento_month.get()}/{fecha_nacimiento_year.get()}\n{nombre.get()}\nEdad: {edad} años")
        
        rut.delete(0, tk.END)
        nombre.delete(0, tk.END)
        segundo_nombre.delete(0, tk.END)
        apellido_paterno.delete(0, tk.END)
        apellido_materno.delete(0, tk.END)
        fecha_nacimiento_day.set(1)
        fecha_nacimiento_month.set(1)
        fecha_nacimiento_year.set(2000)
        
    rut = ttk.Entry(ventana_persona_natural, width=30)
    nombre = ttk.Entry(ventana_persona_natural, width=30)
    segundo_nombre = ttk.Entry(ventana_persona_natural, width=30)
    apellido_paterno = ttk.Entry(ventana_persona_natural, width=30)
    apellido_materno = ttk.Entry(ventana_persona_natural, width=30)
    fecha_nacimiento_day = tk.IntVar(value=1)
    fecha_nacimiento_month = tk.IntVar(value=1)
    fecha_nacimiento_year = tk.IntVar(value=2000)

    ttk.Label(ventana_persona_natural, text="Rut:").grid(row=0, column=0, padx=10, pady=5)
    rut.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(ventana_persona_natural, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
    nombre.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(ventana_persona_natural, text="Segundo Nombre").grid(row=2, column=0, padx=10, pady=5)
    segundo_nombre.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(ventana_persona_natural, text="Apellido Paterno :").grid(row=3, column=0, padx=10, pady=5)
    apellido_paterno.grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(ventana_persona_natural, text="Apellido Materno :").grid(row=4, column=0, padx=10, pady=5)
    apellido_materno.grid(row=4, column=1, padx=10, pady=5)

    ttk.Label(ventana_persona_natural, text="Fecha de Nacimiento:").grid(row=5, column=0, padx=10, pady=5)
    ttk.Spinbox(ventana_persona_natural, from_=1, to=31, textvariable=fecha_nacimiento_day, width=5).grid(row=5, column=1, padx=(10, 0), pady=5, sticky='w')
    ttk.Spinbox(ventana_persona_natural, from_=1, to=12, textvariable=fecha_nacimiento_month, width=5).grid(row=5, column=1, padx=(70, 0), pady=5, sticky='w')
    ttk.Spinbox(ventana_persona_natural, from_=1900, to=2100, textvariable=fecha_nacimiento_year, width=7).grid(row=5, column=1, padx=(140, 10), pady=5, sticky='w')

    ttk.Button(ventana_persona_natural, text="Enviar", command=on_button_click).grid(row=6, column=0, columnspan=2, pady=20)

ventana = tk.Tk()
ventana.title("Formulario SII")

ventana.geometry("250x200")
frame_principal = ttk.Frame(ventana)
frame_principal.pack(padx=10, pady=10)

seleccion_var = tk.IntVar()

etiqueta = tk.Label(ventana, text="Seleccione una opción.", font=("Arial", 12))
etiqueta.pack(pady=10)

radio_empresa = ttk.Radiobutton(ventana, text="Opción empresa", variable=seleccion_var, value=1, command=opcion)
radio_empresa.pack()

radio_persona_natural = ttk.Radiobutton(ventana, text="Opción persona natural", variable=seleccion_var, value=2, command=opcion)
radio_persona_natural.pack()

boton_enviar = ttk.Button(ventana, text="Enviar", command=lambda: None)
boton_enviar.pack()
def guardar_en_excel():
    with pd.ExcelWriter('Formulario SII.xlsx', engine='openpyxl') as writer:
        empresa_df.to_excel(writer, sheet_name='Empresas', index=False)
        persona_df.to_excel(writer, sheet_name='Personas Naturales', index=False)
boton_guardar_excel = ttk.Button(ventana, text="Guardar en Excel", command=guardar_en_excel)
boton_guardar_excel.pack()
ventana.mainloop()


persona_df['Edad'] = persona_df['Fecha de Nacimiento'].apply(calcular_edad)
persona_df['Categoría Edad'] = pd.cut(persona_df['Edad'], bins=[0, 20, 35, 60, 150], labels=['Joven', 'Adulto', 'Senior', 'Tercera Edad'])

edad_counts = persona_df['Categoría Edad'].value_counts().sort_index()

plt.figure(figsize=(8, 6))
edad_counts.plot(kind='bar', color='skyblue')
plt.title('Distribución de Edades')
plt.xlabel('Categoría de Edad')
plt.ylabel('Cantidad de Personas')

plt.show()
