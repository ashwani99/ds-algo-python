# O(modulo)
def modular_inverse(number, modulo):
    for b in range(modulo-1, 0, -1):
        if ((number*b)%modulo) == 1:
            return b

# O(log(max(number, modulo)))
# uses extended Euclid's algorithm as sub routine
from gcd import extended_euclid_gcd_recursive

def modular_inverse_extended_euclid(number, modulo):
    coeffs = [1, 1]
    extended_euclid_gcd_recursive(number, modulo, coeffs)
    return coeffs[0]


# O(log(modulo))
# only works when modulo is prime
# this uses multiplicative exponentiation as subroutine
from exponentiation import modular_exponentiation

def modular_inverse_fermats_theorem(number, modulo):
    return modular_exponentiation(number, modulo-2, modulo)


if __name__ == '__main__':
    number = 5
    modulo = 12
    print('[Modular Inverse] of {} = {}'.format(number, modular_inverse(number, modulo)))
    print('[Modular Inverse using extended euclild] of {} = {}'.format(number, modular_inverse_extended_euclid(number, modulo)))
    modulo = 13
    print('[Modular Inverse using fermat theorem and exponentiation] of {} = {}'.format(number, modular_inverse_fermats_theorem(number, modulo)))
