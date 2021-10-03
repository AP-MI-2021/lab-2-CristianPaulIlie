def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def get_largest_prime_below(n):
    '''
    Găsește ultimul număr prim mai mic decât un număr dat.
    :param : n - numar natural
    :return:i - ultimul numar prim mai mic decat n
    '''
    for i in range(n - 1, 2, -1):
        if is_prime(i):
            return i


def is_palindrome(n):
    aux = n
    x = 0
    '''
        -Determina daca n este palindrom 
        param:-n, numar intreg
        Output:
        -True sau False, daca n este palindrom,respectiv daca n nu este palindrom
        '''
    while aux > 0:
        x = x * 10 + aux % 10
        aux = aux // 10
    if n == x:
        return True
    return False


def is_superprime(n):
    '''
    -Determina daca un numar este superprim
    Input:
    -n,numar intreg,natural
    Output:
    -True sau False , daca n este superprim,respectiv daca n nu este superprim
    '''
    while n > 0:
        if is_prime(n) == False:
            return False
        n = n // 10
    return True


def test_get_largest_prime_below():
    assert get_largest_prime_below(17) == (13)
    assert get_largest_prime_below(11) == (7)
    assert get_largest_prime_below(229) == (227)


def test_is_palindrome():
    assert is_palindrome(65489) == False
    assert is_palindrome(1221) == True
    assert is_palindrome(98273) == False


def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(17) == True
    assert is_superprime(214) == False


test_get_largest_prime_below()
test_is_palindrome()
test_is_superprime()
