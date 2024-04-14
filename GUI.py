# import tkinter
from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime
import logistic.excel_wheel as excel_wheel
import logistic.main_wheel as main_wheel
import os

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("blue")

# global width, height, is_file_uploaded, is_advacend_options_active
is_file_uploaded = False
width = 500
height = 550
is_advacend_options_active = False
actual_date = datetime.now()
date_format_default = formato_fecha = actual_date.strftime("%d/%m/%Y %H:%M")

app = ctk.CTk() # Create the main application window

times = 0

def start_application():
    global times
    data = obtain_data()
    if(data["status"]):
        times += 1
        if times > 1:
            clear_console()
            system_message()
            pass
        progress_bar.start()
        main_wheel.save_data(data)
    # progress_bar.step()

def center_window(window):
    global width, height, screen_height, screen_width, x, y
    # Calcular las coordenadas para centrar la ventana
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    print("[SYSTEM] Initializing window...")
    print("[SYSTEM] Date:", date_format_default)
    print(f"[SYSTEM] Screen width: {screen_width}, Screen height: {screen_height}")
    print(f"[SYSTEM] Window width: {width}, Window height: {height}")
    print(f"[SYSTEM] Window position: x={x}, y={y}\n")
    window.geometry(f"{width}x{height}+{x}+{y}")

def change_window_dimension():
    global width, height, is_advacend_options_active, is_advanced_options_title
    print("Window dimensions changed!")
    if is_advacend_options_active:
        is_advacend_options_active = False
        show_advanced_option_button.configure(text="Mostrar")
        height = 550
        app.geometry(f"{width}x{height}")
        config_550_height()
    else:
        is_advacend_options_active = True
        show_advanced_option_button.configure(text="Ocultar")
        height = 700
        app.geometry(f"{width}x{height}")
        config_700_height()
    center_window(window=app) # Centrar la ventana después de cambiar su tamaño
    
def config_550_height():
    title_label.place(relx=0.5, rely=0.08, anchor='center')
    subtitle_label.place(relx=0.5, rely=0.17, anchor='center')
    configuration_label.place(relx=0.5, rely=0.26, anchor='center')
    first_step.place(relx=0.5, rely=0.33, anchor='center')
    open_excel_button.place(relx=0.5, rely=0.39, anchor='center')
    data_label.place(relx=0.5, rely=0.45, anchor='center')
    second_step.place(relx=0.5, rely=0.5, anchor='center')
    filter_combo_box.place(relx=0.52, rely=0.55, anchor='center')
    option_label.place(relx=0.5, rely=0.6, anchor='center')
    advanced_option_label.place(relx=0.1, rely=0.66, )
    show_advanced_option_button.place(relx=0.65, rely=0.66, )
    start_button.place(relx=0.5, rely=0.8, anchor='center')
    progress_bar.place(relx=0.5, rely=0.885, anchor='center')
    progress_bar_message.place(relx=-0.19, rely=0.91,)
    nexa_message.place(relx=0.32, rely=0.91,)
    
    fitness_label.place(relx=0.22, rely=5.0,)
    fitness_entry.place(relx=0.5, rely=5.0)
    iterator_label.place(relx=0.22, rely=5.0,)
    iterator_entry.place(relx=0.5, rely=5.0)
    p_mut_cruza_label.place(relx=0.22, rely=5.0,)
    p_mut_cruza_value.place(relx=0.5, rely=5.0)
    p_mut_ind_label.place(relx=0.22, rely=5.0,)
    p_mut_ind_value.place(relx=0.5, rely=5.0)
    p_mut_gen_label.place(relx=0.22, rely=5.0,)
    p_mut_gen_value.place(relx=0.5, rely=5.0)
    
def config_700_height():
    title_label.place(relx=0.5, rely=0.06, anchor='center')
    subtitle_label.place(relx=0.5, rely=0.13, anchor='center')
    configuration_label.place(relx=0.5, rely=0.2, anchor='center')
    first_step.place(relx=0.5, rely=0.25, anchor='center')
    open_excel_button.place(relx=0.5, rely=0.3, anchor='center')
    data_label.place(relx=0.5, rely=0.345, anchor='center')
    second_step.place(relx=0.5, rely=0.38, anchor='center')
    filter_combo_box.place(relx=0.52, rely=0.425, anchor='center')
    option_label.place(relx=0.5, rely=0.465, anchor='center')
    advanced_option_label.place(relx=0.1, rely=0.495, )
    show_advanced_option_button.place(relx=0.65, rely=0.495, )
    fitness_label.place(relx=0.22, rely=0.585,)
    fitness_entry.place(relx=0.5, rely=0.58)
    iterator_label.place(relx=0.22, rely=0.635,)
    iterator_entry.place(relx=0.5, rely=0.63)
    p_mut_cruza_label.place(relx=0.22, rely=0.685,)
    p_mut_cruza_value.place(relx=0.5, rely=0.68)
    p_mut_ind_label.place(relx=0.22, rely=0.735,)
    p_mut_ind_value.place(relx=0.5, rely=0.73)
    p_mut_gen_label.place(relx=0.22, rely=0.785,)
    p_mut_gen_value.place(relx=0.5, rely=0.78)
    start_button.place(relx=0.5, rely=0.865, anchor='center')
    progress_bar.place(relx=0.5, rely=0.92, anchor='center')
    progress_bar_message.place(relx=-0.19, rely=0.94,)
    nexa_message.place(relx=0.32, rely=0.94,)
    
