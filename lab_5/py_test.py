import pytest
from unittest.mock import patch
from main import *

generate = {
    "cpp": "11001101011001111100011011000001000110110100110010000000001000011111100001011011011000001001011001011110011000010000110101110101",
    "java": "00101010010001110111101001101000000000010011010000101011001000010011101011001101111001011011011101100001011100000001110100011101"
}

c_results = {
    "frequency_test": 0.37675911781158206,
    "same_bits_test": 0.520891578444262,
    "long_sequence_test": 0.7966724963708365
}

java_results = {
    "frequency_test": 0.37675911781158206,
    "same_bits_test": 0.804645310694816,
    "long_sequence_test": 0.7871342702860351
}


def test_frequency_cpp():
    frequency = frequency_test(generate['cpp'])
    pract = c_results['frequency_test']
    assert frequency == pytest.approx(pract)


def test_frequency_java():
    frequency = frequency_test(generate['java'])
    pract = java_results['frequency_test']
    assert frequency == pytest.approx(pract)


def test_exception_frequency():
    with pytest.raises(Exception):
        frequency_test()


def test_frequency():
    frequency = frequency_test('10010100010110101010')
    assert frequency <= 1.0


def test_bits_cpp():
    frequency = same_bits_test(generate['cpp'])
    pract = c_results['same_bits_test']
    assert frequency == pytest.approx(pract)


def test_bits_java():
    frequency = same_bits_test(generate['java'])
    pract = java_results['same_bits_test']
    assert frequency == pytest.approx(pract)


def test_exception_bits():
    with pytest.raises(Exception):
        same_bits_test()


def test_bits():
    frequency = same_bits_test('00101101010010')
    assert frequency > 0


def test_long_cpp():
    frequency = long_sequence_test(generate['cpp'])
    pract = c_results['long_sequence_test']
    assert frequency == pytest.approx(pract)


def test_long_java():
    frequency = long_sequence_test(generate['java'])
    pract = java_results['long_sequence_test']
    assert frequency == pytest.approx(pract)


def test_exception_long():
    with pytest.raises(Exception):
        long_sequence_test()


def test_long():
    frequency = long_sequence_test('10010100101010111110000001')
    assert frequency != 1


@pytest.mark.parametrize("input_str, expected", [
    ("11110000", pytest.approx(gammainc(1.5, 0), rel=1e-2)),
    ("00001111", pytest.approx(gammainc(1.5, 0), rel=1e-2)),
    ("10101010", pytest.approx(gammainc(1.5, 0), rel=1e-2)),
])
def test_long_sequence_test(input_str, expected):
    assert long_sequence_test(input_str) != expected


def test_frequency_test_error_handling():
    with patch('builtins.print') as mock_print:
        result = frequency_test(None)
        assert result is None
        mock_print.assert_called_once_with(
            "Произошла ошибка при чтении 'None': 'NoneType' object is not iterable")
