def EQ(x, y) -> bool:
    return x == y


def LT(x, y) -> bool:
    return x < y


def GT(x, y) -> bool:
    return x > y


def ZERO(x) -> bool:
    return x == 0


def NZ(x) -> bool:
    return x != 0


def ADD(memory, Rx, Ry, Rz):
    memory[Rz] = memory[Rx] + memory[Ry]


def SUB(memory, Rx, Ry, Rz):
    memory[Rz] = memory[Rx] - memory[Ry]


def MUL(memory, Rx, Ry, Rz):
    memory[Rz] = memory[Rx] * memory[Ry]


def DIV(memory, Rx, Ry, Rz):
    memory[Rz] = memory[Rx] / memory[Ry]


def LDI(memory, Rx, nn):
    memory[Rx] = nn


def LOAD(memory, Rx, Ry):
    memory[Ry] = memory[Rx]


def STORE(memory, Rx, Ry):
    memory[Rx] = memory[Ry]


def INC(memory, Rx):
    memory[Rx] += 1


def DEC(memory, Rx):
    memory[Rx] -= 1


def CMP(memory, Rx, Ry, comparison_op):
    return comparison_op(memory[Rx], memory[Ry])


def CMP_NN(memory, Rx, nn, comparison_op):
    return comparison_op(memory[Rx], nn)


def JMP(i):
    return i


def JMP_CC(i, condition):
    return condition


def HALT():
    pass


def run_program(program, memory) -> None:
    i = 0
    n = len(program)
    while i < n:
        operation, args = program[i]

        if operation.__name__ == "HALT":
            break
        if operation.__name__ == "JMP":
            i = args[0]
            continue
        if operation.__name__ == "JMP_CC" and operation(*args):
            i = args[0]
            continue

        operation(memory, *args)
        sig: str = f"{operation.__name__}{args}"
        pad = " " * (15 - len(sig))
        print(f"{i = }", f"{sig}{pad}", memory)
        i += 1
    return memory
