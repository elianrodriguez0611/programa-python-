# Matriz con la información: nombre y horas cada día de la semana
registro_horas = [
    ["María", 8, 8, 9, 8, 8],
    ["Pedro", 7, 7, 7, 7, 7],
    ["Sofía", 9, 9, 8, 8, 9],
    ["Andrés", 8, 8, 8, 7, 6]
]

# Función para calcular el total y ver el tipo de jornada
def revisar_horas(matriz, limite=40):
    resultados = []
    for persona in matriz:
        nombre = persona[0]
        # Sumo todas las horas de la semana
        total = sum(persona[1:])
        
        # Defino si hizo sobretiempo o no
        if total > limite:
            estado = "Sobretiempo"
        else:
            estado = "Horario Estándar o inferior"
        
        resultados.append([nombre, total, estado])
    return resultados

# Ejecuto el cálculo
datos_finales = revisar_horas(registro_horas)

# Imprimo todo de forma ordenada
print("Resumen de horas trabajadas esta semana:\n")
for nombre, horas, tipo in datos_finales:
    print(f"Nombre: {nombre}")
    print(f"Total de horas: {horas}")
    print(f"Clasificación: {tipo}")
    print("-" * 30)
    
