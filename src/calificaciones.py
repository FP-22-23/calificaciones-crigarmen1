from statistics import mean

def calcula_nota_cuestionario(aciertos,errores,totalRespuestas):
    nota = aciertos*10/totalRespuestas-errores*10/(50-totalRespuestas)
    return max(0,nota)

def devuelve_datos():
    aciertos=int(input('Número de aciertos: '))
    errores=int(input('Número de errores: '))
    totalRespuestas=int(input('Total de respuestas: '))
    return(aciertos,errores,totalRespuestas)

def calcula_nota_cuatrimestre(C1,C2,C3,parcial,proyecto):
    if proyecto < 5:
        nota = 3
    else:
        nota= 0.1*(C1+C2+C3) + 0.6*parcial +0.1*proyecto
    return nota

def devuelve_cuestionario(mensaje):
    nota = float(input(mensaje))
    return nota

def devuelve_parcial(mensaje):
    nota = float(input(mensaje))
    return nota

def devuelve_proyecto(mensaje):
    nota = float(input(mensaje))
    return nota

def calcula_nota_cuatrimestre_para_evaluacion(cuestionarios,parcial,proyecto):
    if proyecto < 5:
        nota = 3
    else:
        nota= 0.1*sum(cuestionarios) + 0.6*parcial +0.1*proyecto
    return nota

def calcula_nota_evaluacion_continua(cuestionarios,parciales,proyectos):
    cuatrimestre1=calcula_nota_cuatrimestre_para_evaluacion(cuestionarios[0:3], parciales[0], proyectos[0])
    cuatrimestre2=calcula_nota_cuatrimestre_para_evaluacion(cuestionarios[3:6], parciales[1], proyectos[1])
    nota=4
    if cuatrimestre1>=4 and cuatrimestre2>=4:
        nota=mean((cuatrimestre1, cuatrimestre2))
    return nota

def devuelve_cuestionarios():
    C1=float(input('Nota cuestionario 1: '))
    C2=float(input('Nota cuestionario 2: '))
    C3=float(input('Nota cuestionario 3: '))
    C4=float(input('Nota cuestionario 4: '))
    C5=float(input('Nota cuestionario 5: '))
    C6=float(input('Nota cuestionario 6: '))
    return(C1,C2,C3,C4,C5,C6)

def devuelve_parciales():
    parcial1=float(input('Nota parcial 1: '))
    parcial2=float(input('Nota parcial 2: '))
    return(parcial1,parcial2)

def devuelve_proyectos():
    proyecto1=float(input('Nota proyecto 1: '))
    proyecto2=float(input('Nota proyecto 2: '))
    return(proyecto1,proyecto2)

'''def calcula_nota_cuatrimestre(cuestionarios,parcial,proyecto):
    if proyecto < 5:
        nota = 3
    else:
        nota= 0.1*sum(cuestionarios[0:2]) + 0.6*parcial +0.1*proyecto
    return nota

def calcula_nota_evaluacion_continua(cuestionarios,parciales,proyectos):
    cuatrimestre1=calcula_nota_cuatrimestre(cuestionarios[0:2], parciales[0], proyectos[0])
    cuatrimestre2=calcula_nota_cuatrimestre(cuestionarios[2:5], parciales[1], proyectos[1])
    nota=4
    if cuatrimestre1>=4 and cuatrimestre2>=4:
        nota=(cuatrimestre1+cuatrimestre2)/2
    return nota

def devuelve_cuestionarios():
    C1=float(input('Nota cuestionario 1: '))
    C2=float(input('Nota cuestionario 2: '))
    C3=float(input('Nota cuestionario 3: '))
    C4=float(input('Nota cuestionario 4: '))
    C5=float(input('Nota cuestionario 5: '))
    C6=float(input('Nota cuestionario 6: '))
    return(C1,C2,C3,C4,C5,C6)

def devuelve_parciales():
    parcial1=float(input('Nota parcial 1: '))
    parcial2=float(input('Nota parcial 2: '))
    return(parcial1,parcial2)

def devuelve_proyectos():
    proyecto1=float(input('Nota proyecto 1: '))
    proyecto2=float(input('Nota proyecto 2: '))
    return(proyecto1,proyecto2)'''