def open_excel():
    result = excel_wheel.open_excel_file()
    if "error" not in result:  
        messagebox.showinfo("ExcelWhile", "Excel cargado exitosamente.")
        date_label(True)
    else:    
        messagebox.showerror("ExcelWhile", f"Hubo un error al cargar el excel: {result['error']}")
        data_label.configure(text=f"{result['error']}")
    
def date_label(file_ready):
    global is_file_uploaded
    if file_ready:
        data_label.configure(text=f"Última revisión: {date_format_default}")
        is_file_uploaded = True
    else:
        data_label.configure(text=f"No se ha subido nada aún")
    
def update_filter_combo_box(event):
    selected_option = filter_combo_box.get()
    option_label.configure(text=f"Opción seleccionada: {selected_option}")
    print(selected_option)
    
def obtain_data():
    global is_file_uploaded
    fitness = fitness_entry.get() if len(fitness_entry.get()) else "100"
    selected_option = filter_combo_box.get()
    iterator = iterator_entry.get() if len(iterator_entry.get()) else "-1"
    p_mut_cruza = p_mut_cruza_value.get() if len(p_mut_cruza_value.get()) else "100"
    p_mut_ind = p_mut_ind_value.get() if len(p_mut_ind_value.get()) else "100"
    p_mut_gen = p_mut_gen_value.get() if len(p_mut_gen_value.get()) else "100"

    if not fitness.isdigit():
        messagebox.showerror("Error", "El valor de Fitness debe ser un número entero positivo.")
        return {"status": False}

    if not iterator == "-1":
        if iterator.isdigit():
            pass

        else:
            messagebox.showerror("Error", "El valor de Iteraciones debe ser un número entero positivo.")
            return {"status": False}


    if not p_mut_cruza.isdigit():
        messagebox.showerror("Error", "El valor de P. mut. cruza debe ser un número entero positivo.")
        return {"status": False}


    if not p_mut_ind.isdigit():
        messagebox.showerror("Error", "El valor de P. mut. ind. debe ser un número entero positivo.")
        return {"status": False}


    if not p_mut_gen.isdigit():
        messagebox.showerror("Error", "El valor de P. mut. gen. debe ser un número entero positivo.")
        return {"status": False}

    fitness = int(fitness)
    iterator = int(iterator)
    p_mut_cruza = int(p_mut_cruza)
    p_mut_ind = int(p_mut_ind)
    p_mut_gen = int(p_mut_gen)
    
    if len(selected_option) and is_file_uploaded:
        return {"status": True, "selected_option": selected_option, "iterator": iterator, "p_mut_cruza": p_mut_cruza, "p_mut_ind": p_mut_ind, "p_mut_gen": p_mut_gen, "fitness": fitness}
    else:
        message = "No se pudo iniciar el programa. \nPor favor, Cargue los siguientes archivos:"
        if not is_file_uploaded:
            message += "\n- Archivo Excel"
        if not len(selected_option):
            message += "\n- La opción de ordenamiento"
        messagebox.showerror("ExcelWhile", message)

        return {"status": False}

def clear_console():
    os.system('cls')
    
def system_message():
    print("[SYSTEM] Initializing window...")
    print("[SYSTEM] Date:", date_format_default)
    print(f"[SYSTEM] Screen width: {screen_width}, Screen height: {screen_height}")
    print(f"[SYSTEM] Window width: {width}, Window height: {height}")
    print(f"[SYSTEM] Window position: x={x}, y={y}\n")

app.geometry(f"{width}x{height}")
clear_console()
center_window(window=app)

