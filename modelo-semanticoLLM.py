def clasificar_estudiante_optimizado(nota1, nota2, nota3, intentos1):
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # --- REGLAS DE RIESGO (Prioridad Máxima) ---
    # 1. Tolerancia Cero: Si falló la primera entrega (0.0), es riesgo alto
    #    independientemente de su recuperación posterior.
    if nota1 == 0.0:
        return 0 
    
    # 2. Promedio Insuficiente o Caída Final
    if promedio < 3.0 or nota3 < 2.0:
        return 0
        
    # --- REGLAS DE EXCELENCIA ---
    # 3. Alto Desempeño: Requiere promedio alto Y buen inicio (consistencia)
    if promedio >= 4.4 and nota1 >= 3.8:
        return 2
        
    # 4. Bonus por Persistencia: Buen promedio + Esfuerzo masivo (>15 intentos)
    if promedio >= 4.3 and intentos1 > 15:
        return 2
        
    # --- DESEMPEÑO MEDIO ---
    return 1