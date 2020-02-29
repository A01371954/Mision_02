#Roberto Sobrado
#calcular ingredientes para galletas

xg= int(input ("¿Cuántas galletas quieres hace?"))

ya= (xg*1.5)/48
ym= (xg*1)/48
yh= (xg*2.75)/48

print ("Para elaborar %d galletas, necesitas los siguientes ingredientes:" % (xg))
print ("- %.2f tazas de azúcar." % (ya))
print ("- %.2f tazas de mantequilla." % (ym))
print ("- %.2f tazas de harina." % (yh))
