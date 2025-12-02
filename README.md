# mrandom
> This package provides a random number generator.
> It is based on the [Mersenne Twister](http://en.wikipedia.org/wiki/Mersenne_Twister) algorithm.
> It includes both 32 and 64 bit versions of the algorithm.
> The generator has large period of 2^19937-1 
> mrandom is a Python package that provides a high-quality random number generator along with utility functions like sampling, shuffling, rolling dice, flipping coins, and drawing cards.
> It is built on top of the Mersenne Twister (MT19937) algorithm, which is one of the most reliable and widely used pseudorandom number generators.
> The Mersenne Twister is a pseudorandom number generator developed by Makoto Matsumoto and Takuji Nishimura in 1997. 
> t is known for its exceptional speed and statistical randomness and is used in many languages and libraries, including Python’s built-in random module.

Why It’s Used?
	•	Very long period:
        MT19937 has a period of
        2^{19937} - 1
        meaning its random sequence takes an extremely long time before repeating.
	•	Fast and efficient:
        Capable of generating millions of random numbers per second.
	•	Statistically strong randomness:
        The numbers are uniformly distributed across 623 dimensions, making it ideal for simulations, analytics, and sampling.
	•	Reproducibility:
        Mersenne Twister is deterministic — given the same seed, it produces the same sequence. This is extremely useful for testing and debugging.

**Features**
* Can generate random numbers
* Can return a choice from a list
* Can shuffle a list
* Can flip a coin
* Can roll a die
* Can shuffle a deck

* Deterministic output using seeds
* Consistent API similar to Python’s built-in random module
* Utility functions for common probability tasks
* Extensible design


**Installing the package**

``` bash
pip install mrandom
```

**Importing the module**

``` python
>>> import mrandom

# 1 = 32 bit, 2 = 64 bit algorithm
>>> random = mrandom.RandomGenerator(s)
```

# Examples

**Return a random number between 0 and 1**
``` python
>>> print(random.rand())
0.9888888888888889
```

**Return a random number between a and b (inclusive)**
``` python
>>> print(random.randint(a, b))
1
```

**Return a random number between a and b (exclusive)**
``` python
>>> print(random.randrange(a, b))
12
```

**Return k random numbers between a and b (inclusive)**
``` python
>>> print(random.sample(a, b, k))
[1, 2, 3, 4, 5]
```

**Return a random number from a list l**
``` python
>>> print(random.choice(l))
21
```

**Return shuffled list l**
``` python
>>> print(random.shuffle(l))
[1, 3, 5, 4, 2]
```

**Return sample of flipping k coins n times**
``` python
>>> print(random.flip_coin(n, k))
[1, 0, 0, 1, 0]
```

**Return sample of rolling k dices n times**
``` python
>>> print(random.roll_dice(n, k))
[[1, 4], [1, 1]]
```

**Return sample of picking a card from a deck of 52 cards n times**
``` python
>>> print(random.shuffle_deck(n))
["Ace of Spades", "Ace of Hearts", "Ace of Clubs", "Ace of Diamonds", "Ace of Clubs"]
```
---

**Classes**
class mrandom.RandomGenerator
RandomGenerator is a simple pseudo-random number generator based on the Mersenne Twister algorithm.
It supports generating random numbers, picking items from lists, shuffling sequences, flipping coins, rolling dice, and drawing cards from a deck.

Parameters:
seed (int, optional):
The starting value for the generator.
Use this when you want reproducible random results.
If not provided, a default or time-based seed is used.
version (int, optional):
Selects the algorithm version.
Use 1 for the 32-bit version, or 2 for the 64-bit version.

**Methods**
| Methods | Description |
| --- | --- |
| `rand()` | Return a random number between 0 and 1 |
| `randint(a, b)` | Return a random number between a and b (inclusive) |
| `randrange(a, b)` | Return a random number between a and b (exclusive) |
| `sample(a, b, k)` | Return k random numbers between a and b (inclusive) |
| `choice(l)` | Return a random number from a list l |
| `shuffle(l)` | Return shuffled list l |
| `flip_coin(n, k)` | Return sample of flipping k coins n times |
| `roll_dice(n, k)` | Return sample of rolling k dices n times |
| `shuffle_deck(n)` | Return sample of picking a card from a deck of 52 cards n times |


Real-World Use Cases of Mersenne Twiste

1. Scientific Simulations:
Many simulation environments rely on large sets of random numbers:
	•	Physics simulations
	•	Molecular dynamics
	•	Weather and climate modeling
	•	Population modeling in biology

2. Machine Learning & Data Science:
    Randomness is used for:
	•	Data shuffling
	•	Random train-test splits
	•	Weight initialization in neural networks
	•	Bootstrapping
	•	Bagging / Random Forest sampling

3. Gaming & Game Development

    Games heavily rely on randomization:
	•	Loot drops
	•	Critical hits
	•	Card shuffling
	•	Enemy behavior randomness
	•	Procedural terrain generation

4. Graphics & Visual Effects

    Randomness is used for:
	•	Procedural texture generation
	•	Particle effects (smoke, fire, water)
	•	Noise generation
	•	Animation randomness

5. Statistical sampling (NumPy, MATLAB, R)  
6. Operations research & optimization  
7. Graphics and VFX procedural randomness  
8. Robotics & embedded system simulations  
9.  Educational tools for probability and algorithms  
10. Software testing & fuzzing with reproducible randomnesscd 
