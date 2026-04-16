"""
Enunciat:
Implementa la funció 'convert_to_integer(string)' que rebi com a paràmetre una
cadena i retorneu un name enter si és possible. En cas contrari, heu de retornar
un missatge indicant que la cadena no pot ser convertida a un name enter o
un missatge d'error inesperat. Per a l'error 'ValueError' heu de retornar "The
string cannot be converted to an integer"; si és qualsevol altra excepció, ha de
mostrar "An unexpected error has occurred:" seguit de l'error.

Paràmetres:
string (str): cadena que voleu convertir a un name enter.

Exemple:
     Entrada:
     convert_to_integer("123")
     convert_to_integer("foo")
     convert_to_integer(["3.14"])
     

     Sortida:
     - En el primer cas el resultat és: 123
     - En el segon cas el resultat és: The string cannot be converted to an integer
     - En el tercer cas el resultat és: An unexpected has occurred: int() argument
     must be a string, a bytes-like object or a number, not 'list'
"""


def convert_to_integer(string: str):
    try:
        return int(string)
    except ValueError:
        return "The string cannot be converted to an integer"
    except Exception as error:
        return f"An unexpected error has occurred: {error}"


# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(convert_to_integer("123"))
print(convert_to_integer(["3.14"]))
print(convert_to_integer("foo"))
