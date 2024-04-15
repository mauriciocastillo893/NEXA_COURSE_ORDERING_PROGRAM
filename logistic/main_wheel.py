import os
from datetime import datetime
import openpyxl
import pandas as pd
from tkinter import messagebox
import logistic.auxiliar_wheel as aux
import logistic.excel_wheel as exc
import time

selected_option = 'a'
epochs = -1
p_mut_cruza = 100
p_mut_ind = 100
p_mut_gen = 100
fitness = 100
current_epoch_infinite = 0
name_file_report = ""
progress_bar_ref = ""

best_fitness = 0
best_array = []
best_epoch = 0

def save_data(data, progress_bar):
    global epochs, p_mut_cruza, p_mut_ind, p_mut_gen, selected_option, fitness, current_epoch, current_epoch_infinite, name_file_report, progress_bar_ref
    file_name = exc.save_default_data_to_excel(data)
    name_file_report = file_name
    fitness = data['fitness']
    selected_option = data['selected_option'][0]
    epochs = data['iterator']
    p_mut_cruza = data['p_mut_cruza']
    p_mut_ind = data['p_mut_ind']
    p_mut_gen = data['p_mut_gen']
    progress_bar_ref = progress_bar
    current_epoch_infinite = 0
    
    print("\n[PARAMETERS]",)
    print("\tEpochs:", epochs, "\n\tFitness:", fitness,"\n\tP_mut_cruza:", p_mut_cruza, "\n\tP_mut_ind:", p_mut_ind, "\n\tP_mut_gen:", p_mut_gen, "\n\tSelected option:", selected_option)
    
    result = upload_data_by_parameter(data['selected_option'][0])
    if result:
        form_pairs(result)
        print(f"\n\n\n[SYSTEM] Data uploaded successfully. Process finished.")
        print(f"Best Fitness: {best_fitness} \nBest Epoch: {best_epoch} \nBest Array: {best_array}")
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

def form_pairs(data_list, second_data_list = [], array1_fitness = 0, array2_fitness = 0, current_epoch = 0, current_epoch_infinite=0):
    # print("\nData list:", data_list, "\nSecond data list:", second_data_list, "\nArray1 fitness:", array1_fitness, "\nArray2 fitness:", array2_fitness, "\nFitness:", fitness, "\nCurrent epoch:", current_epoch)
    # Asignar los 2 arrays al excel de "reports" actual del programa
    global fitness, best_fitness
    fitness = calculate_fitness_base(fitness, current_epoch)
    print(f"\n[FORMING PAIRS] Fitness value to reach: {fitness}")
    if epochs == -1 or current_epoch < epochs:
        if array1_fitness >= fitness:
            if epochs == -1:
                print(f"\n[FORMING PAIRS] Best fitness value found. Current Epoch: {'<<Hallar mejor fitness>>' if epochs == -1 else current_epoch} Process finished.\n[FORMING PAIRS] Best array [first_list]:\n\t{data_list}")
                print(f"[FORMING PAIRS] Best fitness obtained: {array1_fitness}")
                return
            
            elif current_epoch > 0 and current_epoch == epochs:
                print(f"\n[FORMING PAIRS] Best fitness value found. Current Epoch: {'<<Hallar mejor fitness>>' if epochs == -1 else current_epoch} Process finished.\n[FORMING PAIRS] Best array [first_list]:\n\t{data_list}")
                print(f"[FORMING PAIRS] Best fitness obtained: {array1_fitness}")
                return
            
            else: 
                pass
            
        else:
            pass
        
        if array2_fitness >= fitness:
            if epochs == -1:
                print(f"\n[FORMING PAIRS] Best fitness value found. Current Epoch: {'<<Hallar mejor fitness>>' if epochs == -1 else current_epoch} Process finished.\n[FORMING PAIRS] Best array [second_list]:\n\t{second_data_list}")
                print(f"[FORMING PAIRS] Best fitness obtained: {array2_fitness}")
                return
            
            elif current_epoch > 0 and current_epoch == epochs:
                print(f"\n[FORMING PAIRS] Best fitness value found. Current Epoch: {'<<Hallar mejor fitness>>' if epochs == -1 else current_epoch} Process finished.\n[FORMING PAIRS] Best array [second_list]:\n\t{data_list}")
                print(f"[FORMING PAIRS] Best fitness obtained: {array2_fitness}")
                return
            
            else: 
                pass
        else:
            pass
        print("\n[FORMING PAIRS] Epoch: ", current_epoch)
        first_pair = data_list
        
        if current_epoch == 0 and current_epoch_infinite == 0:
            first_pair = [f"{value}-P{index + 1}" for index, value in enumerate(first_pair)]
            
        if not len(second_data_list):
            second_pair = first_pair[::-1]
            print("[FORMING PAIRS] Second data list is empty. Creating second pair from first pair (default).")
            aux.save_generation(name_file_report, first_pair, second_pair, current_epoch)
        else:
            second_pair = second_data_list
            print("[FORMING PAIRS] Second data list exists, importing this one.")
        print("[FORMING PAIRS] First pair", first_pair)
        print("[FORMING PAIRS] Second pair", second_pair)
        
        global epoch_parameter_f_p,  best_array, best_epoch
        epoch_parameter_f_p = 0
        if epochs == -1:
            epoch_parameter_f_p = current_epoch_infinite
        else:
            epoch_parameter_f_p = current_epoch
        
        if array1_fitness > best_fitness:
            best_fitness = array1_fitness
            best_array = first_pair
            best_epoch = epoch_parameter_f_p
            # aux.save_best_generation(name_file_report, first_pair, array1_fitness, epoch_parameter_f_p)
            
        if array2_fitness > best_fitness:
            best_fitness = array2_fitness
            best_array = second_pair
            best_epoch = epoch_parameter_f_p
            # aux.save_best_generation(name_file_report, second_pair, array2_fitness, epoch_parameter_f_p)
        
        information_crossover(first_pair, second_pair, current_epoch, current_epoch_infinite)
    else:
        print(f"\n[FORMING PAIRS] Process finished. Epochs limit reached.", "Current epoch:", current_epoch, "Epochs:", "Obtain the best fitness value." if epochs == -1 else epochs)
        if array1_fitness < array2_fitness:
            print(f"[FORMING PAIRS] Best fitness value found. Current Epoch: {'<<Hallar mejor fitness>>' if epochs == -1 else current_epoch} Process finished.\n[FORMING PAIRS] Best array [first_list]:\n\t{data_list}")
        else:
            print(f"[FORMING PAIRS] Best fitness value found. Current Epoch: {'<<Hallar mejor fitness>>' if epochs == -1 else current_epoch} Process finished.\n[FORMING PAIRS] Best array [second_list]:\n\t{second_data_list}")
    
