# Satisfaccion de restricciones

# Problema: ====================================================

# al inicio hay que definir una lista de tareas
# cada TAREA tiene:
# - Identificacion
# - Duracion
# - Requerimientos de Maquina (Tipo)

# ademas hay que cargar las maquinas que tenemos
# cada MAQUINA tiene:
# - Identificador
# - Tipo

# Variables: ====================================================
# TSi: periodo en que se inicia la tarea (num entero de periodos ej horas)
# TMi: lista de maquinas del tipo que se requieran (puede haber mas de una maquina de ese tipo)

# Restricciones: ====================================================
# una restriccion Cr involucra 4 variables (TSi,TMi,TSj,TMj)

# NOTA:
# Hay que definir al incio: variables, dominio y restricciones
# luego es usar un A* para ir buscando en el arbol,
# solo que cada rama no tiene todas las posibles combinaciones
# sino aquellas que cumplan las restricciones.