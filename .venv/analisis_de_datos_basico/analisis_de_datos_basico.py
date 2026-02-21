"""
Análisis de datos básico: estadísticas y gráfica de dispersión
"""
import os
import pandas as pd

# Directorio del script para rutas relativas
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
import matplotlib
matplotlib.use("Agg")  # Backend sin ventana para ejecución por CLI
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv(os.path.join(SCRIPT_DIR, "base_de_datos.csv"), sep=";", encoding="latin-1")

# 1. Estadísticas simples por columna (media, mediana, desviación estándar)
print("=" * 60)
print("ESTADÍSTICAS POR COLUMNA")
print("=" * 60)

# Solo para columnas numéricas
columnas_numericas = df.select_dtypes(include=["number"]).columns

for col in df.columns:
    if col in columnas_numericas:
        media = df[col].mean()
        mediana = df[col].median()
        desv_estandar = df[col].std()
        print(f"\n{col}:")
        print(f"  Media:           {media:.2f}")
        print(f"  Mediana:         {mediana:.2f}")
        print(f"  Desv. estándar:  {desv_estandar:.2f}")
    else:
        print(f"\n{col}: (categórica - sin media/mediana/std)")

# 2. Gráfica de dispersión col2 vs col9
# col2 = índice 2, col9 = índice 9 (por posición en el DataFrame)
col2 = df.columns[2]  # RUT
col9 = df.columns[9]  # MODALIDAD

# Si col9 es categórica, la codificamos numéricamente para el scatter
x = df[col2]
y_raw = df[col9]

if pd.api.types.is_numeric_dtype(y_raw):
    y = y_raw
else:
    y, _ = pd.factorize(y_raw)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.7, c="steelblue", edgecolors="darkblue")
plt.xlabel(col2)
plt.ylabel(col9)
plt.title(f"Gráfica de dispersión: {col2} vs {col9}")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, "scatter_col2_vs_col9.png"))
print("\n" + "=" * 60)
print("Gráfica guardada como: scatter_col2_vs_col9.png")
print("=" * 60)
