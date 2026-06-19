import pandas as pd
import numpy as np

datos_titanic = {
    'pasajero_id': range(1, 21),
    'nombre': ['Mr. Owen Harris', 'Mrs. John Bradley', 'Miss. Lottie', 
               'Mrs. Jacques Heath', 'Mr. William Henry', 'Miss. Dorothy',
               'Mr. James', 'Mrs. Henry', 'Mr. John', 'Miss. Anna',
               'Mr. Alberto', 'Mrs. Carl', 'Mr. Teodore', 'Miss. Margaret',
               'Mrs. John Jacob', 'Mr. George', 'Miss. Eileen', 'Mr. William',
               'Mrs. Thomas', 'Master. John'],
    'sexo': ['male', 'female', 'female', 'female', 'male', 'female',
             'male', 'female', 'male', 'female', 'male', 'female',
             'male', 'female', 'female', 'male', 'female', 'male',
             'female', 'male'],
    'edad': [22.0, 38.0, 26.0, 35.0, 35.0, 27.0, np.nan, 54.0, 2.0, 
             27.0, 20.0, 40.0, 30.0, 22.0, np.nan, 51.0, 19.0, 35.0, 
             np.nan, 18.0],
    'clase': [3, 1, 3, 1, 3, 3, 1, 1, 3, 3, 2, 1, 3, 3, 1, 2, 3, 3, 1, 3],
    'tarifa': [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 25.93, 21.07,
               7.88, 13.00, 30.50, 7.85, 8.67, 30.50, 26.55, 8.03, 21.07,
               247.52, 13.00],
    'hermanos_conyuge': [1, 1, 0, 1, 0, 0, 0, 1, 3, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2],
    'padres_hijos': [0, 0, 0, 0, 0, 2, 0, 1, 1, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 1],
    'sobrevive': [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    'embarcado': ['S', 'C', 'S', 'S', 'S', 'Q', 'S', 'S', 'S', 'S', 'S', 'C', 
                  'S', 'S', 'S', 'S', 'Q', 'S', 'C', 'S']
}

df_limpio = pd.DataFrame(datos_titanic)

edad = df_limpio['edad'].values
tarifa = df_limpio['tarifa'].values
sobrevive = df_limpio['sobrevive'].values

def analisis_numpy(datos,nombre):
    print(f"\n Analisis de {nombre}:")
    print(f" count: {len(datos)}")
    print(f" media: {np.mean(datos):.2f}")
    print(f" mediana: {np.median(datos):.2f}")
    print(f" std: {np.std(datos):.2f}")
    print(f" min: {np.min(datos):.2f}")
    print(f" max: {np.max(datos):.2f}")
    print(f" Rango: {np.ptp(datos):.2f}")

    # Cuantiles
    print(f"\n  Cuantiles:")
    print(f" Q1 (25%): {np.percentile(datos, 25):.2f}")
    print(f" Q2 (50% - Mediana): {np.percentile(datos, 50):.2f}")
    print(f" Q3 (75%): {np.percentile(datos, 75):.2f}")
    print(f" IQR: {np.percentile(datos, 75) - np.percentile(datos, 25):.2f}")

    analisis_numpy(edad, "Edad")
    analisis_numpy(tarifa, "Tarifa")
    analisis_numpy(sobrevive, "Sobrevive")
