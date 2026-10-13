import os
import matplotlib.pyplot as plt
from datetime import datetime

# Ruta de tu archivo de base de datos
file_path = os.path.expanduser("~/Documents/Projects/Weight_progress/weight_db.txt")

dates = []
weights = []

# Leer y parsear el archivo
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split("-")
        if len(parts) == 5:
            day, month, year, weight_str, time_str = parts
            dt = datetime.strptime(f"{day}-{month}-{year} {time_str}", "%d-%m-%Y %H:%M")
            weight = float(weight_str)
            
            dates.append(dt)
            weights.append(weight)

# Ordenar cronológicamente por fecha
data = sorted(zip(dates, weights), key=lambda x: x[0])
sorted_dates = [x[0] for x in data]
sorted_weights = [x[1] for x in data]

# Configuración de la figura
plt.figure(figsize=(12, 6))
plt.plot(sorted_dates, sorted_weights, marker="o", linestyle="-", color="#1f77b4", linewidth=2)

# Mostrar la cifra (peso) en cada punto de la gráfica
for dt, weight in zip(sorted_dates, sorted_weights):
    plt.annotate(
        f"{weight}", 
        (dt, weight), 
        textcoords="offset points", 
        xytext=(0, 10), # Desplazamiento en pixeles (arriba del punto)
        ha='center', 
        fontsize=9,
        fontweight='bold'
    )

# Forzar a que aparezcan TODAS las fechas en el eje X
plt.xticks(sorted_dates, [dt.strftime("%d-%m-%Y") for dt in sorted_dates], rotation=45, ha='right')

# Estética de la gráfica
plt.title("Progreso de Peso", fontsize=14, fontweight="bold")
plt.xlabel("Fecha y Hora", fontsize=10)
plt.ylabel("Peso (kg)", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()