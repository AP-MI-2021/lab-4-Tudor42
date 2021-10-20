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
            # TODO
            pass
        elif x == "5":
            # TODO
            pass
        elif x == "6":
            break
        else:
            print("Nu exista astfel de optiune")


if __name__ == "__main__":
    main()
