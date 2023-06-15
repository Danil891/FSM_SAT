from pycryptosat import Solver


def trace_to_sat():
    with open("input.txt") as file:
        all_in = [row.strip() for row in file]
    fout = open('output.txt', 'w')
    program_output = open('sat_to_genFSM.txt', 'w')
    inputs_array = [all_in[i][:all_in[i].find(" ")] for i in range(len(all_in))]
    print(inputs_array)
    output_array = [int(all_in[i][all_in[i].find(" ") + 1:]) for i in range(len(all_in))]
    print(output_array)
    size_old = len(inputs_array)
    print(size_old)
    transitions_num = 2 ** len(inputs_array[0])
    print(transitions_num)
    output_counter0 = 0
    output_counter1 = 0
    inputs_decimal = [int(inputs_array[i], base=2) for i in range(len(inputs_array))]
    print(inputs_decimal)
    for i in range(len(output_array)):
        if output_array[i] == 0:
            output_counter0 += 1
        else:
            output_counter1 += 1
    for size_new in range(3, size_old + 1):
        fout.seek(0)
        s = Solver()
        print(size_new)
        cnt1 = 0  # 1st condition
        cnt1s = 1
        for i in range(size_old):
            arr1 = [cnt1s + j for j in range(size_new)]
            s.add_clause(arr1)
            cnt1s += size_new
            for j in range(size_new):
                cnt1 += 1
                print(cnt1, end=' ', file=fout)
            print("1", file=fout)
        cnt2_1 = 1  # 2nd condition
        cnt2_2 = 2
        while cnt2_1 <= size_old * size_new:
            print("-" + str(cnt2_1) + " -" + str(cnt2_2) + " 2", file=fout)
            s.add_clause([-cnt2_1, -cnt2_2])
            if cnt2_2 >= size_new and cnt2_2 % size_new == 0 and (cnt2_1 + 1) % size_new == 0:
                cnt2_1 += 2
                cnt2_2 = cnt2_1 + 1
            elif cnt2_2 >= size_new and cnt2_2 % size_new == 0:
                cnt2_1 += 1
                cnt2_2 = cnt2_1 + 1
            else:
                cnt2_2 += 1
        cnt3_1 = 1  # 3rd condition
        cnt3_2 = 0
        array_ones = [0] * output_counter1
        for i in range(size_old):
            if output_array[(cnt3_1 - 1) // size_new] == 1:
                array_ones[cnt3_2] = cnt3_1
                cnt3_2 += 1
            cnt3_1 += size_new
        # print(array_ones)
        cnt3_3 = 1
        for i in range(size_new):
            for j in range(output_counter1):
                for k in range(size_old):
                    if output_array[k] == 0:
                        print("-" + str(cnt3_3 + i) + " -" + str(array_ones[j] + i) + " 3", file=fout)
                        s.add_clause([-(cnt3_3 + i), -(array_ones[j] + i)])
                    cnt3_3 += size_new
                cnt3_3 = 1
        cnt5_1 = size_new * size_old + 1  # 5th condition
        cnt5_2 = cnt5_1 + transitions_num
        for i in range(size_new - 1):
            for j in range((size_new - i - 1) * transitions_num * size_new):
                # print(j)
                print("-" + str(cnt5_1) + " -" + str(cnt5_2) + " 5", file=fout)
                s.add_clause([-cnt5_1, -cnt5_2])
                if (cnt5_1 - size_new * size_old) % transitions_num == 0 and cnt5_2 == cnt5_1 + (
                        size_new - i - 1) * transitions_num:
                    cnt5_1 = cnt5_1 + transitions_num * (size_new - 1) + 1
                    cnt5_2 = cnt5_1 + transitions_num
                elif cnt5_2 == cnt5_1 + (size_new - i - 1) * transitions_num:
                    cnt5_1 += 1
                    cnt5_2 = cnt5_1 + transitions_num
                else:
                    cnt5_2 += transitions_num
            cnt5_1 = size_new * size_old + 1 + transitions_num * (i + 1)
            cnt5_2 = cnt5_1 + transitions_num
        for i in range(len(inputs_array) - 1):  # 6th and 7th conditions
            cnt6_in = size_new * size_old + 1 + inputs_decimal[i]
            cnt6_1 = 1 + i * size_new
            cnt6_2 = cnt6_1 + size_new
            while cnt6_1 % size_new != 0 and cnt6_2 % size_new != 0:
                if not ((cnt6_2 - cnt6_1) % size_new == 0 and output_array[i] != output_array[i + 1]):
                    print(str(cnt6_in) + " -" + str(cnt6_1) + " -" + str(cnt6_2) + " 6", file=fout)
                    s.add_clause([cnt6_in, -cnt6_1, -cnt6_2])
                    print("-" + str(cnt6_in) + " -" + str(cnt6_1) + " " + str(cnt6_2) + " 7", file=fout)
                    s.add_clause([-cnt6_in, -cnt6_1, cnt6_2])
                cnt6_in += transitions_num
                cnt6_2 += 1
                if cnt6_2 % size_new == 0:
                    if not ((cnt6_2 - cnt6_1) % size_new == 0 and output_array[i] != output_array[i + 1]):
                        print(str(cnt6_in) + " -" + str(cnt6_1) + " -" + str(cnt6_2) + " 6", file=fout)
                        s.add_clause([cnt6_in, -cnt6_1, -cnt6_2])
                        print("-" + str(cnt6_in) + " -" + str(cnt6_1) + " " + str(cnt6_2) + " 7", file=fout)
                        s.add_clause([-cnt6_in, -cnt6_1, cnt6_2])
                    cnt6_in += transitions_num
                    cnt6_1 += 1
                    cnt6_2 -= size_new - 1
            else:
                for j in range(size_new):
                    if not ((cnt6_2 - cnt6_1) % size_new == 0 and output_array[i] != output_array[i + 1]):
                        print(str(cnt6_in) + " -" + str(cnt6_1) + " -" + str(cnt6_2) + " 6", file=fout)
                        s.add_clause([cnt6_in, -cnt6_1, -cnt6_2])
                        print("-" + str(cnt6_in) + " -" + str(cnt6_1) + " " + str(cnt6_2) + " 7", file=fout)
                        s.add_clause([-cnt6_in, -cnt6_1, cnt6_2])
                    cnt6_in += transitions_num
                    cnt6_2 += 1
        cnt6_in = size_new * size_old + 1 + inputs_decimal[-1]
        cnt6_1 = 1 + size_new * (size_old - 1)
        cnt6_2 = 1
        while cnt6_1 % size_new != 0 and cnt6_2 % size_new != 0:
            if not ((cnt6_1 - cnt6_2) % size_new == 0 and output_array[0] != output_array[-1]):
                print(str(cnt6_in) + " -" + str(cnt6_1) + " -" + str(cnt6_2) + " 6", file=fout)
                s.add_clause([cnt6_in, -cnt6_1, -cnt6_2])
                print("-" + str(cnt6_in) + " -" + str(cnt6_1) + " " + str(cnt6_2) + " 7", file=fout)
                s.add_clause([-cnt6_in, -cnt6_1, cnt6_2])
            cnt6_in += transitions_num
            cnt6_2 += 1
            if cnt6_2 % size_new == 0:
                if not ((cnt6_1 - cnt6_2) % size_new == 0 and output_array[0] != output_array[-1]):
                    print(str(cnt6_in) + " -" + str(cnt6_1) + " -" + str(cnt6_2) + " 6", file=fout)
                    s.add_clause([cnt6_in, -cnt6_1, -cnt6_2])
                    print("-" + str(cnt6_in) + " -" + str(cnt6_1) + " " + str(cnt6_2) + " 7", file=fout)
                    s.add_clause([-cnt6_in, -cnt6_1, cnt6_2])
                cnt6_in += transitions_num
                cnt6_1 += 1
                cnt6_2 -= size_new - 1
        else:
            for j in range(size_new):
                if not ((cnt6_1 - cnt6_2) % size_new == 0 and output_array[0] != output_array[-1]):
                    print(str(cnt6_in) + " -" + str(cnt6_1) + " -" + str(cnt6_2) + " 6", file=fout)
                    s.add_clause([cnt6_in, -cnt6_1, -cnt6_2])
                    print("-" + str(cnt6_in) + " -" + str(cnt6_1) + " " + str(cnt6_2) + " 7", file=fout)
                    s.add_clause([-cnt6_in, -cnt6_1, cnt6_2])
                cnt6_in += transitions_num
                cnt6_2 += 1
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


if __name__ == '__main__':
    trace_to_sat()
