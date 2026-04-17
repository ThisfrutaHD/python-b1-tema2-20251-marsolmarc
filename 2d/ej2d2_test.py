from ej2d2 import calculate_max_and_min
from flake8.api import legacy as flake8

def test_calculate_max_and_min(capfd):
    list_numbers = [10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55]
    result = calculate_max_and_min(list_numbers)
    assert result == (-55.55, 200), "calculate_max_and_min does not return the correct value for input [10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55]. It should be (-55.55, 200)"

    salida_stdout, salida_stderr = capfd.readouterr()
    assert salida_stdout.strip() != "", "calculate_max_and_min does not print anything"
    assert salida_stderr.strip() == "", "calculate_max_and_min prints an error message"


def test_pep8_conformity():
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files(["ej2d2.py"])
    
    assert report.get_statistics("") == [], (
        "Your code does not comply with flake8. Please review your code"
    )

