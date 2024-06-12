import unittest
import pytest
from unittest.mock import patch

from MainFolder.test import print_hello, concatenate_strings, calculate_salary


class TestHelloWorld(unittest.TestCase):
    def test_print_hello_world(self):
        with patch("random.choice") as mock_choice:
            mock_choice.return_value = "B"
            expected_output = "hello worldB"
            actual_output = print_hello()
            self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()


def test_concatenate_strings_success():
    assert concatenate_strings("Hello ", "World!") == "Hello World!"


@pytest.mark.parametrize(
    ("total_compensation", "result"),
    [
        (100, 87),
        (0, 0),
        (99, 86.13),
    ],
)
def test_calculate_salary(total_compensation, result):
    assert calculate_salary(total_compensation) == result


# import pytest
# from matplotlib.testing.decorators import image_comparison
# from test import create_plots
#
#
# @image_comparison(baseline_images=['result_images/testing/line_plots.png'], remove_text=True)
# def test_line_plots():
#     return create_plots()
#
#
# if __name__ == '__main__':
#     pytest.main(['testing.py'])
