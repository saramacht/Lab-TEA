#Tendencias e Innovacion en Tecnologia Agricola (TEA)
minutos= input ("minutos jugados?")
valorPorMinuto= input("valor por minuto?")

#se utiliza la conversión de tipo a int
#sino se hace la conversión existira error porque trata de multiplicar strings
#calculando el valor total de los minutos jugados
total= int(minutos) * int(valorPorMinuto)
