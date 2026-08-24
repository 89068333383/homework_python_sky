import pytest
from string_processor import StringProcessor


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello."),
        ("Hello", "Hello."),
        ("hello world", "Hello world."),
    ],
)
def test_process_positive(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")],
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output
