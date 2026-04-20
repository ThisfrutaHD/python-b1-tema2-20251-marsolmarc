from typing import List

"""
Enunciat:
Corregeix la funció 'division_list' que fa una divisió d'una llista
de nombre enters dividit per a un nombre escalar.

Per corregir els errors es poden canviar els valors de la llista
'list_numbers' i el valor del número escalar 'scalar_number'.

A la funció 'division_list' s'ha de verificar que el contingut de
la llista sigui de tipus 'int' o 'float', en cas contrari, mostra una
excepció TypeError(f"Value {number_in_list} is not numeric.").

Paràmetres:
     list_numbers (list): Llista de números.
     number (int): Número sencer.

Exemples:
     Entrada:
         list_numbers = [1.5, 2.5, 9.2, 0, 22]
         scalar_number = 4.0

     Sortida:
         [0.375, 0.625, 2.3, 0.0, 5.5]

"""


def division_list(list_numbers: List, scalar_number: float) -> List[float]:
    result = []
    for number_in_list in list_numbers:
        if not isinstance(number_in_list, (int, float)):
            raise TypeError(f"Value {number_in_list} is not numeric.")
        result.append(number_in_list / scalar_number)
    return result


list_numbers = [1.5, 2.5, 9.2, 0.0, 22.0]
scalar_number = 4.0

# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(division_list(list_numbers, scalar_number))
