# jukebox

`jukebox` is a hobby project around three sequences:

<br>

<span style="text-align: center">

![{\Large J_b(x)} = {\LARGE\sum}_{i=0}^{k-1}{\Large b^i \cdot x_i}](https://render.githubusercontent.com/render/math?math=%7B%5CLarge%20J_b(x)%7D%20%3D%20%7B%5CLARGE%5Csum%7D_%7Bi%3D0%7D%5E%7Bk-1%7D%7B%5CLarge%20b%5Ei%20%5Ccdot%20x_i%7D)

<br>

![{\Large K_b(x)} = {\Large b \cdot J_b(x)}](https://render.githubusercontent.com/render/math?math=%7B%5CLarge%20K_b(x)%7D%20%3D%20%7B%5CLarge%20b%20%5Ccdot%20J_b(x)%7D)

<br>

![{\Large B_b(x)} = {\Large b^n \cdot J_b(x)}](https://render.githubusercontent.com/render/math?math=%7B%5CLarge%20B_b(x)%7D%20%3D%20%7B%5CLarge%20b%5En%20%5Ccdot%20J_b(x)%7D)

</span>

<br>

It started with the 2<sup>nd</sup> of these functions and the interesting observation that a repeated application of *K<sub>2</sub>(x)* eventually ends with *16* for what appears to be any *x > 0*. Ends, because *K<sub>2</sub>(16) = 16*.

All calculations return and are performed using a `Natural`, which raises a `TypeError` or `ValueError` when initiated with a non-integral type or negative integer, respectively.

<u>**Installation**</u>

	pip install jukebox

## Use

---

<u>Natural</u>

```py
#	Natural
from jukebox.natural import Natural

x = Natural.of(12345)
digit_sum = sum(x)
```

<u>Transforms</u>

```py
from jukebox.transforms import J, K, B

print(J(1, 2)) # J_2(1) = 1
print(K(1, 2)) # K_2(1) = 2
print(B(1, 2, 2)) # B_2(1, 2) = 4
```

<u>Transformers</u>

```py
from jukebox.transformers import Transformer, JTransformer, KTransformer, BTransformer

generic_transformer = Transformer(2)
j_transformer = JTransformer(2) # J_2(x)
k_transformer = KTransformer(2) # K_2(x)
b_transformer = BTransformer(2, 2) # B_2(x, 2)

print(generic_transformer.J(1, 3)) # J_3(1) = 1
print(generic_transformer.K(1, 3)) # K_3(1) = 3
print(generic_transformer.B(1, 2)) # B_3(1, 2) = 9

print(j_transformer(16)) # J_2(16) = 8
print(k_transformer(16)) # K_2(16) = 16
print(b_transformer(16)) # B_2(16) = 32
```

<u>Sequences</u>

```py
# Enum with an option for each transform
from jukebox.transforms import Transform 
from jukebox.sequences import TransformSequence as tseq, KSequence as kseq

# Transform.J is the default
ks_t = tseq(x_0=1, base=2, transform=Transform.K)
ks = kseq(x_0=1, base=2)

print(k_seq_gen.info())
#	Transform: K
#	Base: 2
#
#	x_0: 1
#	x_mu: 16
#	x_lambda: 16
#
#	mu: 4
#	lambda: 1
#
#	Path: {1, 2, 4, 8}
#	Cycle: {16}

print(k_seq.info()) # Same as above
```
<u>Factories</u>

```py
from jukebox.factories import TrasformSequenceFactory as tseq_factory, KSequenceFactory as kseq_factory

ks_factory_t = tseq_factory(1, Transform.K, fix_x_0 = True, max_mu = 5000)
ks_factory = kseq_factory(1, fix_x_0=True, max_mu=5000)

# Creates a dictionary mapping the bases 0-9 to their K_b(x) unit sequnces,
# or sequences with initial value 1.
#
# max_mu is 5000 because the sequence for K_8 starting with 1, has mu = 3330, 
# lambda = 1100. That's a cycle with an 1100 value period and a total sequence
# length of 4430.

unit_K_sequences_t = {i, ks_factory_t(i) for i in range(10)}
unit_k_sequences = {k ks_factory(i) for i in range(10)}
```

