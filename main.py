from math import gcd


def human(n):
    while not (n == 2 or n == 3):
        m = n

        if n % 2 == 0:
            n /= 2
        elif n % 3 == 0:
            n /= 3

        if n == m:
            return False

    return True


if __name__ == '__main__':
    for i in range(3, 18):
        for j in range(2, i):
            if gcd(i, j) == 1:
                if human(i) and human(j):
                    print(str(i) + '/' + str(j) + ' easy')
                elif not human(i) and not human(j):
                    print(str(i) + '/' + str(j) + ' hard')
                else:
                    print(str(i) + '/' + str(j))
