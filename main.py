def citire_lst():
    """
    Citeste o lista de numere intregi
    param:
    return:
        lista citita
    """
    # TODO
    res_lst = []
    return res_lst


def run_tests():
    """
    Executa functiile de test
    param:
    return:
    """
    # TODO
    pass


def print_menu():
    print("1. Citire lista")
    print("")
    print("")
    print("")
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
            # TODO
            pass
        elif x == "3":
            # TODO
            pass
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
