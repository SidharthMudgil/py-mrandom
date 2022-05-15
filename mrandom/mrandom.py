"""
Module to generate random numbers

Algorithm used: Mersenne Twister
- general purpose pseudorandom number generator
- developed by Makoto Matsumoto and Takuji Nishimura
- strong PCRG with a period of 2^19937-1
- based on matrix linear recurrence
- not suitable for cryptography
- algorithm is twisted generalised feedback shift register (TGSR)
- used in programming languages such as Python, C++, etc.
"""


class MT11937:
    """
    A class to generate random numbers.

    Methods:
        seed(seed: int):
            Initialize the generator from a seed.

        twist():
            Twist the generator.

        extract_number():
            Extract a random number.
    """

    def __init__(self, seed: int = 0, flavor: int = 1):
        # Standard Mersenne Twister constants (from Wikipedia)

        if flavor != 2:
            self.w = 32  # word size
            self.n = 624  # degree of recurrence
            self.m = 397  # middle word
            self.r = 31  # separation point
            self.a = 0x9908B0DF  # coefficient of rational normal form twist matrix
            self.u, self.d = 11, 0xFFFFFFFF  # tempering bitmasks
            self.s, self.b = 7, 0x9D2C5680  # tempering bit shifts
            # additional tempering bitmasks/ shifts
            self.t, self.c, self.l = 15, 0xEFC60000, 18
            # other constants
            self.f = 1812433253

        elif flavor == 2:
            self.w = 64  # word size
            self.n = 312  # degree of recurrence
            self.m = 156  # middle word
            self.r = 31  # separation point
            self.a = 0xB5026F5AA96619E9  # coefficient of rational normal form twist matrix
            self.u, self.d = 29, 0x5555555555555555  # tempering bitmasks
            self.s, self.b = 17, 0x71D67FFFEDA60000  # tempering bit shifts
            # additional tempering bitmasks/ shifts
            self.t, self.c, self.l = 37, 0xFFF7EEE000000000, 43
            # other constants
            self.f = 6364136223846793005

        self.MT = [0] * self.n  # the array of state variables
        self.index = self.n + 1  # initial index
        self.lower_mask = (1 << self.r) - 1  # lower mask
        self.upper_mask = ~self.lower_mask  # upper mask

        self.seed(seed)

    def seed(self, seed: int):
        """
        Initialize the generator from a seed.

        :param seed: The seed to use.

        :return: None
        """
        self.index = self.n
        self.MT[0] = seed
        for i in range(1, self.n):
            self.MT[i] = self.upper_mask & (
                self.f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (self.w - 2))) + i)

    def twist(self):
        """
        Twist the generator.

        :return: None
        """
        for i in range(self.n):
            x = (self.MT[i] & self.upper_mask) + \
                (self.MT[(i + 1) % self.n] & self.lower_mask)
            xA = x >> 1
            if x % 2 != 0:
                xA ^= self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA
        self.index = 0

    def extract_number(self):
        """
        Extract a random number.

        :return: A random number.
        """
        if self.index >= self.n:
            self.twist()

        y = self.MT[self.index]
        y ^= (y >> self.u) & self.d
        y ^= (y << self.s) & self.b
        y ^= (y << self.t) & self.c
        y ^= (y >> self.l)

        self.index += 1
        return y & 0xFFFFFFFF 

    def __repr__(self) -> str:
        return "MT11937"


