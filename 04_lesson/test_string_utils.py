import pytest
from string_utils import StringUtils


# =============================================================================
# TEST capitalize
# =============================================================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello"),
        ("123","123"),
        ("hello friend","Hello friend"),
    ],
)
def test_capitalize_positive(input_text, expected_output):
    str01 = StringUtils()
    assert str01.capitalize(input_text) == expected_output

@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" ", " "),
        ("",""),
    ],
)
def test_capitalize_negative(input_text, expected_output):
    str01 = StringUtils()
    assert str01.capitalize(input_text) == expected_output


# =============================================================================
# TEST trim
# =============================================================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" hello", "hello"),  # Пробел в начале
        ("  ",""),            # Строка только из пробелов
    ],
)
def test_trim_positive(input_text, expected_output):
    str01 = StringUtils()
    assert str01.trim(input_text) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("sky pro", "sky pro"),  # Строка с пробелам в середине
    ],
)
def test_trim_negative(input_text, expected_output):
    str01 = StringUtils()
    assert str01.trim(input_text) == expected_output


# =============================================================================
# TEST contains
# =============================================================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_output, expected",
    [
        ("SkyPro", "S", True),      # Символ есть
    ],
)
def test_contains_positive(input_text, expected_output, expected):
    str01 = StringUtils()
    assert str01.contains(input_text, expected_output) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_output, expected",
    [
        ("SkyPro", "U", False) # Символ отсутствует в строке
    ],
)
def test_contains_negative(input_text, expected_output, expected):
    str01 = StringUtils()
    assert str01.contains(input_text, expected_output) == expected


# =============================================================================
# TEST delete_symbol
# =============================================================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_output, expected",
    [
        ("SkyPro", "Sky", "Pro")    # Удаление Sky
    ],
)
def test_delete_symbol_positive(input_text, expected_output, expected):
    str01 = StringUtils()
    assert str01.delete_symbol(input_text, expected_output) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_output, expected",
    [
        ("SkyPro", "w", "SkyPro")    # Удаление не существующего символа
    ],
)
def test_delete_symbol_negative(input_text, expected_output, expected):
    str01 = StringUtils()
    assert str01.delete_symbol(input_text, expected_output) == expected

