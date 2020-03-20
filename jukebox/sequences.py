from jukebox._algae import ensure_integral_is_between, first, last
from jukebox.natural import Natural
from jukebox.transforms import Transform
from typing import Callable, Final, Sequence, Tuple, Union

import jukebox.transforms

__all__ = ['Transform', 'TransformSequence', 'TransformSequenceFactory', 'JSequence', 'JSequenceFactory',' KSequence', 'KSequenceFactory', 'BSequence, BSequenceFactory']

DEFAULT_MAX_MU: Final[Natural] = Natural.of(500)

class TransformSequence(object):
    """Generic sequence starting with an initial value, base, and optional power.

    The sequence generated is a result of repeated application of a `jukebox`
    transform until a cycle is reached, at which point it stops before the cycle
    repeats. If a cycle is never reached, it stops after the sequence has reached
    a given maximum length.
    """

    def __init__(self, x_0: Natural, base: Natural, power: Natural = 1, transform: Transform = Transform.J, max_mu: Natural = DEFAULT_MAX_MU):
        """ Initializes a transform sequence starting with the `x_0` and `base` with optional `power`.

        The sequence is a result of subsequent applications of the J, K, B transforms,
        until a cycle or the maximum mu is reached.

        Raises:
            TypeError: If `transform` is not a `Transform` option.
        """

        self.__base = Natural.of(base)
        self.__x_0 = Natural.of(x_0)
        self.__x_mu = -1
        self.__x_lambda = -1
        self.__lambda = 0
        self.__mu = 0
        self.__track = tuple()

        if not isinstance(transform, Transform):
            raise TypeError(':[%s]: Input is not a valid `Transform` option. Options are `Transform.J`, `Transform.K`, or `Transform.B`.' % str(transform))

        self.__transform = transform
        self.__power = Natural.of(power) if transform == Transform.B else (0 if transform == Transform.J else 1)
        self.__max_mu = Natural.of(max_mu)

        self.__build()

    @property
    def base(self) -> Natural:
        """The base of this transform."""
        return self.__base

    @property
    def cycle(self) -> Sequence[Natural]:
        """The cycle of the sequence, if one exists."""
        return last(self.__lambda, self.__track)

    @property
    def full_sequence(self) -> Tuple[Natural]:
        """The full sequence."""
        return self.__track

    @property
    def is_cyclic(self) -> bool:
        """Whether or not this sequence has ended in a cycle. True if it has, False otherwise."""
        return self.__x_mu != -1

    @property
    def is_persistent(self) -> bool:
        """Whether or not this sequence has ended in a cycle. False if it has. True otherwise."""
        return self.__x_mu == -1

    @property
    def path(self) -> Sequence[Natural]:
        """The subset of values not in the cycle."""
        return first(self.__mu, self.__track)

    @property
    def lambda_(self) -> Natural :
        """The length of the cycle if one exists."""
        return self.__lambda

    @property
    def mu(self) -> Natural:
        """The length of the path."""
        return self.__mu

    @property
    def power(self) -> Natural:
        """The power of the transform, if it is a `B_b(x)` transform."""
        return self.__power

    @property
    def transform(self) -> Callable:
        """The transform of this sequence."""
        return self.__transform.value[1]

    @property
    def transform_name(self) -> str:
        """The transform name of this sequence."""
        return self.__transform.value[0]

    @property
    def x_0(self) -> Natural:
        """The initial value of the sequence."""
        return self.__x_0

    @property
    def x_lambda(self) -> int:
        """The last value in the cycle if one exists, -1 otherwise."""
        return self.__x_lambda

    @property
    def x_mu(self) -> int:
        """The first value of the cycle if one exists, -1 otherwise."""
        return self.__x_mu

    def info(self, include_path: bool = True, include_cycle: bool = True) -> str:
        """String with all the information about this sequence.

        Info is returned as a sequence of the form:

        Transform: [transform name]

        Base: [base]

        x_0: [initial value]
        x_mu: [first value of cycle]
        x_lambda: [last value of cycle]

        mu: [length of path]
        lambda: [length of cycle]

        Path: [path]
        Cycle: [cycle]

        Returns:
            str: The information about this sequence.
        """
        data = [
            'Transform: %s' % self.__transform.value[0],
            '\nBase: %d' % self.__base,
            '\nx_0: %d' % self.__x_0,
            'x_\u03BC: %s' % (str(self.__x_mu) if self.__x_mu > -1 else '-'),
            'x_\u03BB: %s' % (str(self.__x_lambda) if self.__x_lambda > -1 else '-'),
            '\n\u03BC: %d' % self.__mu,
            '\u03BB: %d\n' % self.__lambda ]

        base = '\n'.join(data)

        if include_path:
            base += '\nPath: {%s}' % ', '.join(map(str, self.path))

        if include_cycle:
            base += '\nCycle: {%s}' % ', '.join(map(str, self.cycle))

        return base

    def __contains__(self, value: Natural): return value in self.__track

    def __getitem__(self, index: int):
        try:
            return self.__track[ensure_integral_is_between(index, -len(self.__track), len(self.__track))]
        except ValueError as err:
            raise IndexError(str(err))

    def __iter__(self):
        for value in self.__track:
            yield value

    def __len__(self): return len(self.__track)

    def __reversed__(self):
        for i in range(len(self.__track)):
            yield self.__track[-(i + 1)]

    def __build(self):
        track = []
        step = self.__x_0
        cycled = False
        f = self.__transform.value[1]

        if f == Transform.B:
            while(not cycled) and (len(track) < self.__max_mu):
                track.append(step)
                step = f(step, self.__base, self.__power)
                cycled = step in track
        else:
            while (not cycled) and (len(track) < self.__max_mu):
                track.append(step)
                step = f(step, self.__base)
                cycled = step in track

        self.__mu = track.index(step) if cycled else len(track)
        self.__lambda = len(track) - self.__mu

        if cycled:
            self.__x_mu = step
            self.__x_lambda = track[-1]

        self.__track = tuple(track)

class JSequence(TransformSequence):
    """The J_b(x) specific sequence."""

    def __init__(self, initival_value: Natural, base: Natural, max_mu: Natural = DEFAULT_MAX_MU):
        super().__init__(x_0, base, transform=Transform.J, max_mu=max_mu)

class KSequence(TransformSequence):
    """The K_b(x) specific sequence."""

    def __init__(self, x_0: Natural, base: Natural, max_mu: Natural = DEFAULT_MAX_MU):
        super().__init__(x_0, base, transform=Transform.K, max_mu=max_mu)

class BSequence(TransformSequence):
    """The B_b(x) specfic sequence."""

    def __init__(self, x_0: Natural, base: Natural, power: Natural, max_mu: Natural = DEFAULT_MAX_MU):
        super().__init__(x_0, base, power, transform=Transform.B, max_mu=max_mu)
