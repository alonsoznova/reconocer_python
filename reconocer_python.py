num1 = 42  #declaración de variable (Número)
num2 = 2.3  #declaración de variable (Número)
boolean = True  #declaración de variable (Booleano)
string = 'Hello World'  #declaración de variable (Cadena)
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalapeños', 'Queso', 'Aceitunas']  #declaración de variable (Lista)
person = {'nombre': 'John', 'ubicación': 'Salt Lake', 'edad': 37, 'está_calvo': False}  #declaración de variable (Diccionario)
fruta = ('arándano', 'fresa', 'plátano')  #declaración de variable (Tupla)
print(type(fruta))  #verificación de tipo
print(pizza_toppings[1])  #acceso al valor
pizza_toppings.append('Champiñones')  #agregar valor
print(person['nombre'])  #acceso al valor
person['nombre'] = 'George'  #cambiar valor
person['color_de_ojos'] = 'azul'  #agregar valor
print(fruta[2])  #acceso al valor

if num1 > 45:
    print("Es mayor")  #condicional (if)
else:
    print("Es menor")  #condicional (else)

if len(string) < 5:
    print("Es una palabra corta")  #comprobación de longitud
elif len(string) > 15:
    print("Es una palabra larga")  #condicional (else if)
else:
    print("Justo")  #condicional (else)

for x in range(5):  #bucle for
    print(x)

for x in range(2, 5):  #bucle for (inicio, fin)
    print(x)

for x in range(2, 10, 3):  #bucle for (inicio, fin, incremento)
    print(x)

x = 0
while x < 5:  #bucle while (inicio, fin)
    print(x)
    x += 1

pizza_toppings.pop()  #eliminar valor
pizza_toppings.pop(1)  #eliminar valor

print(person)
person.pop('color_de_ojos')  #eliminar valor
print(person)

for topping in pizza_toppings:  #bucle for (secuencia)
    if topping == 'Pepperoni':
        continue  #continuar
    print('Después de la primera comprobación')

    if topping == 'Aceitunas':
        break  #romper

def imprimir_hola_diez_veces():  #función
    for num in range(10):
        print('Hola')

imprimir_hola_diez_veces()

def imprimir_hola_x_veces(x):  #función (parámetro)
    for num in range(x):
        print('Hola')

imprimir_hola_x_veces(4)  #función (argumento)

def imprimir_hola_x_o_diez_veces(x=10):  #función (parámetro por defecto)
    for num in range(x):
        print('Hola')

imprimir_hola_x_o_diez_veces()  #función (parámetro por defecto)
imprimir_hola_x_o_diez_veces(4)  #función (argumento)

