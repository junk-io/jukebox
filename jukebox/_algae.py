from typing import Any, Sequence, Tuple, Union

import functools

__all__ = []

#       Decorators      #
def return_on_exception(exception, return_value):
    def decorator(method):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except exception:
                return return_value
        return wrapper
    return decorator


#       Sequence        #
def first(n: int, sequence: Sequence[Any]) -> Sequence[Any]: return [] if sequence is None or n < 1 else sequence[0:n]
def last(n: int, sequence: Sequence[Any]) -> Sequence[Any]: return [] if sequence is None or n < 1 else sequence[-n:]


#       Integral        #
def ensure_integral(value: int) -> int:
    if isinstance(value, int):
        return value
    elif hasattr(val, '__index__'):
        return val.__index__()
    else:
        raise TypeError(':[%s]: Input is not an integral type.' % str(value))

def ensure_integral_is_between(value: int, left: int, right: int, right_inclusive: bool = False) -> int:
    n_value = ensure_integral(value)
    n_left = ensure_integral(left)
    n_right = ensure_integral(right)

    is_min_to_max = n_left < n_right

    if right_inclusive:
        n_right += 1 if is_min_to_max else -1

    if (is_min_to_max and (n_value >= n_left) and (n_value < n_right)) or (not is_min_to_max and (n_value <= left) and (n_value > right)):
        return n_value
    else:
        base = ':[%d]: Input is not in the range of [%d, ' % (n_value, n_left)

        if right_inclusive:
            msg = ''.join([base, '%d].' % (n_right + (-1 if is_min_to_max else 1))])
        else:
            msg = ''.join([base, '%d).' % (n_right + (-1 if is_min_to_max else 1))])

        raise ValueError(msg)

def ensure_integral_is_not_zero(value: int):
    n_value = ensure_integral(value)

    if n_value != 0:
        return n_value
    else:
        raise ValueError(':[%d]: Input is zero.')

def ensure_in_natural(value: int, zero_inclusive: bool = True):
    n_value = ensure_integral(value)

    if n_value >= (0 if zero_inclusive else 1):
        return n_value
    else:
        raise ValueError(':[%d]: Input is less than %d.' % (0 if zero_inclusive else 1))


#       Digit       #
class _Digit(int):

    def __new__(cls, digit = 0):
        return int.__new__(cls, ensure_integral_is_between(digit, 0, 9, True))

    def __abs__(self): return self
    def __ceil__(self) : return self
    def __floor__(self) : return self
    def __round__(self) : return self
    def __trunc__(self) : return self

def _digits_of(value: int, reverse: bool = False) -> Tuple[_Digit]:
    n_value = ensure_in_natural(value)
    digits = [] if n_value != 0 else [0]

    while n_value > 0:
        n_value, remainder = divmod(n_value, 10)
        digits.append(_Digit(remainder))

    if reverse:
        digits.reverse()

    return tuple(digits)
