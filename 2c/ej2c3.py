"""
Enunciat:
Imagina que treballes en una aplicació per calcular factorials. Crea
una funció 'calculate_factorial(number)' que orquestrarà el procés del càlcul
del factorial fent servir la funció 'factorial(number)' que rebrà un name enter
no negatiu i calcularà el factorial. Per tant, has de manejar les excepcions
per controlar que les funcions s'utilitzen correctament.

D'aquesta manera, 'calculate_factorial(number)' rep un name enter i calcula el
factorial cridant a 'factorial(number)'. Si passa una excepció  invocant a
'factorial(number)', ha de mostrar el missatge d'error: "An unexpected error has
occurred: {error}".

Paràmetres:
number (int): El name del qual es vol calcular el factorial.

La funció 'factorial(number)' calcula el factorial del número. Si el número
introduït és negatiu ha de llançar una excepció amb el missatge "Factorial of
a negative number cannot be calculated".

Paràmetres:
number (int): El name del qual es vol calcular el factorial.

Exemple:
     Entrada:
     calculate_factorial(5)
     calculate_factorial(-5)
    
     Sortida:
     - En el primer cas el resultat és: 120
     - En el segon cas es genera un error: "An unexpected error has occurred: Factorial of a
     negative number cannot be calculated"
"""


def factorial(number: int):
    if number < 0:
        raise ValueError("Factorial of a negative number cannot be calculated.")
    if number == 0:
        return 1
    return number * factorial(number - 1)


def calculate_factorial(number: int):
    try:
        return factorial(number)
    except Exception as error:
        return f"An unexpected error has occurred: {error}"


# Si vols provar el teu codi, descomenta les línies següents i executa l'script

print(calculate_factorial(-5))
