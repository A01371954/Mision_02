#Roberto Sobrado
#Calcular costos en una comida

t= int(input ("Cuanto consumio en el restaurante?"))

p= t*0.13
i= t*0.16
z= t+p+i

print ("Costo de su comida: $%.2f" % (t))
print ("Propina: $%.2f" % (p))
print ("IVA: $%.2f" % (i))
print ("Total a pagar: $%.2f" % (z))
print ("Gracias por su preferencia.")
