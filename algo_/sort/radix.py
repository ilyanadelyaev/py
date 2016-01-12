def radix_sort(D, reverse=False):
    """
    Порязрядная сортировка.
    ---
    O(N) - Линейное время работы алгоритма
    Требуется дополнительные объем памяти, равный исходному объему ключей.
    ---
    Начигая с меньшего разряда, сортируем ключи во вспомогательные массивы.
    После сортировки складываем вспомогательные массивы.
    Пока один из вспомогательных массивов не будет пустой после сортировки.
    """

    D = D[:]

    bp = 0
    while True:
        T = [[], []]
        for d in D:
            b = 1 & int(d) >> bp
            T[b].append(d)
        if not len(T[0]) or not len(T[1]):
            break
        D = T[1] + T[0] if reverse else T[0] + T[1]
        bp += 1

    return D


if __name__ == '__main__':
    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    #print I

    D = radix_sort(I)
    DD = sorted(I)
    print 'D == DD:', D == DD

    D = radix_sort(I, reverse=True)
    DD = sorted(I, reverse=True)
    print 'reverse: D == DD:', D == DD
