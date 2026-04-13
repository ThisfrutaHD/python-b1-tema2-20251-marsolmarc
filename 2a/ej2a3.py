"""
Enunciat:
Cal crear dues funcions que treballin amb una llista d'estudiants
i afegeixin un nou estudiant a la llista. La diferència és que la funció
'add_student_by_value(list_students, new_student)' ha d'afegir al nou
estudiant fent servir pas per valor i la funció
'add_student_by_reference(list_students, new_student)' fent servir pas per
referència. Ambdues funcions seran orquestrades des de la funció
'main(list_students, new_student)' que ja està definida.

La funció 'add_student_by_value(list_students, new_student)' ha de copiar
la llista d'estudiants per no afectar la llista original i afegir al nou
estudiant. Aquesta és la solució de pas per valor.
Paràmetres:
     - list_students (List): Llista d'estudiants original.
     - new_student (str): Nom del nou estudiant.

La funció 'add_student_by_reference(list_students, new_student)' ha d'afegir
al nou estudiant usant pas per referència.
Paràmetres:
     - list_students (List): Llista d'estudiants original.
     - new_student (str): Nom del nou estudiant.

La funció 'main(list_students, new_student)' és la que trucarà a les 2
funcions prèviament definides per comprovar que list_students
canvieu d'acord amb la funció trucada.
Paràmetres:
     - list_students (List): Llista d'estudiants original.
     - new_student (str): Nom del nou estudiant.

Exemple:
     Entrada:
     list_students = ['Alice', 'Bob', 'Juan']
     new_student_by_value = 'Maria'
     new_student_by_reference = 'Sofia'

     main(list_students, new_student_by_value, new_student_by_reference)

     Sortida:
     Original student list ['Alice', 'Bob', 'Juan']
     Student list by value ['Alice', 'Bob', 'Juan', 'Maria']
     Student list by reference ['Alice', 'Bob', 'Juan', 'Sofia']
     Original student list ['Alice', 'Bob', 'Juan', 'Sofia']

"""


def add_student_by_value(list_students, new_student):
     new_list_by_value = []
     for i in list_students:
        new_list_by_value.append(i)
     new_list_by_value.append(new_student)
     return new_list_by_value



def add_student_by_reference(list_students, new_student):
    list_students.append(new_student)
    return list_students


def main(list_students, new_student_by_value, new_student_by_reference):
    print(f"Original student list {list_students}")
    print(f"Student list by value {add_student_by_value(list_students, new_student_by_value)}")
    print(f"Student list by reference {add_student_by_reference(list_students, new_student_by_reference)}")
    print(f"Original student list {list_students}")
    


# Si vols provar el teu codi, descomenta les línies següents i executa l'script
list_students = ["Alice", "Bob", "Juan"]
new_student_by_value = "Maria"
new_student_by_reference = "Sofia"

main(list_students, new_student_by_value, new_student_by_reference)