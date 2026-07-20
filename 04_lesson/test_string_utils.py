import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# --- capitalize ---
# ---test_capitalize_positive -первая буква строки заглавная, а остальные как есть ---
# ---test_capitalize_negative -граничные значения, пусто, пробел, строка с цифры ---


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("123abc", "123abc"),
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# --- trim ---
# ---test_trim_positive -убрать лишние пробелы ---
# ---test_trim_negative -пустая строка, строка из спецсимволов---


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("no_spaces", "no_spaces"),
        (" single", "single"),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("no spaces at end ", "no spaces at end "),
        ("\t\n", "\t\n"),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# --- contains ---
# ---test_contains_positive -верно находит символ в строке и возвращает True---
# ---test_contains_negative -символа нет, строка /символ пусто возвращает False---


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "k", True),
        ("SkyPro", "o", True),
    ],
)
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "U", False),
        ("", "a", False),
    ],
)
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# --- delete_symbol ---
# ---test_delete_symbol_positive - проверка удаления символа---
# ---test_delete_symbol_negative - пудалять нечего - строка неизменна---


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("aaaaaa", "a", ""),
        ("abracadabra", "a", "brcdbr"),
    ],
)
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "X", "SkyPro"),
        ("", "a", ""),
        ("test", "", "test"),
    ],
)
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
