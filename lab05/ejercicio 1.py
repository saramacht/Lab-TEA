cadena="X-DSPAM-Confidence:0.8475"
inicio= cadena.find(":")+1
final=len(cadena)
final2= cadena.find(",")
numero=float(cadena[inicio:final])
print(numero)
print(type(numero))



