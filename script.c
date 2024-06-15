#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
int main() {
    printf("%d\n", 5);
    printf("%f\n", (3.141592653589793 + 2.718281828459045));
    printf("%f\n", sin((3.141592653589793 / 2)));
    printf("%f\n", (3 + (4.5 * 10)));
    printf("%f\n", ((3 + 4) * 10.5));
    printf("%d\n", ((1 && 0) || 1));
    printf("%d\n", (3.0 >= 2));
    char temp_1[16] = "Hello";
    char temp_2[9] = " World!";
    strcat(temp_1, temp_2);
    printf("%s\n", temp_1);
    printf("%f\n", log(10) / log(100));
    printf("%f\n", (double)rand() / RAND_MAX);
    printf("%f\n", (3.14 + 2.71));
    printf("%d\n", (5 == 5));
    printf("%d\n", (10 != 20));
    printf("%f\n", sqrt(4));
    printf("%f\n", exp(1));
    printf("%f\n", (4 / 2.0));
    printf("%d\n", (10 - 5));
    printf("%d\n", 1);
    printf("%d\n", 0);
    printf("%f\n", (sin(3.141592653589793) + cos(2.718281828459045)));
    return 0;
}
