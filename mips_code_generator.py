from TAC import TACOperation, TACFunctionCall, TACConcat, TACPrint
from my_types import INT_TYPE, FLOAT_TYPE, STRING_TYPE, BOOL_TYPE

class MipsCodeGenerator:
    def __init__(self):
        self.temp_count = 0

    def generate_mips_code(self, tac_code):
        mips_code = [
            ".data",
            "PI: .float 3.141592653589793",
            "E: .float 2.718281828459045",
        ]
        text_section = [
            ".text",
            "main:"
        ]
        temp_map = {}
        string_literals = {}

        for instr in tac_code:
            if isinstance(instr, TACOperation):
                if instr.result not in temp_map:
                    if instr.data_type in (FLOAT_TYPE, "float"):
                        temp_map[instr.result] = f"$f{len(temp_map)}"  # Para operaciones flotantes
                    else:
                        temp_map[instr.result] = f"$t{len(temp_map)}"  # Para operaciones enteras y booleanas

                result_reg = temp_map[instr.result]

                temp1 = self.new_temp()
                temp2 = self.new_temp()
                arg1_reg = ''
                arg2_reg = ''

                if instr.data_type in (FLOAT_TYPE, "float"):
                    temp_map[temp1] = f"$f{len(temp_map)}"  # Para operaciones flotantes
                    temp_map[temp2] = f"$f{len(temp_map)}"
                    arg1_reg = temp_map[temp1]
                    arg2_reg = temp_map[temp2]
                    text_section.append(f"    li {arg1_reg}, {instr.arg1}")
                    text_section.append(f"    li {arg2_reg}, {instr.arg2}")
                else:
                    temp_map[temp1] = f"$t{len(temp_map)}"  # Para operaciones flotantes
                    temp_map[temp2] = f"$t{len(temp_map)}"
                    arg1_reg = temp_map[temp1]
                    arg2_reg = temp_map[temp2]
                    text_section.append(f"    li {arg1_reg}, {instr.arg1}")
                    text_section.append(f"    li {arg2_reg}, {instr.arg2}")


                if instr.data_type in (FLOAT_TYPE, "float"):
                    # Operaciones aritméticas con flotantes
                    if instr.operation == '+':
                        text_section.append(f"    add.s {result_reg}, {arg1_reg}, {arg2_reg}")
                    elif instr.operation == '-':
                        text_section.append(f"    sub.s {result_reg}, {arg1_reg}, {arg2_reg}")
                    elif instr.operation == '*':
                        text_section.append(f"    mul.s {result_reg}, {arg1_reg}, {arg2_reg}")
                    elif instr.operation == '/':
                        text_section.append(f"    div.s {result_reg}, {arg1_reg}, {arg2_reg}")
                else:
                    # Operaciones aritméticas con enteros
                    if instr.operation == '+':
                        text_section.append(f"    add {result_reg}, {arg1_reg}, {arg2_reg}")
                    elif instr.operation == '-':
                        text_section.append(f"    sub {result_reg}, {arg1_reg}, {arg2_reg}")
                    elif instr.operation == '*':
                        text_section.append(f"    mul {result_reg}, {arg1_reg}, {arg2_reg}")
                    elif instr.operation == '/':
                        text_section.append(f"    div {result_reg}, {arg1_reg}")
                        text_section.append(f"    mflo {result_reg}")

                # Operaciones lógicas y comparativas (enteros y booleanos)
                if instr.operation == '&&':
                    text_section.append(f"    and {result_reg}, {arg1_reg}, {arg2_reg}")
                elif instr.operation == '||':
                    text_section.append(f"    or {result_reg}, {arg1_reg}, {arg2_reg}")
                elif instr.operation == '==':
                    if instr.data_type in (FLOAT_TYPE, "float"):
                        text_section.append(f"    c.eq.s {arg1_reg}, {arg2_reg}")
                        text_section.append(f"    bc1t label_eq_true_{instr.result}")
                        text_section.append(f"    li {result_reg}, 0")
                        text_section.append(f"    j label_eq_end_{instr.result}")
                        text_section.append(f"label_eq_true_{instr.result}:")
                        text_section.append(f"    li {result_reg}, 1")
                        text_section.append(f"label_eq_end_{instr.result}:")
                    else:
                        text_section.append(f"    seq {result_reg}, {arg1_reg}, {arg2_reg}")
                elif instr.operation == '!=':
                    if instr.data_type in (FLOAT_TYPE, "float"):
                        text_section.append(f"    c.eq.s {arg1_reg}, {arg2_reg}")
                        text_section.append(f"    bc1t label_ne_false_{instr.result}")
                        text_section.append(f"    li {result_reg}, 1")
                        text_section.append(f"    j label_ne_end_{instr.result}")
                        text_section.append(f"label_ne_false_{instr.result}:")
                        text_section.append(f"    li {result_reg}, 0")
                        text_section.append(f"label_ne_end_{instr.result}:")
                    else:
                        text_section.append(f"    sne {result_reg}, {arg1_reg}, {arg2_reg}")
                elif instr.operation == '>':
                    if instr.data_type in (FLOAT_TYPE, "float"):
                        text_section.append(f"    c.le.s {arg2_reg}, {arg1_reg}")
                        text_section.append(f"    bc1t label_gt_true_{instr.result}")
                        text_section.append(f"    li {result_reg}, 0")
                        text_section.append(f"    j label_gt_end_{instr.result}")
                        text_section.append(f"label_gt_true_{instr.result}:")
                        text_section.append(f"    li {result_reg}, 1")
                        text_section.append(f"label_gt_end_{instr.result}:")
                    else:
                        text_section.append(f"    sgt {result_reg}, {arg1_reg}, {arg2_reg}")
                elif instr.operation == '<':
                    if instr.data_type in (FLOAT_TYPE, "float"):
                        text_section.append(f"    c.lt.s {arg1_reg}, {arg2_reg}")
                        text_section.append(f"    bc1t label_lt_true_{instr.result}")
                        text_section.append(f"    li {result_reg}, 0")
                        text_section.append(f"    j label_lt_end_{instr.result}")
                        text_section.append(f"label_lt_true_{instr.result}:")
                        text_section.append(f"    li {result_reg}, 1")
                        text_section.append(f"label_lt_end_{instr.result}:")
                    else:
                        text_section.append(f"    slt {result_reg}, {arg1_reg}, {arg2_reg}")
                elif instr.operation == '>=':
                    if instr.data_type in (FLOAT_TYPE, "float"):
                        text_section.append(f"    c.lt.s {arg1_reg}, {arg2_reg}")
                        text_section.append(f"    bc1t label_ge_false_{instr.result}")
                        text_section.append(f"    li {result_reg}, 1")
                        text_section.append(f"    j label_ge_end_{instr.result}")
                        text_section.append(f"label_ge_false_{instr.result}:")
                        text_section.append(f"    li {result_reg}, 0")
                        text_section.append(f"label_ge_end_{instr.result}:")
                    else:
                        text_section.append(f"    sge {result_reg}, {arg1_reg}, {arg2_reg}")
                elif instr.operation == '<=':
                    if instr.data_type in (FLOAT_TYPE, "float"):
                        text_section.append(f"    c.le.s {arg1_reg}, {arg2_reg}")
                        text_section.append(f"    bc1t label_le_true_{instr.result}")
                        text_section.append(f"    li {result_reg}, 0")
                        text_section.append(f"    j label_le_end_{instr.result}")
                        text_section.append(f"label_le_true_{instr.result}:")
                        text_section.append(f"    li {result_reg}, 1")
                        text_section.append(f"label_le_end_{instr.result}:")
                    else:
                        text_section.append(f"    sle {result_reg}, {arg1_reg}, {arg2_reg}")

            elif isinstance(instr, TACFunctionCall):
                temp_var = temp_map.get(instr.result, instr.result)
                if instr.function_name == 'rand':
                    text_section.append(f"    li {temp_var}, 42")  # Placeholder for random function
                else:
                    arg1_reg = temp_map.get(instr.args[0], instr.args[0])
                    if len(instr.args) > 1:
                        arg2_reg = temp_map.get(instr.args[1], instr.args[1])
                        text_section.append(f"    {instr.function_name} {temp_var}, {arg1_reg}, {arg2_reg}")
                    else:
                        text_section.append(f"    {instr.function_name} {temp_var}, {arg1_reg}")

            elif isinstance(instr, TACPrint):
                arg = instr.arg
                if instr.data_type in (FLOAT_TYPE, "float"):
                    text_section.append(f"    li $v0, 2")  # Syscall for printing float
                    if arg in temp_map:
                        arg_reg = temp_map[arg]
                        text_section.append(f"    mov.s $f12, {arg_reg}")
                    else:
                        if arg in ('PI', 'E'):
                            text_section.append(f"    l.s $f12, {arg}")
                        else:
                            temp_var = self.new_temp()
                            mips_code.append(f"{temp_var}: .float {arg}")
                            text_section.append(f"    l.s $f12, {temp_var}")
                    text_section.append(f"    syscall")
                elif instr.data_type in (INT_TYPE, "int"):
                    text_section.append(f"    li $v0, 1")  # Syscall for printing integer
                    if arg in temp_map:
                        arg_reg = temp_map[arg]
                        text_section.append(f"    move $a0, {arg_reg}")
                    else:
                        text_section.append(f"    li $a0, {arg}")
                    text_section.append(f"    syscall")
                elif instr.data_type in (STRING_TYPE, "string"):
                    if arg not in string_literals:
                        string_label = f"str_{len(string_literals)}"
                        string_literals[arg] = string_label
                        mips_code.append(f"{string_label}: .asciiz \"{arg}\"")
                    string_label = string_literals[arg]
                    text_section.append(f"    li $v0, 4")  # Syscall for printing string
                    text_section.append(f"    la $a0, {string_label}")
                    text_section.append(f"    syscall")
                elif instr.data_type in (BOOL_TYPE, "bool"):
                    bool_value = 1 if arg == 'true' else 0
                    text_section.append(f"    li $v0, 1")  # Syscall for printing integer
                    text_section.append(f"    li $a0, {bool_value}")
                    text_section.append(f"    syscall")

            elif isinstance(instr, TACConcat):
                arg1_reg = temp_map.get(instr.arg1, instr.arg1)
                arg2_reg = temp_map.get(instr.arg2, instr.arg2)
                result_reg = temp_map.get(instr.result, instr.result)
                text_section.append(f"    concat {result_reg}, {arg1_reg}, {arg2_reg}")

        return mips_code + text_section

    def new_temp(self):
        self.temp_count += 1
        return f"temp_{self.temp_count}"
