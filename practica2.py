#Crear un programa que permita realizar las operaciones basicas +,-,*,/ utilizando un funciones para cada operacion y un menu principal para desplegar y elegir que operacion realizemos


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

print("Calculadora de Operaciones Basicas")
print("")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = input("Elige una opcion escribiendo su numero: ")

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

if opcion == "1":
    print("Resultado:", suma(num1, num2))

elif opcion == "2":
    print("Resultado:", resta(num1, num2))

elif opcion == "3":
    print("Resultado:", multiplicacion(num1, num2))

elif opcion == "4":
    print("Resultado:", division(num1, num2))

else:
    print("Error")
