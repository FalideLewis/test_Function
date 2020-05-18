a = int(input())
b = int(input())


def printMax(a, b):
    if a > b:
        print(a, 'More')

    elif b > a:
        print(b, 'More')

    elif a == b:
        print(a, 'values are equal', b)

    else:
        print('Check the values are correct')


printMax(a, b)
