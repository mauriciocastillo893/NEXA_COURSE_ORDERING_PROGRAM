import openpyxl
from tkinter import filedialog
import pandas as pd
import os

def open_excel_file():
    # Obtener la ruta del directorio del script actual
    project_route = os.path.dirname(__file__)
    
    # Unir la ruta del proyecto con el nombre de la carpeta "excel"
    default_route = os.path.join(project_route, "excel_files")

    # Verificar si la ruta predeterminada es válida
    if os.path.exists(default_route):
        file_route = filedialog.askopenfilename(initialdir=default_route, filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    else:
        print("[EXCEL WHILE] The default route does not exist.")
        file_route = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    # Verificar si se seleccionó un archivo
    if file_route:
        # Leer el archivo Excel seleccionado usando pandas
        try:
            df = pd.read_excel(file_route)
            print("[EXCEL WHILE] Excel file read successfully.")
            print(df)
            process_excel_file(df)
            return {"success": "Archivos creados exitosamente en la carpeta 'temp_files'."}
        except Exception as e:
            print(f"[EXCEL WHILE] Error reading the Excel file: {e}")
            return {"error": e}
    else:
        print("[EXCEL WHILE] No file selected.")
        
def process_excel_file(df_file):
    if not os.path.exists('temp_files'):
        os.makedirs('temp_files')
        
    # Crear el primer archivo "duration"
    df_duration = df_file[['Nombre de curso', 'Duración (en minutos)']].rename(columns={'Nombre de curso': 'id', 'Duración (en minutos)': 'level'})
    df_duration.to_excel('temp_files/duration.xlsx', index=False)

    # Crear el segundo archivo "difficulty"
    df_difficulty = df_file[['Nombre de curso', 'Dificultad']].rename(columns={'Nombre de curso': 'id', 'Dificultad': 'level'})
    df_difficulty['conversion_num'] = df_difficulty['level'].apply(convert_difficulty)
    df_difficulty.to_excel('temp_files/difficulty.xlsx', index=False)

    # Crear el tercer archivo "requirements"
    df_requirements = df_file[['Nombre de curso', 'Requisitos']].rename(columns={'Nombre de curso': 'id', 'Requisitos': 'size'})
    df_requirements['conversion_num'] = df_requirements['size'].apply(lambda x: 0 if pd.isna(x) else len(str(x).split(',')))
    df_requirements.to_excel('temp_files/requirements.xlsx', index=False)

    print("\n[EXCEL WHILE] Files created successfully in the 'temp_files' folder.")

def convert_difficulty(difficulty):
    difficulty = str(difficulty).lower()
    if difficulty in ['facil', 'fácil', '0', 'easy']:
        return 0
    elif difficulty in ['media', 'medio', '1', 'medium']:
        return 1
    elif difficulty in ['difícil', 'dificil', '2', 'hard']:
        return 2
    elif difficulty in ['muy difícil', 'muy dificil', '3', 'very hard']:
        return 3
    elif difficulty in ['insano', 'maestro', '4', 'insane', 'master']:
        return 4
    else:
        return 0