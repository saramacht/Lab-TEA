cantidad= 0
suma=0
primerNumero= True
while True:
    try:
        numero= input("Ingrese un numero:")
        if(numero== "fin"):
            break
        cantidad= cantidad + 1
        suma= suma + int(numero)
        
    except:
        print("dato erróneo")

print ("Cantidad de números", cantidad)
print ("Total", suma)
print ("Media", suma/cantidad)


        