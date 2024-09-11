

def is_prime(func):
    def wrapper(a,b,c):
        rezult = func(a,b,c)
        counter = 0
        if rezult > 0 and rezult-round(rezult,0) == 0:
            for i in range(rezult):
                if rezult %(i+1) == 0:
                    counter += 1
                    if counter > 2:
                        print('Составное')
                        return rezult
            print('Простое')
            return rezult
        else:
            return 'Простым или составным числом могут быть натуральные числа'
    return wrapper

@is_prime
def sum_three(a,b,c):
    if (type(a) == int or float and type(b) == int or float
            and type(c) == int or float):
        summ =a+b+c
    else:
        print('Аргумент не является числом')
        return 0
    return summ


result = sum_three(2, 3, 6)
print(result)