title_label = ctk.CTkLabel(app, text="NEXA: COURSE ORDERING PROGRAM", fg_color="#d9d9d9", width=400, height=40, text_color="#000000", font=("Arial", 20, "bold"))
subtitle_label = ctk.CTkLabel(app, text="Programa de ordenamiento de cursos \npara el desarrollo web", width=400, height=30, text_color="#fff", font=("Arial", 14, "bold"))
configuration_label = ctk.CTkLabel(app, text="CONFIGURACIÓN", fg_color="#d9d9d9", width=400, height=40, text_color="#000000", font=("Arial", 20, "bold"))
first_step = ctk.CTkLabel(app, text="1) Carga de cursos", width=400, height=20, text_color="#fff", font=("Arial", 14, "bold"))
open_excel_button = ctk.CTkButton(app, text="Abrir Excel", command=open_excel, height=40, width=120,fg_color="#868686", font=("Arial", 14, "bold"), text_color="#000000", corner_radius=0)
data_label = ctk.CTkLabel(app, width=400, text="No se ha subido nada aún", height=20, text_color="#fff", font=("Arial", 12, "bold"))
second_step = ctk.CTkLabel(app, text="2) Obtener lista de cursos por", width=400, height=20, text_color="#fff", font=("Arial", 14, "bold"))
filter_combo_box = ctk.CTkComboBox(app, width=400,values=["a) Facil a dificil", "b) Dificil a facil", "c) Menor o mayor tiempo", "d) Mayor a menor tiempo", "e) Pocos a muchos requisitos", "f) Muchos a pocos requisitos"], command=update_filter_combo_box)
filter_combo_box.configure(width=165, height=30)
option_label = ctk.CTkLabel(app, text=f"Opción por default: {filter_combo_box.get()}", height=20, text_color="#fff", font=("Arial", 12, "bold"))
advanced_option_label = ctk.CTkLabel(app, text="OPCIONES AVANZADAS", fg_color="#d9d9d9", width=250, height=40, text_color="#000000", font=("Arial", 20, "bold"))
show_advanced_option_button = ctk.CTkButton(app, text="Mostrar", command=change_window_dimension, height=40, width=125,fg_color="#868686", font=("Arial", 14, "bold"), text_color="#000000", corner_radius=0)
fitness_label = ctk.CTkLabel(app, text="Rango mín de Fitness.", height=20, text_color="#fff", font=("Arial", 13, "bold"))
fitness_entry = ctk.CTkEntry(app, placeholder_text="Default 100%", placeholder_text_color="#000000", bg_color="#d9d9d9", corner_radius=0, border_color="#d9d9d9", fg_color="#d9d9d9", text_color='#000000')
iterator_label = ctk.CTkLabel(app, text="Iteraciones.", height=20, text_color="#fff", font=("Arial", 13, "bold"))
iterator_entry = ctk.CTkEntry(app, placeholder_text="Hallar el mejor fitness", placeholder_text_color="#000000", bg_color="#d9d9d9", corner_radius=0, border_color="#d9d9d9", fg_color="#d9d9d9", text_color='#000000')
p_mut_cruza_label = ctk.CTkLabel(app, text="P. mut. cruza. (%)", height=20, text_color="#fff", font=("Arial", 13, "bold"))
p_mut_cruza_value = ctk.CTkEntry(app, placeholder_text="Default 100%", placeholder_text_color="#000000", bg_color="#d9d9d9", corner_radius=0, border_color="#d9d9d9", fg_color="#d9d9d9", text_color='#000000')
p_mut_ind_label = ctk.CTkLabel(app, text="P. mut. ind. (%)", height=20, text_color="#fff", font=("Arial", 13, "bold"))
p_mut_ind_value = ctk.CTkEntry(app, placeholder_text="Default 100%", placeholder_text_color="#000000", bg_color="#d9d9d9", corner_radius=0, border_color="#d9d9d9", fg_color="#d9d9d9", text_color='#000000')
p_mut_gen_label = ctk.CTkLabel(app, text="P. mut. gen. (%)", height=20, text_color="#fff", font=("Arial", 13, "bold"))
p_mut_gen_value = ctk.CTkEntry(app, placeholder_text="Default 100%", placeholder_text_color="#000000", bg_color="#d9d9d9", corner_radius=0, border_color="#d9d9d9", fg_color="#d9d9d9", text_color='#000000')
start_button = ctk.CTkButton(app, text="SOLICITAR LISTA DE CURSOS", command=start_application, height=40, width=400,fg_color="#868686", font=("Arial", 20, "bold"), text_color="#000000", corner_radius=0)
progress_bar = ctk.CTkProgressBar(app, width=400, height=20, corner_radius=0)
progress_bar.configure(mode="determinate")
progress_bar.set(0)
progress_bar_message = ctk.CTkLabel(app, width=400, text="[✔] Listo para inicializar", height=10, text_color="#fff", font=("Arial", 10, "bold"))
nexa_message = ctk.CTkLabel(app, width=400, text="NEXA Industries from Mauricio Castillo", height=10, text_color="#fff", font=("Arial", 10, "bold"))
config_550_height()

app.mainloop()
