from functools import reduce


def sum_function(*parameter):
    c = reduce(lambda a, b: a + b, parameter)
    print(c)




sum_function(2, 5, 6, 7)

def odd_square(n,k):
    result =[el**2 for el in range(n,k) if el%2!=0]
    print(result)


odd_square(2,6)