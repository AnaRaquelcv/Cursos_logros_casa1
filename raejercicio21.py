numero1 = int(input("ingresar primer numero:"))
numero2 = int(input("ingresar segundo numero:"))
numero3 = int(input("ingresar tercer numero:"))

# Corrige la fórmula para calcular el mayor
mayor = (numero1 if (numero1 >= numero2 and numero1 >= numero3) else
         numero2 if (numero2 >= numero1 and numero2 >= numero3) else
         numero3)

# Corrige la fórmula para calcular el menor
menor = (numero1 if (numero1 <= numero2 and numero1 <= numero3) else
         numero2 if (numero2 <= numero1 and numero2 <= numero3) else
         numero3)

print(f"el numero mayor es: {mayor}")
print(f"el numero menor es: {menor}")