def information_crossover(first_pair, second_pair, current_epoch, current_epoch_infinite):
    print("\n[CROSSOVER] Epoch: ", current_epoch)
    if len(first_pair) >= 3:
        print("[CROSSOVER] Crossover can be performed. Arrays are greater than 3 elements.")
        arr1, arr2 = aux.swap_elements(first_pair, second_pair, p_mut_cruza, p_mut_ind)
        mutation(arr1, arr2, current_epoch, current_epoch_infinite)
    else:
        print("[CROSSOVER] Crossover can't be performed. Arrays are less than 3 elements.")
        
def mutation(first_pair, second_pair, current_epoch, current_epoch_infinite):
    global p_mut_gen
    percentage_per_element = 100/len(first_pair)
    jumps = int(p_mut_gen//percentage_per_element)

    print(f"\n[MUTATION] Epoch: {current_epoch}")
    print("[MUTATION] Percentage per element:", percentage_per_element, "%")
    
    operator = aux.define_operator(selected_option)
    
    print("[MUTATION] Jumps required:", jumps)
    print(f"[MUTATION] Array parameters: \n\tFirst: {first_pair}\n\tSecond: {second_pair}")
    print(f"[MUTATION] Current INFITE EPOCH: {current_epoch_infinite}")
    if current_epoch >= 25 or current_epoch_infinite >= 25:
        print("\n[MUTATION] Mutation for FIRST ARRAY initialized")
        arr1 = sorted(first_pair, key=lambda x: int(x.split('-')[0]))
        print("[MUTATION] [X] Mutation for FIRST ARRAY is not required. Array is already forced sorted.")
        
        print("\n[MUTATION] Mutation for SECOND ARRAY initialized")
        arr2 = sorted(second_pair, key=lambda x: int(x.split('-')[0]))
        print("[MUTATION] [X] Mutation for SECOND ARRAY is not required. Array is already forced sorted.")
    else:
        print("\n[MUTATION] Mutation for FIRST ARRAY initialized")
        arr1 = aux.mutation_for_array_parameter(first_pair, operator, p_mut_gen, percentage_per_element, jumps)

        print("\n[MUTATION] Mutation for SECOND ARRAY initialized")
        arr2 = aux.mutation_for_array_parameter(second_pair, operator, p_mut_gen, percentage_per_element, jumps)
    
    pruning(arr1, arr2, operator, percentage_per_element, current_epoch, current_epoch_infinite)
    
def pruning(first_pair, second_pair, operator, percentage_per_element, current_epoch, current_epoch_infinite):
    # global current_epoch_infinite
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
    
    if epochs == -1:
        pass
    else:
        current_epoch += 1
    
    global epoch_parameter
    epoch_parameter = 0
    if epochs == -1:
        epoch_parameter = current_epoch_infinite
    else:
        epoch_parameter = current_epoch
    current_epoch_infinite += 1
    aux.save_generation(name_file_report, first_pair, second_pair, epoch_parameter, fitness_arr1, fitness_arr2)
    time.sleep(.025)
    form_pairs(first_pair, second_pair, fitness_arr1, fitness_arr2, epoch_parameter, current_epoch_infinite)
    # Los mejores son puestos debajo de los 2 primeros creados al inicio en el excel de "reports" actual del programa, y hasta
    # abajo despues de colocar cada resultado por epoca, se pone el mejor de todos los resultados.

def calculate_fitness_base(fitness, current_epoch):
    if current_epoch % 3 == 0 and current_epoch != 0:
        fitness -= 1
    
    return fitness
