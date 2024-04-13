import os
from datetime import datetime
import openpyxl
import pandas as pd
from tkinter import messagebox
import logistic.auxiliar_wheel as aux

epochs = -1
p_mut_cruza = 100
p_mut_ind = 100
p_mut_gen = 100

def save_data(data):
    global epochs, p_mut_cruza, p_mut_ind, p_mut_gen
    print(f"Guardando los datos: {data}")
    epochs = data['iterator']
    p_mut_cruza = data['p_mut_cruza']
    p_mut_ind = data['p_mut_ind']
    p_mut_gen = data['p_mut_gen']
    # save_default_data_to_excel(data)
    result = upload_data_by_parameter(data['selected_option'][0])
    if result:
        form_pairs(result)
    else:
        print("Error al cargar los datos.")
    
def upload_data_by_parameter(parameter):
    if parameter == 'a' or parameter == 'b':
        excel_file_path = 'temp_files/difficulty.xlsx'
        df = pd.read_excel(excel_file_path)
        # print(parameter, "\n",df['conversion_num'].tolist())
        return df['conversion_num'].tolist()
    elif parameter == 'c' or parameter == 'd':
        excel_file_path = 'temp_files/duration.xlsx'
        df = pd.read_excel(excel_file_path)
        # print(parameter, "\n",df['level'].tolist())
        return df['level'].tolist()
    elif parameter == 'e' or parameter == 'f':
        excel_file_path = 'temp_files/requirements.xlsx'
        df = pd.read_excel(excel_file_path)
        return df['conversion_num'].tolist()
    else:
        messagebox.showerror("Error", f"Opción {parameter} no válida, se encuentra fuera de alcance.")
        return False

def form_pairs(data_list):
    print("\n\n\nFormando pares de datos...")
    first_pair = data_list
    second_pair = data_list[::-1]
    print("Primer par:", first_pair)
    print("Segundo par:", second_pair)
    information_crossover(first_pair, second_pair)
    # Añadir validacion de que si ya está ordenado segun f(x) retorne el arreglo y ya no siga con el proceso
    
def information_crossover(first_pair, second_pair):
    print("\n\nCruce de información")
    print("Parametros dados:", "epochs:", epochs, "p_mut_cruza:", p_mut_cruza, "p_mut_ind:", p_mut_ind, "p_mut_gen:", p_mut_gen,)
    print("length of first pair:", len(first_pair), "length of second pair:", len(second_pair))
    if len(first_pair) >= 3:
        print("Se puede realizar el cruce de información.")
        arr1, arr2 = aux.swap_elements(first_pair, second_pair, p_mut_cruza)
        print("Arrays received:\n", arr1, "\n", arr2)
        mutation(arr1, arr2)
    else:
        print("No se puede realizar el cruce de información, la longitud de los pares es menor a 3. Pasa directo a mutación.")
        
def mutation(first_pair, second_pair):
    print("\n\nMutación")
    print(f"In mutation received arrays:\n{first_pair}\n{second_pair}")
    
    
def pruning():
    print("\n\nPoda")
    # Los mejores son puestos debajo de los 2 primeros creados al inicio en el excel de "reports" actual del programa, y hasta
    # abajo despues de colocar cada resultado por epoca, se pone el mejor de todos los resultados.

def save_default_data_to_excel(data):
    # Get the current date and time
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H%M%S")

    # Create the file name
    file_name = f"report_{date}_{time}.xlsx"

    # Create the folder if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # Create the Excel workbook
    wb = openpyxl.Workbook()

    # Select the active sheet
    ws = wb.active

    # Write the data to the Excel file
    ws.append(["Order by", "Epochs", "P_mut_cruza", "P_mut_ind", "P_mut_gen"])
    ws.append([data["selected_option"], data["iterator"], data["p_mut_cruza"], data["p_mut_ind"], data["p_mut_gen"]])

    # Save the workbook
    wb.save(os.path.join("reports", file_name))
    
    
