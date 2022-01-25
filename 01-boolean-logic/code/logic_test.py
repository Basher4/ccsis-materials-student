from logic_answer import Logic

def NAND(A, B):
    return ~(A*B)

def AND(A, B):
    return A*B

def NAND_CNF(A, B):
    return (~A + ~B)

Logic.print_truthtable(NAND, NAND_CNF, AND)
print('Is NAND and NAND_CNF eqivalent:', Logic.is_equivalent(NAND, NAND_CNF))
print('Is NAND and AND eqivalent:', Logic.is_equivalent(NAND, AND))
