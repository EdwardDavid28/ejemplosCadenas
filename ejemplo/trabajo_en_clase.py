price=97
texto3=f"the price is: {price:.2f} dollars"
print(texto3)

texto4=f"la multiplicacion es: {20*59} "
print(texto4)

texto5="python es un lenguaje de alto nivel"
result1=texto5.capitalize()
print(result1)

#String casefold()
titulo="Cien Años De Soledad"
tituloConvertido=titulo.casefold()
print(tituloConvertido)

#String Center()
fruta="banana"
centrarCadena=fruta.center(20,"-")
print(centrarCadena)

#String count
titulo1="yo amo las manzanas,las manzanas es mi fruta favorita"
result2=titulo1.count("manzanas")
print(result2)

#String endswith
texto6="curso.fundamentos con Python."
result3=texto6.endswith(".")
print(result3)

#String expandtabs
Letra=("F")

#String find
texto7="Hola, bienvenidos a Colombia"
result4=texto7.find("bienvenidos")
print(result4)

#Funcion title
texto8="bienvenidos a mi mundo"
result5=texto8.title()
print(result5)

#Funcion isalnum
alfanumerico="Python321"
result6=alfanumerico.isalnum()
print(result6)

#Funcion isalpha
letras="Space X"
result7=letras.isalpha()
print(result7)

