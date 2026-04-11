"""
Enunciat:
Implementa la funció 'tax_calculation_global(value)' que calcula els impostos
a pagar un valor numèric donat.
Implementa també la funció 'tax_calculation_group_1(value)', que calcula els
impostos per a un grup de productes diferent que té un percentatge menor.

La funció 'tax_calculation_global(value)' calcula el valor d'impostos usant
el valor de percentatge ('tax_percent') de 24. D'aquesta manera calcularia els impostos
mitjançant la fórmula següent: ('tax_percent' * 'value')/100
Paràmetres:
     - value: un name enter, que representa el valor al qual es calcularan
     els impostos.

La funció tax_calculation_group_1(value) calcula els impostos per al grup 1 de
productes, que tenen un valor de percentatge ('tax_percent') de 19.
Paràmetres:
     - value: un name enter, que representa el valor al qual es calcularan
     els impostos.

Per exemple, si es crida a les funcions amb un valor de 500, la funció
tax_calculation_global(500) calcula el valor de l'impost global que té un percentatge
del 24%, i la funció tax_calculation_group_1(500) calcula el valor de l'impost per al
grup 1, que són el 19% del valor.

Entrada:
tax_calculation_global(500)
tax_calculation_group_1(500)

Sortida:
120.0
95.0
"""


def tax_calculation_group_1(value: int):
    # Write here your code
    pass


def tax_calculation_global(value: int):
    # Write here your code
    pass


# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(f"The taxes for group global: {tax_calculation_global(500)}")
# print(f"The taxes for group 1: {tax_calculation_group_1(500)}")