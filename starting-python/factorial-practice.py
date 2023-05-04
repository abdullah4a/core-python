from math import factorial as fact


def main():
    n = 5
    factorial = fact(n)
    print(f"{factorial}")
    print(len(str(factorial)))
    print("Hacks")
    print(0b10)
    print(0o10)
    print(0x10)
    print(int(3.5))
    """
    To take base of variable
    one need to pass int(str_val, base)
    eg int("10000",3) // output will be 81
    see example below
    """
    print(int("10000",3))

main()
