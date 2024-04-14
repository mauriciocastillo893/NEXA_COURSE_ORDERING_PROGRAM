import os
from datetime import datetime
import openpyxl
import pandas as pd
from tkinter import messagebox
import logistic.auxiliar_wheel as aux

selected_option = 'a'
epochs = -1
p_mut_cruza = 100
p_mut_ind = 100
p_mut_gen = 100
current_epoch = 0
fitness = 100

def save_data(data):
    global epochs, p_mut_cruza, p_mut_ind, p_mut_gen, selected_option, fitness
    # save_default_data_to_excel(data)
    fitness = data['fitness']
    selected_option = data['selected_option'][0]
    epochs = data['iterator']
    p_mut_cruza = data['p_mut_cruza']
    p_mut_ind = data['p_mut_ind']
    p_mut_gen = data['p_mut_gen']
    
    print("\n[PARAMETERS]",)
    print("\tEpochs:", epochs, "\n\tFitness:", fitness,"\n\tP_mut_cruza:", p_mut_cruza, "\n\tP_mut_ind:", p_mut_ind, "\n\tP_mut_gen:", p_mut_gen, "\n\tSelected option:", selected_option, "\n\tCurrent epoch:", current_epoch)
    
    result = upload_data_by_parameter(data['selected_option'][0])
    if result:
        form_pairs(result, [])
    else:
        print("[SYSTEM] Data couldn't be uploaded. Please check the parameter 'selected_option' value.")
    
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

def form_pairs(data_list, second_data_list):
    # Asignar los 2 arrays al excel de "reports" actual del programa
    if epochs == -1 or current_epoch < epochs:
        print("\n[FORMING PAIRS] Epoch: ", current_epoch)
        first_pair = data_list
        first_pair = [f"{value}-P{index + 1}" for index, value in enumerate(first_pair)]
        if not len(second_data_list):
            second_pair = first_pair[::-1]
            print("[FORMING PAIRS] Second data list is empty. Creating second pair from first pair (default).")
        else:
            second_pair = []
            print("[FORMING PAIRS] Second data list exists, importing this one.")
        print("[FORMING PAIRS] First pair", first_pair)
        print("[FORMING PAIRS] Second pair", second_pair)
        information_crossover(first_pair, second_pair)
        # Añadir validacion de que si ya está ordenado segun f(x) retorne el arreglo y ya no siga con el proceso
    else:
        print(f"\n[FORMING PAIRS] Process finished. Epochs limit reached.", "Current epoch:", current_epoch, "Epochs:", "Obtain the best fitness value." if epochs == -1 else epochs)
    
def information_crossover(first_pair, second_pair):
    print("\n[CROSSOVER] Epoch: ", current_epoch)
    if len(first_pair) >= 3:
        print("[CROSSOVER] Crossover can be performed. Arrays are greater than 3 elements.")
        arr1, arr2 = aux.swap_elements(first_pair, second_pair, p_mut_cruza, p_mut_ind)
        mutation(arr1, arr2)
    else:
        print("[CROSSOVER] Crossover can't be performed. Arrays are less than 3 elements.")
        
def mutation(first_pair, second_pair):
    global p_mut_gen
    percentage_per_element = 100/len(first_pair)
    jumps = int(p_mut_gen//percentage_per_element)

    print(f"\n[MUTATION] Epoch: {current_epoch}")
    print("[MUTATION] Percentage per element:", percentage_per_element, "%")
    
    operator = aux.define_operator(selected_option)
    
    print("[MUTATION] Jumps required:", jumps)
    print(f"[MUTATION] Array parameters: \n\tFirst: {first_pair}\n\tSecond: {second_pair}")
    
    print("\n[MUTATION] Mutation for FIRST ARRAY initialized")
    arr1 = aux.mutation_for_array_parameter(first_pair, operator, p_mut_gen, percentage_per_element, jumps)
    
    print("\n[MUTATION] Mutation for SECOND ARRAY initialized")
    arr2 = aux.mutation_for_array_parameter(second_pair, operator, p_mut_gen, percentage_per_element, jumps)
        
    pruning(arr1, arr2, operator, percentage_per_element)
    
def pruning(first_pair, second_pair, operator, percentage_per_element):
    operator += "="
    print("\n[PRUNING] Epoch: ", current_epoch)
    print("[PRUNING] Operator to use:", operator)
    print("[PRUNING] Percentage per element:", percentage_per_element, "%")
    print("[PRUNING] First pair:\n\t", first_pair)
    print("[PRUNING] Second pair:\n\t", second_pair, "\n")
    
    print("[PRUNING] Calculating fitness for FIRST ARRAY")
    fitness_arr1 = aux.calculate_fitness(first_pair, operator, percentage_per_element)
    
    print("[PRUNING] Calculating fitness for SECOND ARRAY")
    fitness_arr2 = aux.calculate_fitness(second_pair, operator, percentage_per_element)
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
    
    
