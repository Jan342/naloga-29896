def sestej(a, b):
    return a + b


def odstej(a, b):
    return a - b


def pomnozi(a, b):
    return a * b


def deli(a, b):
    if b == 0:
        raise ValueError("Deljenje z nic ni dovoljeno.")
    return a / b


if __name__ == "__main__":
    print("Preprosta racunska aplikacija")
    print("5 + 3 =", sestej(5, 3))
    print("5 - 3 =", odstej(5, 3))
    print("5 * 3 =", pomnozi(5, 3))
    print("6 / 3 =", deli(6, 3))
