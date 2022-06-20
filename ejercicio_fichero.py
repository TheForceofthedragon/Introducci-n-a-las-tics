
numero = int(input("Ingrese un número entero entre 1 y 10: "))
fichero = "tabla-n" + ".txt"
f = open(fichero, "w")

for i in range (1,13):
    m = i * numero 
    print(numero ,"*",i , "= ", m)