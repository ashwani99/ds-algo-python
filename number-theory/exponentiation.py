# simple recursive implementation of calculating exponents
# will fail for larger numbers as it could not be stored in in built number containers
# O(n)
def simple_exponentiation(number, exponent):
    if exponent == 0:
        return 1
    return number * simple_exponentiation(number, exponent-1)


# binary exponentiation implementation
# same problem for this as above, very big number will not fit into language built-in containers
# but this is much faster
# O(log(n))
def binary_exponentiation(number, exponent):
    if exponent == 0:
        return 1
    if exponent & 1 == 0:
        return binary_exponentiation(number*number, exponent//2)
    return number * binary_exponentiation(number*number, (exponent-1)//2)


# modular exponentiation
# in this instead of storing the actual result, we store the remainder when divided by a modulo (say it M)
# generally the modulo is taken a big number so that result can fit in the memory
# O(log(n))
def modular_exponentiation(number, exponent, modulo):
    if exponent == 0:
        return 1
    if exponent & 1 == 0:
        return modular_exponentiation((number*number)%modulo, exponent//2, modulo)
    return (number * modular_exponentiation((number*number)%modulo, (exponent-1)//2, modulo))%modulo


if __name__ == '__main__':
    n = 6
    expo = 8
    modulo = 107 # taken small modulo for demonstration

    print('[Simple exponentiation] {}^{} = {}'.format(n, expo, simple_exponentiation(n, expo)))
    print('[Binary exponentiation] {}^{} = {}'.format(n, expo, binary_exponentiation(n, expo)))
    print('[Modular exponentiation] ({}^{})%{} = {}'.format(n, expo, modulo, modular_exponentiation(n, expo, modulo)))
