from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,most_likely


def test_version():
    assert __version__ == '0.1.0'


def test_encryption():
    """
    Do encryption and test the result
    """
    expected="Ymnx nx 956 u~ymts htzwxj"
    actual=encrypt("This is 401 python course",5)
    assert expected==actual


def test_decryption():
    """
    Do decryption and test the result
    """
    expected="This is python course"
    actual=decrypt('Ymnx nx u~ymts htzwxj',5)
    assert expected==actual
    

def test_possible_sentence_1():
    expected="['Eat the bird bdqe mohammed']"
    actual=str(most_likely('Gcv"vjg"dktf"dfsg"oqjcoogf'))
    assert expected==actual

def test_possible_sentence_2():
    expected="invalid input"
    actual=str(most_likely(''))
    assert expected==actual
    

def test_fruit_for_Samer():
    """
    Do encryption and test the result
    """
    expected="bqqmft boe cbobobt"
    actual=encrypt("apples and bananas",1)
    assert expected==actual
