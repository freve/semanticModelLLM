# Archivo generado para 30 iteraciones independientes del prompt heuristico


def clasificar_estudiante_exp_1(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_2(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_3(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_4(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_5(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_6(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_7(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_8(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_9(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_10(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_11(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_12(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_13(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_14(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_15(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_16(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_17(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_18(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_19(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_20(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_21(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_22(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_23(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_24(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_25(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_26(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_27(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1


def clasificar_estudiante_exp_28(nota1, nota2, nota3, intentos1):
    prom = (nota1 + nota2 + nota3) / 3
    
    # Evaluacion de Riesgo
    if nota1 == 0.0 or prom < 3.0 or nota3 < 2.0:
        return 0
        
    # Evaluacion de Excelencia
    if (prom >= 4.4 and nota1 >= 3.8) or (prom >= 4.3 and intentos1 > 15):
        return 2
        
    # Por defecto, Medio
    return 1


def clasificar_estudiante_exp_29(nota1, nota2, nota3, intentos1):
    '''Clasificador heuristico basado en reglas semanticas y pedagogicas.'''
    promedio_labs = sum([nota1, nota2, nota3]) / 3.0
    
    # Tolerancia Cero y Colapso
    if nota1 == 0.0:
        riesgo = True
    elif promedio_labs < 3.0:
        riesgo = True
    elif nota3 < 2.0:
        riesgo = True
    else:
        riesgo = False
        
    if riesgo:
        return 0
        
    # Consistencia y Bonus
    if promedio_labs >= 4.4 and nota1 >= 3.8:
        return 2
    elif promedio_labs >= 4.3 and intentos1 > 15:
        return 2
    else:
        return 1


def clasificar_estudiante_exp_30(nota1, nota2, nota3, intentos1):
    # Promedio general de laboratorios
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    # 1. Reglas de Riesgo (Prioridad Maxima - Clase 0)
    if nota1 == 0.0: return 0
    if promedio < 3.0: return 0
    if nota3 < 2.0: return 0
    
    # 2. Reglas de Excelencia (Clase 2)
    if promedio >= 4.4 and nota1 >= 3.8: return 2
    if promedio >= 4.3 and intentos1 > 15: return 2
    
    # 3. Desempeño Medio (Clase 1)
    return 1

