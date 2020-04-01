def getData():
    qtd = input().split()
    if qtd[0].isnumeric() and qtd[1].isnumeric():
        q = [int(n) for n in qtd]
    else:
        print("digite um número válido")
        exit(1)

    if q[0]==0 or q[1]==0:
        exit(1)
    if len(q)>2:
        print("Só é permitido dois jogadores por vez")
        exit(1)

    a = input().split()
    if len(a) != q[0]:
        print("a quantidade de cartas deve ser igual a inserida anteriormente")
        exit(1)

    b = input().split()
    if len(b) != q[1]:
        print("a quantidade de cartas deve ser igual a inserida anteriormente")
        exit(1)

    a = set(a)
    b = set(b)
    return q, a, b


def main():
    q, a, b =getData()
    while q[0] != 0 or q[1] != 0:
        # tem em a, mas não tem em b (conjunto complementar de b)
        auxA = list(a - b)

        # tem em b, mas não tem em a (conjunto complementar de a)
        auxB = list(b - a)

        if(len(auxA) < len(auxB)):
            print(len(auxA))
        else:
            print(len(auxB))
        q, a, b = getData()


if __name__ == '__main__':
    main()