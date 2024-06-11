class MipsCodeGenerator:

    def generate_mips_code(self, tac_code):
        mips_code = [
            ".data",
            "PI: .float 3.141592653589793",
            "E: .float 2.718281828459045",
            ".text",
            "main:"
        ]
        temp_map = {}

        for instr in tac_code:
            if instr.result not in temp_map:
                temp_map[instr.result] = f"$t{len(temp_map)}"

            result_reg = temp_map[instr.result]

            if instr.arg1 in temp_map:
                arg1_reg = temp_map[instr.arg1]
            else:
                arg1_reg = instr.arg1

            if instr.arg2 in temp_map:
                arg2_reg = temp_map[instr.arg2]
            else:
                arg2_reg = instr.arg2

            if instr.operation == '+':
                mips_code.append(f"    l.s $f1, {arg1_reg}")
                mips_code.append(f"    l.s $f2, {arg2_reg}")
                mips_code.append(f"    add.s {result_reg}, $f1, $f2")
            elif instr.operation == '-':
                mips_code.append(f"    l.s $f1, {arg1_reg}")
                mips_code.append(f"    l.s $f2, {arg2_reg}")
                mips_code.append(f"    sub.s {result_reg}, $f1, $f2")
            elif instr.operation == '*':
                mips_code.append(f"    l.s $f1, {arg1_reg}")
                mips_code.append(f"    l.s $f2, {arg2_reg}")
                mips_code.append(f"    mul.s {result_reg}, $f1, $f2")
            elif instr.operation == '/':
                mips_code.append(f"    l.s $f1, {arg1_reg}")
                mips_code.append(f"    l.s $f2, {arg2_reg}")
                mips_code.append(f"    div.s {result_reg}, $f1, $f2")
            elif instr.operation == '&&':
                mips_code.append(f"    and {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '||':
                mips_code.append(f"    or {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '==':
                mips_code.append(f"    seq {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '!=':
                mips_code.append(f"    sne {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '>':
                mips_code.append(f"    sgt {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '<':
                mips_code.append(f"    slt {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '>=':
                mips_code.append(f"    sge {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '<=':
                mips_code.append(f"    sle {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == 'rand':
                mips_code.append(f"    li {result_reg}, 42")  # Placeholder for random function
            elif instr.operation == '@':
                mips_code.append(f"    concat {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == 'print':
                print(instr.arg1)
                if instr.arg1 in ('PI', 'E') or instr.arg1.startswith('$f'):
                    mips_code.append(f"    li $v0, 2")  # Syscall for printing float
                    mips_code.append(f"    mov.s $f12, {arg1_reg}")
                    mips_code.append(f"    syscall")
                elif instr.arg1.startswith('$t') or instr.arg1.isdigit():
                    mips_code.append(f"    li $v0, 1")  # Syscall for printing integer
                    mips_code.append(f"    move $a0, {arg1_reg}")
                    mips_code.append(f"    syscall")
                elif instr.arg1 in ('true', 'false'):
                    bool_value = 1 if instr.arg1 == 'true' else 0
                    mips_code.append(f"    li $v0, 1")  # Syscall for printing integer
                    mips_code.append(f"    li $a0, {bool_value}")
                    mips_code.append(f"    syscall")
                else:
                    mips_code.append(f"    li $v0, 4")  # Syscall for printing string
                    mips_code.append(f"    la $a0, {arg1_reg}")
                    mips_code.append(f"    syscall")

        return mips_code
