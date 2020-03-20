from enum import Enum
from jukebox.natural import Natural

__all__ = ['Transform', 'J', 'K', 'B']

def J(value: Natural, base: Natural) -> Natural:
    """The J_b(x) transform

        J_b(x) = sum([b ** i * x[i] for i in range(len(x)))

    Args:
        value: The value to transform.
        base: The base to use in the transformation.

    Returns:
        Natural: The result of the sum

    """
    sum = 0
    n_value = Natural.of(value)
    n_base = Natural.of(base)

    for digit in reversed(n_value):
        sum = (sum * n_base) + digit

    return sum


def K(value: Natural, base: Natural) -> Natural:
    """The K_b(x) transform

        K_b(x) = sum([b ** (i+1) * x[i] for i in range(len(x)))
        K_b(x) = b * J_b(x)

    Args:
        value: The value to transform.
        base: The base to use in th transformation.

    Returns:
        Natural: The result of the sum.

    """
    return base * J(value, base)

def B(value: Natural, base: Natural, power: Natural) -> Natural:
    """The B_b(x) transform

        B_b(x) = sum([b ** (i+power) * x[i] for i in range(len(x)))
        B_b(x) = (b ** power) * J_b(x)

    Args:
        value: The value to transform.
        base: The base to use in the transformation.

    Returns:
        Natural: The result of the sum.

    """
    n_power = Natural.of(power)
    return (base ** n_power) * J(value, base)

class Transform(Enum):
    J = 'J', J
    K = 'K', K
    B = 'B', B
