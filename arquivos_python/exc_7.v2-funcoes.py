def fatorial(num, show=False):
    """

    """
    fat = 1

    for n in range(num, 0, -1):
        fat = n * fat

        if show:
            print(n, end='')
            if n != 0:
                if n == 1:
                    print(' = ', end='')
                else:
                    print(' x ', end='')

    return fat


print(fatorial(3, show=True))
