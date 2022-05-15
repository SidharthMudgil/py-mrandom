from mrandom import mrandom


def main():
    random = mrandom.RandomGenerator()
    print(random.rand())
    print(random.randint(1, 5))
    print(random.randrange(1, 5))
    print(random.sample(1, 5, 5))
    print(random.choice([1, 2, 3, 4, 5]))
    print(random.flip_coin(5, 2))
    print(random.roll_dice(5, 2))
    print(random.shuffle_deck(5))


if __name__ == '__main__':
    main()
