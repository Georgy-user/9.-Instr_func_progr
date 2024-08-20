def is_prime(func):
    def expertize(*args):
        rez = func(*args)
        i = 1
        for i in range(1, rez // 2):
            i += 1
            if rez % i == 0:
                print(f'Число {rez} - составное.')
                break
            elif i == rez // 2:
                print(f'Число {rez} - простое.')

        return rez

    return expertize


@is_prime
def sum_three(x, y, z):
    return x + y + z


result = sum_three(20, 3, 2)
print(result)
