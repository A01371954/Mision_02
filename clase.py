#Roberto Sobrado
#calcular % de alunos mujeres y hombres

m= int(input("¿Cuántas mujeres hay en tu clase?"))
h= int(input("¿Cuántos hombres hay en tu clase?"))

t= m+h
mp= (m*100)/t
hp= (h*100)/t

print ("Total de alumnos inscritos: %d" % (t))
print ("Porcentaje de mujeres: %.1f%%" % (mp))
print ("Porcentaje de hombres: %.1f%%" % (hp))
