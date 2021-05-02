if __name__ == '__main__':
    n = int(input())

numbers = []
for i in range(n):
    if i not in numbers:
        numbers.append(i)

for num in numbers:
    print(num ** 2)
