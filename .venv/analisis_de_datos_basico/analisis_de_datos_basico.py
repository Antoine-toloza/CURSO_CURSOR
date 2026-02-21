"""
Análisis de datos básico: estadísticas y gráfica de dispersión
"""
import os
import pandas as pd
import plotly.express as px

# Directorio del script para rutas relativas
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Cargar datos
df = pd.read_csv(os.path.join(SCRIPT_DIR, "base_de_datos.csv"), sep=";", encoding="latin-1")

# 1. Estadísticas solicitadas: total de RUT y conteo por FACT_FINANCIADOR
print("=" * 60)
print("RESUMEN RUT Y FACT_FINANCIADOR")
print("=" * 60)

# Columna 3: RUT (por nombre)
col_rut = "RUT"
total_registros = len(df)
print(f"\nColumna '{col_rut}' - Total de registros: {total_registros}")

# Columna 4: FACT_FINANCIADOR (conteo por categoría)
col_fin = "FACT_FINANCIADOR"
print(f"\nColumna '{col_fin}' - Cantidad por categoría:")
conteos_fin = df[col_fin].value_counts(dropna=False)
for categoria, cantidad in conteos_fin.items():
    print(f"  {categoria}: {cantidad}")

# 2. Gráfico dinámico: FECHA vs cantidad de RUT por FACT_FINANCIADOR
# Nos aseguramos de que la columna FECHA sea de tipo datetime
col_fecha = "FECHA"
df[col_fecha] = pd.to_datetime(df[col_fecha], errors="coerce")

# Agrupamos por FECHA y FACT_FINANCIADOR contando registros (RUT)
df_group = (
    df.groupby([col_fecha, col_fin])
    .size()
    .reset_index(name="cantidad_rut")
    .sort_values(col_fecha)
)

fig = px.line(
    df_group,
    x=col_fecha,
    y="cantidad_rut",
    color=col_fin,
    markers=True,
    title=f"Evolución de cantidad de RUT por FACT_FINANCIADOR (Total registros: {total_registros})",
)
fig.update_layout(xaxis_title="FECHA", yaxis_title="Cantidad de RUT")

output_html = os.path.join(SCRIPT_DIR, "grafico_dinamico_rut_fact_financiador_fecha.html")
fig.write_html(output_html, auto_open=False)
print("\n" + "=" * 60)
print(f"Gráfico dinámico guardado como archivo HTML: {output_html}")
print("Ábrelo en tu navegador para interactuar con él.")
print("=" * 60)
