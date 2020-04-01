def get_data():
    m, n = [int(i) for i in input().split()]
    l = int(input()) / 100
    k = input()
    tam = [int(i) for i in input().split()]
    return m, n, l, k, sorted(tam, reverse=True)

def get_matrix(x, y, l):
    if x % l != 0.0:
        return
    x_size = int(x / l)
    return [y] * x_size

def fill_matrix(available, vet):
    vet_aux = vet
    used = []

    for e in vet_aux:
        available_aux = available
        in_use = 0
        in_use_pos = -1
        if e > available_aux:
            pass
        in_use, in_use_pos = e, vet_aux.index(e)

        available_aux = available_aux - in_use
        if available_aux == 0:
            return True, [in_use]
        for i in range(in_use_pos + 1, len(vet_aux)):
            if vet_aux[i] == available_aux:
                used = [in_use, vet_aux[i]]
                return True, used

    return False, used

    pass

def remove_used(used, tam):
    for e in used:
        tam.remove(e)

def get_used_vet(matrix, tam):
    if matrix is None:
        return 0
    tam_aux = tam.copy()
    total_used = 0
    for i in range(0, len(matrix)):
        success, used = fill_matrix(matrix[i], tam_aux)
        if not success:
            return 0
        remove_used(used, tam_aux)
        total_used = total_used + len(used)
    return total_used

def main():
    m, n, l, k, tam = get_data()
    matrix = get_matrix(m, n, l)
    matrix2 = get_matrix(n, m, l)

    total = get_used_vet(matrix, tam)
    total2 = (get_used_vet(matrix2, tam))

    if total == 0 and total2 == 0:
        print('impossivel')
        exit(0)

    result = None

    if total == 0 or total2 == 0:
        result = total if total2 == 0 else total2
    else:
        result = total if total2 > total else total2

    print(result)

if __name__ == '__main__':
    main()