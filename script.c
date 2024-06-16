#include <math.h>
double tan(double x) {
    return (sin(x) / cos(x));
}
double cot(double x) {
    return (1 / tan(x));
}
#include <stdio.h>
int main() {
    ;
    ;
    printf("%f\n", ((tan((3.141592653589793 / 4)) * tan((3.141592653589793 / 4))) + (cot((3.141592653589793 / 4)) * cot((3.141592653589793 / 4)))));;
    return 0;
}
