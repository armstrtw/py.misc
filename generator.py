def odd(start: int):
    n = start
    while True:
        if n % 2 == 1:
            yield n
        n += 1

def even_sq(start: int):
    n = start
    while True:
        if n % 2 == 0:
            yield n ** 2
        n += 1


if __name__ == "__main__":
    print("odd gen:")
    odd_gen = odd(2)
    print(next(odd_gen))
    print(next(odd_gen))
    print(next(odd_gen))
    print(next(odd_gen))
    print("even_sq gen:")
    even_sqg = even_sq(5)
    print(next(even_sqg))
    print(next(even_sqg))
    print(next(even_sqg))
    print(next(even_sqg))

    ## generator comprehension
    esqg = (i ** 2 for i in range(1_000_000) if i % 2 == 0)
