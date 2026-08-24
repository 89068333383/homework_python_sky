import io
import sys
from Lesson_2_4 import fizz_buzz


def test_fizz_prints_fizz():
    captured = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = captured
        fizz_buzz(3)
        output = captured.getvalue()
        assert "Fizz" in output
    finally:
        sys.stdout = old_stdout


def test_buzz_prints_buzz():
    captured = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = captured
        fizz_buzz(5)
        output = captured.getvalue()
        assert "Buzz" in output
    finally:
        sys.stdout = old_stdout


def test_fizzbuzz_prints_fizzbuzz():
    captured = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = captured
        fizz_buzz(15)
        output = captured.getvalue()
        assert "FizzBuzz" in output
    finally:
        sys.stdout = old_stdout
