#define PI 3.141592
#define E 2.71828
#include <stdio.h>

int main();
float function_let_1(float a);
float function_let_2(float a, float b);

int main()
{
    float local__internal_0;
    float local__internal_1;
    local__internal_0 = 0;
    local__internal_1 = function_let_1(local__internal_0);
    return 0;
}
float function_let_1(float a)
{
    float local_let_1_internal_0;
    float local_let_1_internal_1;
    float local_let_1_internal_2;
    local_let_1_internal_0 = a;
    local_let_1_internal_1 = 1;
    local_let_1_internal_0 = local_let_1_internal_1;
    local_let_1_internal_2 = function_let_2(local_let_1_internal_0, local_let_1_internal_1);
    return local_let_1_internal_2;
}
float function_let_2(float a, float b)
{
    float local_let_2_internal_0;
    float local_let_2_internal_1;
    int local_let_2_internal_2;
    int local_let_2_internal_3;
    local_let_2_internal_0 = a;
    local_let_2_internal_1 = b;
    local_let_2_internal_2 = printf("%.6g\n", local_let_2_internal_0);

    local_let_2_internal_3 = printf("%.6g\n", local_let_2_internal_1);

    return local_let_2_internal_1;
}