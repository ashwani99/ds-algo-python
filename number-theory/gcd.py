# naive solution
# O(min(a,b))
def simple_gcd(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, 0, -1):
        if a%i == 0  and b%i == 0:
            return i


# euclid's GCD
# O(log(max(a, b)))
def euclidean_gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return euclidean_gcd(b%a, a)


# euclid's GCD iterative
def euclidean_gcd_iter(a, b):
    if a > b:
        a, b = b, a
    while a:
        a, b = b%a, a
    return b


# extended euclidean algorithm
# recursive solution
def extended_euclid_gcd_recursive(a, b, coeffs):
    if b == 0:
        coeffs[0], coeffs[1] = 1, 0
        return a
    coeffs1 = [1, 1]
    res = extended_euclid_gcd_recursive(b, a%b, coeffs1)
    coeffs[0], coeffs[1] = coeffs1[1], coeffs1[0]-(a//b)*coeffs1[1]
    return res


if __name__ == '__main__':
    a, b = 35, 15
    print('[Simple GCD] GCD({}, {})={}'.format(a, b, simple_gcd(a, b)))
    print('[Euclidean GCD] GCD({}, {})={}'.format(a, b, euclidean_gcd(a, b)))
    print('[Euclidean GCD] GCD({}, {})={}'.format(a, b, euclidean_gcd_iter(a, b)))
    coeffs = [1, 1]
    d = extended_euclid_gcd_recursive(a, b, coeffs)
    print('[Extended Eucledian GCD] GCD({}, {})={} Coeffs={}'.format(a, b, d, coeffs))
