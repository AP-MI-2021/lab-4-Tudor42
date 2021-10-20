def cmmdc(a, b):
    """
    Returneaza cmmdc a lui a si b
    param:
        a - primul numar
        b - al doilea numar
    return:
        cmmdc(a, b)
    """
    x = a
    r = b
    while r != 0:
        y = x % r
        x = r
        r = y
    return x


def test_cmmdc():
    assert cmmdc(10, 5) == 5
    assert cmmdc(24, 18) == 6
    assert cmmdc(5, 2) == 1


def inversare_string(x):
    """
    Returneaza stringul x inversat
    param:
        x - stringul
    return:
        stringul inversat
    """
    return x[::-1]


def test_inversare_string():
    assert inversare_string("erp") == "pre"
    assert inversare_string("1020") == "0201"
    assert inversare_string("") == ""


def modificare_lista(lst):
    """
    Inlocuieste numerele pozitive nenule cu cmmdc
    param:
        lst - lista de numere
    return:
        Lista modificata
    """
    x = 0  # Pastreaza cel mai mic divizor al numerelor pozitive
    for i in lst:
        if i > 0:
            x = cmmdc(x, i)
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = x
        elif lst[i] < 0:
            s = '-' + inversare_string(str(lst[i])[1:])
            lst[i] = int(s)
    return lst


def test_modificare_lista():
    assert modificare_lista([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]
    assert modificare_lista([4]) == [4]
    assert modificare_lista([2, 8]) == [2, 2]
    assert modificare_lista([]) == []


def is_prime(n):
    """
    Verifica daca un numar este prim
    param:
        n - numar
    return:
        True sau False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(10) is False
    assert is_prime(1) is False
    assert is_prime(23) is True


def is_superprime(n):
    """
    Verifica daca un numar este super prim
    param:
        n - numarul
    return:
        True - daca este super prim
        False - daca nu este super prim
    """
    if n <= 0:
        return False
    for i in range(1, len(str(n))+1):
        s = str(n)[:i]
        if not is_prime(int(s)):
            return False
    return True


def test_is_superprime():
    assert is_superprime(0) is False
    assert is_superprime(239) is True


def numere_superprime(lst):
    """
    Returneaza o lista de numere superprime din lst
    param:
        lst - lista de numre
    return:
        Lista de numere superprime
    """
    res_lst = []
    for x in lst:
        if is_superprime(x):
            res_lst.append(x)
    return res_lst


def test_numere_superprime():
    assert numere_superprime([239, 1, 23]) == [239, 23]
    assert numere_superprime([9, 10, 5, 2]) == [5, 2]
    assert numere_superprime([]) == []


def cel_mai_mic_numar(lst, n):
    """
    Returneaza cel mai mic numar
    cu ultima cifra n
    param:
        lst - lista de numere
        n - cifra
    return:
        cel mai mic numar din lista
        cu ultima cifra n
    """
    res = None
    for x in lst:
        if x % 10 == n:
            if res is None:
                res = x
            elif x < res:
                res = x
    return res


def test_cel_mai_mic_numar():
    assert cel_mai_mic_numar([10, -1, -20, 0], 0) == -20
    assert cel_mai_mic_numar([15, 5, 255, 0], 5) == 5
    assert cel_mai_mic_numar([10, 15, 14], 2) is None


def numere_negative(lst):
    """
    Returneaza o lista de numere negative
    param:
        lst - lista de numere
    return:
        lista de numre negative
    """
    res_lst = []
    for x in lst:
        if x < 0:
            res_lst.append(x)
    return res_lst


def test_numere_negative():
    assert numere_negative([10, -1, -3, 0, 10]) == [-1, -3]
    assert numere_negative([]) == []
    assert numere_negative([0, 1, 2, 3]) == []


def citire_lst():
    """
    Citeste o lista de numere intregi
    param:
    return:
        lista citita
    """
    res_lst = [int(x) for x in input('Dati sirul de numere prin'
                                     ' spatiu: ').split()]
    return res_lst


def run_tests():
    """
    Executa functiile de test
    param:
    return:
    """
    test_numere_negative()
    test_cel_mai_mic_numar()
    test_is_prime()
    test_is_superprime()
    test_numere_superprime()
    test_cmmdc()
    test_inversare_string()
    test_modificare_lista()


def print_menu():
    print("1. Citire lista")
    print("2. Afișarea tuturor numerelor negative nenule din listă")
    print("3. Afișarea celui mai mic număr care are ultima cifră"
          " egală cu o cifră citită de la tastatură.")
    print("4. Afișarea tuturor numerelor din listă care sunt superprime."
          " Un număr este superprim dacă este"
          " strict pozitiv și toate prefixele sale sunt prime.")
    print("5. Afișarea listei obținute din lista inițială în care numerele "
          "pozitive și nenule au fost înlocuite cu"
          " CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
    print("6. Exit")


def main():
    """
    Apeleaza functiile de test si face interfata
    de tip consola
    param:
    return:
    """
    run_tests()
    lst = []
    while True:
        print_menu()
        x = input("Dati optiunea: ")
        if x == "1":
            lst = citire_lst()
        elif x == "2":
            for i in numere_negative(lst):
                print(i)
        elif x == "3":
            i = input("Dati o cifra: ")
            if len(i) > 1:
                print("Trebuie sa fie cifra")
                continue
            print(cel_mai_mic_numar(lst, int(i)))
        elif x == "4":
            for i in numere_superprime(lst):
                print(i)
        elif x == "5":
            print(modificare_lista(lst))
        elif x == "6":
            break
        else:
            print("Nu exista astfel de optiune")


if __name__ == "__main__":
    main()
