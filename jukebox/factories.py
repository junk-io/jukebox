from jukebox.natural import Natural
from jukebox.sequences import DEFAULT_MAX_MU, TransformSequence, JSequence, KSequence, BSequence
from jukebox.transforms import Transform
from typing import Callable

class TransformSequenceFactory(object):
    """A factory that makes it convenient to generate a `TransformSequence`.

    It must be fixed with either an initial value or base. It can also be fixed
    with transform.

    The factory is callable taking in non-fixed values. The transform can be
    overwritten in the call
    """

    def __init__(self, x_0_base_constant: Natural, transform_constant: Transform = None, fix_x_0: bool = False, max_mu: Natural = DEFAULT_MAX_MU):
        """Initializes the factory.

        Arguments:
            x_0_base_constant: Initial value or base to fix.

            transform_constant: Optional transform to fix.

            fix_x_0: Optional flag. If True `x_0_base_constant` is fixed as the
                initial value, it is fixed as the base. The default is False.

            max_mu: Maximum length of the sequence if a cycle isn't reached. The
                default is 500.

        """
        self._x_0_base = Natural.of(x_0_base_constant)

        if not (transform_constant is None or isinstance(transform_constant, Transform)):
            raise TypeError(':[%s]: Input is not a `Transform` option. Options are `Transform.J`, `Transform.K`, or `Transform.B`.' % str(transform))

        self.__transform = transform_constant

        if not (fix_x_0 is None or isinstance(fix_x_0, bool)):
            raise TypeError(':[%s]: Factory cannot determine whether or not to fix the initial value or base.')

        self._fix_iv = False if fix_x_0 is None else fix_x_0
        self._max_mu = Natural.of(max_mu)

    @property
    def base(self):
        """The base if it is fixed, None otherwise."""
        return self._x_0_base if not self._fix_iv else None

    @property
    def x_0(self):
        """The initial value if it is fixed, None otherwise."""
        return self._x_0_base if self._fix_iv else None

    @property
    def transform(self) -> Callable:
        """The transform if it is fixed, None otherwise."""
        return self.__transform.value[1] if not self.__transform is None else None

    @property
    def transform_name(self):
        """The name of the transform if it is fixed. Empty string otherwise."""
        return self.__transform.value[0] if not self.__transform is None else ''

    def __call__(self, x_0_base: Natural, power: Natural = None, transform: Transform = None, max_mu: Natural = None):
        if self._fix_iv:
            n_iv = self._x_0_base
            n_base = Natural.of(x_0_base)
        else:
            n_iv = Natural.of(x_0_base)
            n_base = self._x_0_base

        if self.__transform is None and (transform is None or not isinstance(transform, Transform)):
            raise TypeError(':[%s]: Factory does not have a valid `Transform` option. Options are `Transform.J`, `Transform.K`, or `Transform.B`.' % transform)
        elif not self.__transform is None and not transform is None:
            if isinstance(transform, Transform):
                print('WARNING: Input transform is: %s. Fixed transform is: %s. Factory will ignore the fixed and use the input transform.' % (transform[0], self.__transform.value[0]))
            else:
                print('WARNING: Input transform is not a valid `Transform` option. Factory will ignore the input value and use the fixed transform')

        n_transform = transform if isinstance(transform, Transform) else self.__transform.value[1]

        if not max_mu is None:
            try:
                n_max_mu = Natural.of(max_mu)
            except (TypeError, ValueError):
                n_max_mu = self._max_mu
        else:
            n_max_mu = self._max_mu

        return TransformSequence(n_iv, n_base, power, n_transform, n_max_mu)

class JSequenceFactory(TransformSequenceFactory):
    """The J_b(x) specific sequence factory."""

    def __init__(self, x_0_base_constant, fix_x_0: bool = False, max_mu: Natural = DEFAULT_MAX_MU):
        super().__init__(x_0_base_constant, Transform.J, fix_x_0, max_mu)

    def __call__(self, x_0_base: Natural, max_mu: Natural = None):
        if self._fix_iv:
            n_iv = self._x_0_base
            n_base = Natural.of(x_0_base)
        else:
            n_iv = Natural.of(x_0_base)
            n_base = self._x_0_base

        if not max_mu is None:
            try:
                n_max_mu = Natural.of(max_mu)
            except (TypeError, ValueError):
                n_max_mu = self._max_mu
        else:
            n_max_mu = self._max_mu

        return JSequence(n_iv, n_base, n_max_mu)

class KSequenceFactory(TransformSequenceFactory):
    """The K_b(x) specific sequence factory."""

    def __init__(self, x_0_base_constant, fix_x_0: bool = False, max_mu: Natural = None):
        super().__init__(x_0_base_constant, Transform.K, fix_x_0, max_mu)

    def __call__(self, x_0_base: Natural, max_mu: Natural = None):
        if self._fix_iv:
            n_iv = self._x_0_base
            n_base = Natural.of(x_0_base)
        else:
            n_iv = Natural.of(x_0_base)
            n_base = self._x_0_base

        if not max_mu is None:
            try:
                n_max_mu = Natural.of(max_mu)
            except (TypeError, ValueError):
                n_max_mu = self._max_mu
        else:
            n_max_mu = self._max_mu

        return KSequence(n_iv, n_base, n_max_mu)

class BSequenceFactory(TransformSequenceFactory):
    """The B_b(x) specific sequence factory."""

    def __init__(self, x_0_base_constant, power: Natural = None, fix_x_0: bool = False, max_mu: Natural = DEFAULT_MAX_MU):
        super().__init__(x_0_base_constant, Transform.B, fix_x_0, max_mu)
        self.__power = Natural.of(power) if not power is None else None

    def __call__(self, x_0_base: Natural, power: Natural = None, max_mu: Natural = None):
        if self._fix_iv:
            n_iv = self._x_0_base
            n_base = Natural.of(x_0_base)
        else:
            n_iv = Natural.of(x_0_base)
            n_base = self._x_0_base

        if not max_mu is None:
            try:
                n_max_mu = Natural.of(max_mu)
            except (TypeError, ValueError):
                n_max_mu = self._max_mu
        else:
            n_max_mu = self._max_mu

        if not self.__power is None:
            if power is None:
                return BSequence(n_iv, n_base, self.__power, n_max_mu)
            else:
                return BSequence(n_iv, n_base, power, n_max_mu)
        else:
            return BSequence(n_iv, n_base, power, n_max_mu)
