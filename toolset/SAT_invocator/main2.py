from pycryptosat import Solver


def tables_for_sat(size_new, size_old, transition_num):
    A = [[0] * size_new for i in range(size_old)]
    B = [[0] * transition_num for i in range(size_new ** 2)]
    counter_num_st = 1  # X(n)
    for j in range(size_old):
        for i in range(size_new):
            A[j][i] = counter_num_st
            counter_num_st += 1

    counter_num_tr = counter_num_st  # Y(n)

    for j in range(size_new ** 2):
        for i in range(transition_num):
            B[j][i] = counter_num_tr
            counter_num_tr += 1

    return A, B


if __name__ == '__main__':

    with open("input.txt") as file:
        all_in = [row.strip() for row in file]
    fout = open('output.txt', 'w')  # файл для визуализации условий для решателя
    program_output = open('sat_to_genFSM.txt', 'w')  # файл для передачи на этап генерации

    inputs_array = [all_in[i][:all_in[i].find(" ")] for i in range(len(all_in))]  # входные воздействия КА

    print(inputs_array)

    output_array = [int(all_in[i][all_in[i].find(" ") + 1:]) for i in range(len(all_in))]  # выходные воздействия КА
    print(output_array)
    inputs_decimal = [int(inputs_array[i], base=2) for i in range(len(inputs_array))]
    print(inputs_decimal)
    size_old = len(inputs_array)  # длина трассы переходов = кол-во исходных состояний

    print(size_old)
    transitions_num = 2 ** len(inputs_array[0])
    print(transitions_num)
    num_of_of_output=len(set(output_array))
    for size_new in range(3, size_old):
        fout.seek(0)
        s = Solver()
        result = tables_for_sat(size_new, size_old, transitions_num)
        first_matrix = result[0]
        second_matrix = result[1]

        print(first_matrix)
        print(second_matrix)
        trans = []
        slice_pairs = []
        pair_index = 0
        counter = 1
        d = []

        for e in range(len(first_matrix)):  # первое условие
            first_clause = []
            for x in first_matrix[e]:
                print(x, end=' ', file=fout)
                first_clause.append(x)
            print("1", file=fout)
            s.add_clause(first_clause)

        pair = [(value1, value2) for row in first_matrix for i, value1 in enumerate(row) for value2 in
                row[i + 1:]]  # второе условие
        for value1, value2 in pair:
            print("-" + str(value1), "-" + str(value2), "2", file=fout)
            s.add_clause([-value1, -value2])

        for i in range(size_old-1):
            for k in range(i+1, size_old):
                if output_array[i] != output_array[k]:
                    for j in range(size_new):
                        value1 = first_matrix[i][j]
                        value2 = first_matrix[k][j]
                        print(str(-value1), str(-value2), "3", file=fout)
                        s.add_clause([-value1, -value2])

        for i in range(0, len(second_matrix), size_new):
            # Создание списка столбцов матрицы
            columns = [list(column) for column in zip(*second_matrix[i:i + size_new])] # срез матрицы по кол-ву существующих переходов из одного сотояний
            for column in columns:
                for k in range(len(column)):
                    for j in range(k + 1, len(column)):
                        value1 = column[k]
                        value2 = column[j]
                        print(str(-value1), str(-value2),"4", file= fout)
                        s.add_clause([-value1, -value2])

        for z in range(size_old - 1):  # пятое и шестое
            for i in range(len(second_matrix)):
                trans.append(second_matrix[i][inputs_decimal[z]])
            for elem in (first_matrix[z]):
                for j in range(size_new):
                    d = [-elem, first_matrix[z + 1][j]]
                    slice_pairs.append(d)
                    if (first_matrix[z].index(elem) == j) & (output_array[z] != output_array[z + 1]):
                        pair_index += 1
                        continue
                    print(str(trans[pair_index]), str(slice_pairs[pair_index][0]), str(-slice_pairs[pair_index][1]), 5, file=fout)
                    print("-"+str(trans[pair_index]), str(slice_pairs[pair_index][0]), str(slice_pairs[pair_index][1]), 6, file=fout)
                    s.add_clause([trans[pair_index], slice_pairs[pair_index][0], -slice_pairs[pair_index][1]])
                    s.add_clause([-trans[pair_index], slice_pairs[pair_index][0], slice_pairs[pair_index][1]])
                    pair_index += 1
                counter += 1
            counter = counter % (size_old -2)
        sat, solution = s.solve()
        if sat:
            print(sat)
            print(solution)
            print(size_old, end=' ', file=program_output)
            print(size_new, end=' ', file=program_output)
            print(transitions_num, file=program_output)
            for i in range(len(solution) - 1):
                if solution[i + 1]:
                    print(i + 1, end=' ', file=program_output)
                else:
                    print(-(i + 1), end=' ', file=program_output)
            print("", file=program_output)
            for i in range(size_new):
                cnt_outs = i + 1
                for j in range(size_old):
                    print(cnt_outs)
                    if solution[cnt_outs]:
                        print(str(output_array[j]), end=' ', file=program_output)
                        break
                    else:
                        cnt_outs += size_new
            break

