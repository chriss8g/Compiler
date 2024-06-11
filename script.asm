.data
PI: .float 3.141592653589793
E: .float 2.718281828459045
.text
main:
    l.s $f1, PI
    l.s $f2, E
    add.s $t0, $f1, $f2
    li $v0, 4
    la $a0, $t0
    syscall
