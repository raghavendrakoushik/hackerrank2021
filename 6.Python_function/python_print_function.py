if __name__ == '__main__':
    n = int(input())


def numberseries(n):
    series = ""
    for i in range(1, n + 1):
        series += str(i)
    return series


print(numberseries(n))