class RandomGenerator:
    """ 
    A class to generate random numbers.

    Methods:
    __check_for_errors(type, *args):
        Checks for TypeErrors.

    __get_generator():
        Returns the generator.

    rand():
        returns a random number between 0 and 1

    randint(a, b): int
        returns a random number between a and b (inclusive)

    randrange(a, b): int
        returns a random number between a and b (exclusive)

    sample(a, b, k): list
        returns a random sample of size k from range(a, b)

    choice(l): list
        returns a random element from a list

    shuffle(l): list
        shuffles a list

    flip_coin(total_flips, total_coins): str or list
        returns a random coin flip

    roll_dice(total_rolls, total_dice): int or list
        returns a number between 1 and 6 or a list of numbers between 1 and 6

    shuffle_deck(total_flips): string or list
        shuffles a deck of cards    
    """

    def __init__(self, flavour: int = None, seed: int = None):
        """
        Initialize the generator.

        :param flavour: The flavour of generator to use.
        :param seed: The seed to use.

        :return: None
        """
        x = 133
        if seed is None:
            seed = id(x)  # address of object is used as seed 😎

        if flavour in [None, 2, 64]:
            print("                 Using MT19937_64\n")
            print("                By Sidharth Mudgil")
            print("-----------------------------------------------------", end="\n\n")
            self.mt64 = MT11937(seed, 2)
            self.mt32 = None
        elif flavour in [1, 32]:
            print("                 Using MT19937_32\n")
            print("                By Sidharth Mudgil")
            print("-----------------------------------------------------", end="\n\n")
            self.mt32 = MT11937(seed, 1)
            self.mt64 = None
        else:
            raise ValueError(
                "flavour must be [1, 32] for MT11937_64 or [2, 64] for MT11937_32")

    def __check_for_errors(self, type, *args):
        """ 
        Checks for TypeErrors.

        :param type: The type of the arguments.
        :param args: The arguments to check.

        :return: True if no TypeErrors, False otherwise.

        :raises TypeError: if any of the arguments are not of type 'type'.
        """
        for arg in args:
            if not isinstance(arg, type):
                msg = f"argument must be of type {type}"
                raise TypeError(msg)
            else:
                return True

    def __get_generator(self):
        """ 
        Returns the generator.

        :return: The generator.
        """
        return self.mt32 or self.mt64

    def rand(self, r_upto: int = 10) -> float:
        """ 
        Returns a random number between 0 and 1.

        :param r_upto: The number of decimal places to round to.

        :return: float (random number)
        """
        return round(self.__get_generator().extract_number() / 2**32, r_upto)

    def randint(self, a: int, b: int) -> int:
        """ 
        Returns a random number between a and b (inclusive).

        :param a: int (lower bound)
        :param b: int (upper bound)

        :return: int (random number)

        :raises TypeError: if a or b are not integers
        """
        if self.__check_for_errors(int, a, b):
            if a < b:
                generator = self.__get_generator()
                number = generator.extract_number()
                return number % (b - a + 1) + a
            else:
                raise ValueError(
                    "lower bound can't be greater than upper bound")

    def randrange(self, a: int, b: int) -> int:
        """
        Returns a random number between a and b (exclusive).

        :param a: int (lower bound)
        :param b: int (upper bound)

        :return: int (random number)

        :raises TypeError: if a or b are not integers
        """
        if self.__check_for_errors(int, a, b):
            if a < b:
                generator = self.__get_generator()
                number = generator.extract_number()
                return number % (b - a) + a
            else:
                raise ValueError(
                    "lower bound can't be greater than upper bound")

    def sample(self, a: int, b: int, k: int) -> list:
        """ 
        Returns a random sample of size k from range(a, b).

        :param a: int (lower bound)
        :param b: int (upper bound)
        :param k: int (size of sample)

        :return: list (random sample)

        :raises TypeError: if a, b, or k are not integers
        """
        if self.__check_for_errors(int, a, b, k):
            if a < b:
                sample = []
                for _ in range(k):
                    sample.append(self.randint(a, b))
                return sample
            else:
                raise ValueError(
                    "lower bound can't be greater than upper bound")

    def choice(self, l: list, size: int = None) -> list or int:
        """ 
        Returns a random element from a list.

        :param l: list (list to choose from)
        :param size: int (size of sample)

        :return: int or list (random element)

        :raises TypeError: if l is not a list
        """
        if self.__check_for_errors(list, l):
            if size is None:
                choice = self.randint(0, len(l) - 1)
                return l[choice]
            else:
                sample = []
                for _ in range(size):
                    choice = l[self.randint(0, len(l) - 1)]
                    sample.append(choice)
                return sample

    def shuffle(self, l: list) -> list:
        """ 
        Shuffles a list.

        :param l: list (list to shuffle)

        :return: list (shuffled list)

        :raises TypeError: if l is not a list
        """
        if self.__check_for_errors(list, l):
            for _ in range(10 * len(l)):
                index1 = self.randint(0, len(l) - 1)
                index2 = self.randint(0, len(l) - 1)
                l[index1], l[index2] = l[index2], l[index1]
            return l

    def flip_coin(self, total_flips: int = None, total_coins: int = None) -> str or list:
        """
        Returns a random boolean.

        :param total_flips: int (number of flips)
        :param total_coins: int (number of coins)

        :return: str or list (random boolean)

        :raises TypeError: if times is not an integer
        """
        if total_flips:
            if not self.__check_for_errors(int, total_flips):
                return
        if total_coins:
            if not self.__check_for_errors(int, total_coins):
                return

        if total_flips is None:
            if total_coins is None:
                return 'head' if self.rand() < 0.5 else 'tail'
            else:
                sample = []
                for _ in range(total_coins):
                    sample.append('head' if self.rand() < 0.5 else 'tail')
                return sample
        else:
            if total_coins is None:
                sample = []
                for _ in range(total_flips):
                    sample.append('head' if self.rand() < 0.5 else 'tail')
                return sample
            else:
                sample_set = []
                for _ in range(total_flips):
                    sample = []
                    for _ in range(total_coins):
                        sample.append('head' if self.rand() < 0.5 else 'tail')
                    sample_set.append(sample)
                return sample_set

    def roll_dice(self, total_rolls: int = None, total_dice: int = None) -> int or list:
        """
        Rolls a dice.

        :param times: int (number of times to roll)

        :return: int (sum of dice)

        :raises TypeError: if times is not an integer
        """
        if total_rolls:
            if not self.__check_for_errors(int, total_rolls):
                return
        if total_dice:
            if not self.__check_for_errors(int, total_dice):
                return

        if total_rolls is None:
            if total_dice is None:
                return self.randint(1, 6)
            else:
                sample = []
                for _ in range(total_dice):
                    sample.append(self.randint(1, 6))
                return sample
        else:
            if total_dice is None:
                sample = []
                for _ in range(total_rolls):
                    sample.append(self.randint(1, 6))
                return sample
            else:
                sample_set = []
                for _ in range(total_rolls):
                    sample = []
                    for _ in range(total_dice):
                        sample.append(self.randint(1, 6))
                    sample_set.append(sample)
                return sample_set

    def shuffle_deck(self, total_picks: int = None) -> list:
        """ 
        Shuffles a deck.

        :param total_picks: int (number of picks)

        :return: list (shuffled deck)

        :raises TypeError: if times is not an integer
        """
        DECK = {
            "spades": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            "hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            "diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            "clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        }

        if total_picks:
            if not self.__check_for_errors(int, total_picks):
                return

        if total_picks is None:
            suit = self.choice(list(DECK.keys()))
            rank = self.choice(DECK[suit])

            return f'{rank} of {suit}'
        else:
            sample = []

            for _ in range(total_picks):
                suit = self.choice(list(DECK.keys()))
                rank = self.choice(DECK[suit])

                sample.append(f'{rank} of {suit}')

            return sample

    def __repr__(self):
        return "Runner class to generate random numbers"
