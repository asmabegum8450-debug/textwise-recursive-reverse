import pytest
from src.reverse_string import reverse_string_recursive

# Normal cases
def test_reverse_word():
    assert reverse_string_recursive("hello") == "olleh"

def test_reverse_sentence():
    assert reverse_string_recursive("TextWise Solutions") == "snoituloS esiWtxeT"

def test_reverse_symbols():
    assert reverse_string_recursive("a1!b2") == "2b!1a"

# Edge cases
def test_empty_string():
    assert reverse_string_recursive("") == ""

def test_single_character():
    assert reverse_string_recursive("x") == "x"

def test_unicode():
    assert reverse_string_recursive("a😊b") == "b😊a"

def test_non_string():
    with pytest.raises(TypeError):
        reverse_string_recursive(123)
