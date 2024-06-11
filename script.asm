.data
PI: .float 3.141592653589793
E: .float 2.718281828459045
.text
main:
    add.s $f0, PI, E
    div.s $f1, PI, 2
    mul.s $f3, 4.5, 10
    add.s $f4, 3, $f3
    add.s $f5, 3, 4
    mul.s $f6, $f5, 10.5
    and $f7, true, false
    or $f8, $f7, true
    sge $f9, 3.0, 2
    concat $f10, Hello,  World!
    li $f12, 42
    add.s $f13, 3.14, 2.71
    seq $f14, 5, 5
    sne $f15, 10, 20
    div.s $f18, 4, 2.0
    sub.s $f19, 10, 5
    add.s $f22, $f20, $f21
