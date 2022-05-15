# mrandom
> This package provides a random number generator.
> It is based on the [Mersenne Twister](http://en.wikipedia.org/wiki/Mersenne_Twister) algorithm.
> It includes both 32 and 64 bit versions of the algorithm.
> The generator has large period of 2^19937-1 




**Features**
* Can generate random numbers
* Can return a choice from a list
* Can shuffle a list
* Can flip a coin
* Can roll a die
* Can shuffle a deck
---

**Installing the package**

``` bash
pip install mrandom
```

**Importing the module**

``` python
import mrandom

# 1 = 32 bit, 2 = 64 bit algorithm
random = mrandom.RandomGenerator(s)
```

# Examples

**Return a random number between 0 and 1**
``` python
print(random.rand())
# output: 0.9888888888888889
```

**Return a random number between a and b (inclusive)**
``` python
print(random.randint(a, b))
# output: 1
```

**Return a random number between a and b (exclusive)**
``` python
print(random.randrange(a, b))
# output: 1
```

**Return k random numbers between a and b (inclusive)**
``` python
print(random.sample(a, b, k))
# output: [1, 2, 3, 4, 5]
```

**Return a random number from a list l**
``` python
print(random.choice(l))
# output: 1
```

**Return shuffled list l**
``` python
print(random.shuffle(l))
# output: [1, 3, 5, 4, 2]
```

**Return sample of flipping k coins n times**
``` python
print(random.flip_coin(n, k))
# output: [1, 0, 0, 1, 0]
```

**Return sample of rolling k dices n times**
``` python
print(random.roll_dice(n, k))
# output: [[1, 4], [1, 1]]
```

**Return sample of picking a card from a deck of 52 cards n times**
``` python
print(random.shuffle_deck(n))
# output: ["Ace of Spades", "Ace of Hearts", "Ace of Clubs", "Ace of Diamonds", "Ace of Clubs"]
```
---

**Classes**
`mrandom.RandomGenerator` - Random number generator

Methods:

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