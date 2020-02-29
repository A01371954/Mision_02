#Roberto Sobrado
#Calcular distancia entre dos puntos

x1= int(input("¿Cuál es el valor de x1?"))
y1= int(input("¿Cuál es el valor de y1?"))
x2= int(input("¿Cuál es el valor de x2?"))
y2= int(input("¿Cuál es el valor de y2?"))

d= ((x2-x1)**2+(y2-y1)**2)**0.5

print ("x1: %d" % (x1))
print ("y1: %d" % (y1))
print ("x2: %d" % (x2))
print ("y2: %d" % (y2))
print ("Distancia: %.3f" % (d))