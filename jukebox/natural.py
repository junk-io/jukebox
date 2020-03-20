from jukebox._algae import _Digit, _digits_of, ensure_in_natural, ensure_integral, ensure_integral_is_between, return_on_exception
from typing import Callable, Sequence

__all__ = ['Natural']

class Natural(int):
    """ A natural number.

    This class represents a read-only, digit-indexable integer N, such that N >= 0, and
    N[i] is the digit in the 10^i place of N.

    """
    def __new__(cls, value: int = 0):
        return int.__new__(cls, ensure_in_natural(value))

    def __init__(self, value: int = 0):
        """Initializes a new `Natural` number.

        Args:
            value: An optional integer.

        Raises:
            TypeError: If  `value` is not an integral type.
            ValueError: If `value` is negative.

        """

        self.__digits = _digits_of(value)
        self.__digit_sum = sum(self.__digits)
        self.__length = len(self.__digits)

    @staticmethod
    def of(value: int):
        """ Creates a natural number.

        Args:
            value: The value of the integer.

        Returns:
            Natural: This integer as a `Natural`.
        """
        return value if isinstance(value, Natural) else Natural(value)

    @property
    def digital_root(self):
        """The digital root of this iteger."""
        return self % 9

    @property
    def digit_sum(self): return Natural(self.__digit_sum)

    @property
    def digits(self) -> Sequence:
        """The digits of this integer."""
        return self.__digits

    def is_fixed_point_of(self, f: Callable[[int], int]) -> bool:
        """Whether or not this natural number is a fixed point of the function `f`.

        A fixed point of a function f is defined as an input, x, where f(x) = x.

        Args:
            f: A function that maps this integer to another.

        Returns:
            bool: True if f(self) = self, else False

        """
        return f(self) == self

    @return_on_exception(TypeError, NotImplemented)
    def __add__(self, value: int): return Natural(super().__add__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __sub__(self, value: int): return Natural(super().__sub__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __mul__(self, value: int): return Natural(super().__mul__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __mod__(self, value: int): return Natural(super().__mod__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __floordiv__(self, value: int): return Natural(super().__floordiv__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __divmod__(self, value: int):
        div, mod = super().__divmod__(ensure_integral(value))
        return Natural(div), Natural(mod)

    @return_on_exception(TypeError, NotImplemented)
    def __lshift__(self, value: int): return Natural(super().__lshift__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __rshift__(self, value: int): return Natural(super().__rshift__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __and__(self, value: int): return Natural(super().__and__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __xor__(self, value: int): return Natural(super().__xor__(ensure_integral(value)))

    @return_on_exception(TypeError, NotImplemented)
    def __or__(self, value: int): return Natural(super().__or__(ensure_integral(value)))

    def __radd__(self, value: int): return self.__add__(value)
    def __rsub__(self, value: int): return self.__sub__(value)
    def __rmul__(self, value: int): return self.__mul__(value)
    def __rmod__(self, value: int): return self.__mod__(value)
    def __rfloordiv(self, value: int): return self.__floordiv__(value)
    def __rtruediv(self, value: int): return self.__truediv__(value)
    def __rdivmod(self, value: int): return self.__divmod__(value)
    def __rlshift(self, value: int): return self.__lshift__(value)
    def __rrshift(self, value: int): return self.__rshift__(value)
    def __rand__(self, value: int): return self.__and__(value)
    def __rxor__(self, value: int): return self.__xor__(value)
    def __ror__(self, value: int): return self.__or__(value)

    def __abs__(self): return Natural(self)
    def __pos__(self): return Natural(self)
    def __round__(self): return Natural(self)
    def __trunc__(self): return Natural(self)
    def __floor__(self): return Natural(self)
    def __ceil__(self): return Natural(self)

    @return_on_exception(ValueError, False)
    @return_on_exception(TypeError, False)
    def __contains__(self, value: int): return _Digit(value) in self.__digits

    def __getitem__(self, index: int):
        try:
            key = ensure_integral_is_between(index, -self.__length, self.__length)
            return self.__digits[key]
        except ValueError as error:
            raise IndexError(str(err))

    def __iter__(self):
        for digit in self.__digits:
            yield digit

    def __len__(self): return self.__length

    def __reversed__(self):
        for i in range(self.__length):
            yield self.__digits[-(i + 1)]
