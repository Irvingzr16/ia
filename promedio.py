nombre=str(input("Ingresa tu nombre: "))
materias=["materia1","materia2","materia3","materia4","materia5"]
trimestres=["trimestre1","trimestre2","trimestre3"]

calificaciones={}

for materia in materias:
    print("Calicaciones de {materia}:")
    calificaciones [materia]={}
    for trimestre in trimestres:
        calificacion=float(input("Ingresa la calificacion de {materia} en {trimestre}: "))
        calificaciones[materia][trimestre]=calificacion

        promedio=sum(calificaciones[materia].values())/len(trimestres)
        print("Promedio de {materia}: {promedio:.2f}")