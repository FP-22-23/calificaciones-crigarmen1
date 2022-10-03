
from calificaciones import *

def test_calcula_nota_cuestionario(aciertos,errores,totalRespuestas):
    nota=calcula_nota_cuestionario(aciertos, errores, totalRespuestas)
    print("La nota del cuestionario es ", nota)

'''def test_calcula_nota_evaluacion_continua(cuestionarios,parciales,proyectos):
    notafinal=calcula_nota_evaluacion_continua(cuestionarios,parciales,proyectos)
    print('La nota final es: ', notafinal)'''

def main():
    aciertos, errores, totalRespuestas = devuelve_datos()
    test_calcula_nota_cuestionario(aciertos, errores, totalRespuestas)

    C1 = devuelve_cuestionario('Nota cuestionario 1: ')
    C2 = devuelve_cuestionario('Nota cuestionario 2: ')
    C3 = devuelve_cuestionario('Nota cuestionario 3: ')
    parcial1= devuelve_parcial('Nota parcial 1: ')
    proyecto1 = devuelve_proyecto('Nota proyecto 1: ')
    nota_cuatrimestre1 = calcula_nota_cuatrimestre(C1,C2,C3,parcial1,proyecto1)
    print('La nota del cuatrimestre 1 es: ', nota_cuatrimestre1)

    C4 = devuelve_cuestionario('Nota cuestionario 4: ')
    C5 = devuelve_cuestionario('Nota cuestionario 5: ')
    C6 = devuelve_cuestionario('Nota cuestionario 6: ')
    parcial2= devuelve_parcial('Nota parcial 2: ')
    proyecto2 = devuelve_proyecto('Nota proyecto 2: ')
    nota_cuatrimestre2 = calcula_nota_cuatrimestre(C4,C5,C6,parcial2,proyecto2)
    print('La nota del cuatrimestre 2 es: ', nota_cuatrimestre2)

    cuestionarios=devuelve_cuestionarios()
    parciales=devuelve_parciales()
    proyectos=devuelve_proyectos()
    notafinal = calcula_nota_evaluacion_continua(cuestionarios,parciales,proyectos)
    print('La nota final es:', notafinal)

if __name__=='__main__':
    main()