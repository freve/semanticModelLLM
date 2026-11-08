# Modelo Semántico LLM
Predicción del rendimiento de los estudiantes de programación usando modelos de lenguaje de gran tamaño (LLM)

# Resumen
Este trabajo aborda el uso de los modelos de lenguaje de gran tamaño (LLM) para predecir el desempeño académico en cursos de programación, con el fin de reducir la deserción y mejorar el aprendizaje. El objetivo central es evaluar la eficacia de los LLM para pronosticar los resultados de los estudiantes a partir de las primeras entregas en un curso de programación, teniendo en cuenta su calificación y el número de intentos. La metodología es cuantitativa y comparativa, se utilizaron conjuntos de datos de entregas en cursos de programación, datos publicados en el repositorio Zenodo para entrenar modelos tipo GPT, cuyos resultados se contrastaron con algoritmos de aprendizaje automático tradicionales publicados y referenciados en el estado del arte. Los principales resultados muestran que los LLM poseen una precisión adecuada (86%) comparado con algoritmos de aprendizaje automático más complejos que dan una mayor precisión (96%) en la semana 7, usados para identificar patrones de éxito o fracaso, gracias a la capacidad de interpretación semántica, los cuales son capaces de encontrar reglas del tipo IF-Then a partir del conjunto de datos, reglas que tienen una semántica asociada. Se concluye que el uso de estas herramientas permite una intervención pedagógica temprana y personalizada, consolidando a los LLM como un recurso que permite el uso de la predicción del desempeño de los estudiantes en el aula, convirtiéndose en una herramienta de fácil uso y con un impacto positivo en los procesos de enseñanza-aprendizaje de la programación.

# Ejecutar prompt
Para la predicción del desempeño estudiantil basada en ingeniería de prompts (Prompt Engineering) aplicada a LLM específicamente usando Gemini 3 - Pro.

Se utilizó el razonamiento en contexto (in-context learning) como mecanismo de inferencia predictiva.

La hipótesis de trabajo consistió en que un LLM puede, mediante instrucción cuidadosamente diseñada, replicar o aproximar la tarea de clasificación trinaria (0: Bajo, 1: Medio, 2: Alto) que en el modelo original requirió entrenamiento supervisado con 468 registros.

Inyección de datos de entrenamiento archivo DataEarlyPrediction_Train (se encuentran en la carpeta datos) y artículo científico peerj-cs-1655 (archivo adjunto) como contexto semántico, implementando un mecanismo de RAG implícito.

Se suministra DataEarlyPrediction_TestSinClase.xlsx (dataset sin etiquetas), requiriendo al modelo generar predicciones autónomas para cada instancia, operando como clasificador zero-label

Se proporciona DataEarlyPrediction_Test.xlsx (ground truth) para que el modelo compare predicciones con valores reales y calcule métricas de precisión.

Se instruye al modelo a contrastar sus métricas con los resultados reportados en el artículo científico.

# Resultados obtenidos

El algoritmo generado por Gemini se puede apreciar como archivo adjunto (modelo-semanticoLLM), es un algoritmo simple basado en un análisis semántico y reglas de asociación. Aclarando que la Nota1 corresponde al Laboratorio 1, la Nota2 al laboratorio 2 y Nota3 al Laboratorio 3, con correspondencia a lo presentado en el artículo científico de referencia.

Métricas por clase para el Modelo Semántico. Gemini 3 - Pro
Clase / Métrica	FPR	Recall	AUC
Clase (0): Desempeño Bajo	0.095	0.967	0.936
Clase (1): Desempeño medio	0.100	0.818	0.859
Clase (2): Desempeño alto	0.026	0.789	0.881
Promedio Macro (AUC Global)			0.892

La incorporación de reglas pedagógicas interpretables como la 'tolerancia cero' ante la falta de entregas iniciales permite alcanzar un rendimiento competitivo del 86.17%.