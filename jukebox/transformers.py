from jukebox.natural import Natural

import transforms

__all__ = ['Transformer', 'JTransformer', 'KTransformer', 'BTransformer']

class Transformer(object):
    """ A wrapper of the transformers with a set base. """

    def __init__(self, base: Natural):
        """ Initializes the based wrapper

        Args:
            base:   The base to use in the transforms.
        """
        self.__base = Natural.of(base)

    def J(self, value: Natural) -> Natural: return transforms.J(value, self.__base)

    def K(self, value: Natural) -> Natural: return transforms.K(value, self.__base)

    def B(self, value: Natural, power: Natural) -> Natural: return transforms.B(value, self.__base, power)

class JTransformer(object):
    """ A wrapper of the J_b(x) transformer with a set base. """

    def __init__(self, base: Natural):
        """ Initializes the based wrapper

        Args:
            base:   The base to use in the transforms.
        """
        self.__base = Natural.of(base)

    @property
    def base(self) -> Natural:
        """ The base for this transformer. """
        return self.__base

    def rebase(base: Natural):
        """ Changes the base for this transformer. """
        self.__base = Natural.of(base)

    def __call__(self, value: Natural) -> Natural: return transforms.J(value, self.__base)

class KTransformer(object):
    """ A wrapper of the J_b(x) transformer with a set base. """

    def __init__(self, base: Natural):
        """ Initializes the based wrapper

        Args:
            base:   The base to use in the transforms.
        """
        self.__base = Natural.of(base)

    @property
    def base(self) -> Natural:
        """ The base for this transformer. """
        return self.__base

    def rebase(base: Natural):
        """ Changes the base for this transformer. """
        self.__base = Natural.of(base)

    def __call__(self, value: Natural) -> Natural: return transforms.K(value, self.__base)

class BasedBTransformer(object):
    """ A wrapper of the J_b(x) transformer with a set base. """

    def __init__(self, base: Natural, power: Natural = 1):
        """ Initializes the based wrapper

        Args:
            base:   The base to use in the transforms.
            power: The optional default power to use in the transforms.
        """
        self.__base = Natural.of(base)
        self.__power = Natural.of(power)

    @property
    def base(self) -> Natural:
        """ The base for this transformer. """
        return self.__base

    @property
    def power(self) -> Natural:
        """The power for this transformer."""
        return self.__power

    def rebase(base: Natural):
        """ Changes the base for this transformer. """
        self.__base = Natural.of(base)

    def __call__(self, value: Natural, power: int = -1) -> Natural: return transforms.B(value, base (self.__power if power is None or power < 0 else power))
