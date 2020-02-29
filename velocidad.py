#Roberto Sobrado
#Calcula distancias y tiempos recorridas a cierta velocidad

v= int(input("¿A qué velocidad viaja usted (en km/h)?"))

d6= 6*v
d3= 3.5*v
t485= 485/v

print ("Distancia recorrida en 6 hrs: %.1fkm" % (d6))
print ("Distancia recorrida en 3.5 hrs: %.1fkm" % (d3))
print ("Tiempo para recorrer 485 km: %.1fhrs." % (t485))