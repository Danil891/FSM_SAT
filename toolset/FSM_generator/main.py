def traceToState(state):  # связывание каждого состояния с переходом
    for i in range(0, new_state):
        state[i] = []
        for j in range(trace_route):
            if second_t[i][j] > 0:
                var = state[i].append(j)

    return state


def decTobin(dec):  # конвертер двоичных чисел, понятных языку verilog
    i = 0
    while 2 ** i <= dec:
        i += 1
    dec = bin(dec)
    s = "'" + str(dec)[1::]
    return s


def uml(state):
    for i in range(len(c)):
        for j in range(len(c[i])):
            umlDiagram.write("St" + str(state) + " --> St" + str(i) + " : " + str(bin(c[i][j])) + "\n")


def create_state(state):  # функция для описания перехода из одного состояния в следующее
    sub_counter = 0
    my_file.write("\t\t" + list_of_states[state] + " : begin\n")

    my_file.write("\t\t\tout = " + decTobin(state_output[state]) + ";\n")
    first = 0
    while (sub_counter) < len(c):  # циклично описываю переходы
        for i in range(len(c[sub_counter])):
            if (sub_counter != 0 and first != 0):
                my_file.write("\t\t\telse if (in == ")
            else:
                my_file.write("\t\t\tif (in == ")
            my_file.write(decTobin(c[sub_counter][i]) + ") begin\n")  # параметризировал переходы состояний
            my_file.write("\t\t\t\t state_next = s" + str(sub_counter) + ";\n"
                                                                         "\t\t\tend\n")
            first += 1
        sub_counter += 1
    else:
        my_file.write("\t\t\telse begin\n"
                      "\t\t\t\t state_next = s" + str(state) + ";\n"
                                                               "\t\t\tend\n")
    my_file.write("\t\tend\n")


if __name__ == '__main__':
    f = open('input.txt')
    first_line = f.readline()
    first_line = list(map(int, first_line.split()))
    old_state = first_line[0]  # кол-во старых состояний
    new_state = first_line[1]  # кол-во новых состояний
    trace_route = first_line[2]  # кол-во возможных переходов между состояниями
    list_of_states = []

    for i in range(new_state):  #
        list_of_states.append("s" + str(i))  # создаем массив с именами переменных
    print(first_line)

    sat_exit = f.readline()
    sat_exit = sat_exit.replace("\n", "")

    sat_exit = list(map(int, sat_exit.split(" ")))  # создаем массив со значениями из выхода SAT-решателя

    for i in range(len(sat_exit)):  # для удобства переформатируем положительные и отрицательные
        # значения в логические "1" и "0" соответственно
        if sat_exit[i] > 0:
            sat_exit[i] = 1
        else:
            sat_exit[i] = 0
    line_output = f.readline()
    line_output = list(map(int, line_output.split(" ")))
    state_output = line_output
    print(state_output)
    o = 0
    first_t = []
    counter = 0

    for i in range(0, old_state):
        first_t.append(sat_exit[counter + new_state * i:new_state * (i + 1)])  # получили матрицу , где
        # №строки - № состояния в исходнном конечном автомате, полученного с временной диграммы,
        # №столбца - № нового состояние, в которое старое переходит
    print(first_t)
    second_t = []
    demi_t = sat_exit[(old_state * new_state):]  # срез для заполнения второй таблицы

    for i in range(0, new_state * new_state):
        second_t.append(demi_t[counter + trace_route * i:trace_route * (i + 1)])
    print(second_t)  # получили вторую раскрашенную таблицу
    set_with_traces = {}
    a = []
    b = []

    for i in range(new_state):
        a.append("s" + str(i))
        b.append("s" + str(i))
        set_with_traces[a[i]] = []

    set_of_states = set()
    for i in range(new_state):
        traceToState(b)
        set_with_traces["s" + str(i)] = b[:]
        second_t = second_t[new_state:]

    print(set_with_traces)  # получили словарь, где ключ - само состояние;
    # value - матрица, где i - массив с индексом равным состоянию,
    # в которое необходимо совершить переход, а j - сигналы, по которым совершается переход
    umlDiagram = open("output1.txt", "w+")
    my_file = open("output.v", "w+")
    my_file.write("module Moore2\n" + "(\n\tinput wire clk, reset, \n"
                                      "\tinput wire [1:0] in,\n"
                                      "\toutput reg [1:0] out \n"
                                      ");\n")

    my_file.write("localparam [" + str(new_state) + ":0]\n")
    umlDiagram.write("@startuml\nstate \"St0\"\n")

    for i in range(new_state):
        my_file.write("\ts" + str(i) + " = " + str(i))
        umlDiagram.write("St" + str(i) + ": state value " + str(state_output[i]) + "\n")
        if i != new_state - 1:
            my_file.write(",\n")
        else:
            my_file.write(";\n")

    my_file.write("\n\t reg[4:0] state_reg, state_next;\n"
                  "always @(posedge clk, posedge reset) begin\n"
                  "\t if (reset) begin\n"
                  "\t\t state_reg <= s")
    for elem in first_t[0]:
        if elem: my_file.write(str(first_t[0].index(elem))+"\n")

    my_file.write(
        "\tend\n"
        "\t else begin\n"
        "\t\t state_reg <= state_next;\n"
        "\tend\n"
        "end\n\n")
    my_file.write("always @(in, state_reg) begin\n"
                  "\tstate_next = state_reg;\n"
                  "\tcase (state_reg)\n")
    for i in range(new_state):
        c = tuple(set_with_traces.get(list_of_states[i]))
        uml(i)
        create_state(i)
    my_file.write("\tendcase\nend\n\nendmodule\n")
    my_file.close()
    umlDiagram.write("@enduml")
    umlDiagram.close()
