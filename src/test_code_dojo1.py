from src.code_dojo1 import *

def test_ano_bissexto():
    assert ano_bissexto(1600) == True
    assert ano_bissexto(1732) == True
    assert ano_bissexto(1888) == True
    assert ano_bissexto(1944) == True
    assert ano_bissexto(2008) == True

    assert ano_bissexto(1742) == False
    assert ano_bissexto(2011) == False
    assert ano_bissexto(1951) == False
    assert ano_bissexto(1889) == False

def test_fatores_primos():
    assert fatores_primos(5) == [5]
    assert fatores_primos(100) == [2, 2, 5, 5]
    assert fatores_primos(198) == [2, 3, 3, 11]
    assert fatores_primos(276) == [2, 2, 3, 23]

    assert fatores_primos(-1) == []
    assert fatores_primos(0) == []
    assert fatores_primos(False) == []
    assert fatores_primos('2') == []


