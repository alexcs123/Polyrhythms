from math import gcd


def squbic(n):
    """Determines if n is a product of only twos and/or threes"""
    while not 2 <= n <= 3:
        if n % 2 == 0:
            n /= 2
        elif n % 3 == 0:
            n /= 3
        else:
            return False

    return True


if __name__ == '__main__':
    limit = 18

    for i in range(3, limit):
        for j in range(2, i):
            if gcd(i, j) == 1:
                if squbic(i) and squbic(j):
                    print(str(i) + ':' + str(j) + ' easy')
                elif squbic(i) or squbic(j):
                    print(str(i) + ':' + str(j))
                else:
                    print(str(i) + ':' + str(j) + ' hard')
