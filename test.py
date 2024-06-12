import random
import string

# import numpy as np
# from matplotlib import pyplot as plt


def print_hello() -> str:
    """
    Приветствие
    """
    return "hello world" + random.choice(string.ascii_uppercase)


def concatenate_strings(a: str, b: str) -> str:
    """
    Сложение строк
    """
    return a + b


def calculate_salary(total_compensation: int) -> float:
    """
    Зарплата мину 13% налогов
    """
    return total_compensation * 0.87


# def create_plots():
#     with plt.style.context('ggplot'):
#         x = np.arange(7)
#
#         fig = plt.figure(figsize=(15, 10))
#
#         lines = [plt.plot(x, -x ** 2),
#                  plt.plot(x, -x ** 3),
#                  plt.plot(x, -2 * x),
#                  plt.plot(x, -2 ** x)]
#
#         plt.show()
#     return fig, lines


if __name__ == "__main__":
    print(print_hello())
