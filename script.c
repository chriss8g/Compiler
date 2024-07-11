#define PI 3.141592
#define E 2.71828
#include <stdio.h>

int main();
float function_let_1(float param_a_0);
float function_let_2(float param_param_a_0_0, float param_b_1);
float function_let_3(float param_param_param_a_0_0_0, float param_param_b_1_1, float param_c_2);

int main()
{
    float local__internal_0;
    float local__internal_1;
    local__internal_0 = 5;
    local__internal_1 = function_let_1(local__internal_0);
    return 0;
}
float function_let_1(float param_a_0)
{
    float local_let_1_internal_0;
    float local_let_1_internal_1;
    float local_let_1_internal_2;
    local_let_1_internal_0 = param_a_0;
    local_let_1_internal_1 = 10;
    local_let_1_internal_2 = function_let_2(local_let_1_internal_0, local_let_1_internal_1);
    return local_let_1_internal_2;
}
float function_let_2(float param_param_a_0_0, float param_b_1)
{
    float local_let_2_internal_0;
    float local_let_2_internal_1;
    float local_let_2_internal_2;
    float local_let_2_internal_3;
    local_let_2_internal_0 = param_param_a_0_0;
    local_let_2_internal_1 = param_b_1;
    local_let_2_internal_2 = 20;
    local_let_2_internal_3 = function_let_3(local_let_2_internal_0, local_let_2_internal_1, local_let_2_internal_2);
    return local_let_2_internal_3;
}
float function_let_3(float param_param_param_a_0_0_0, float param_param_b_1_1, float param_c_2)
{
    float local_let_3_internal_0;
    float local_let_3_internal_1;
    float local_let_3_internal_2;
    float local_let_3_internal_3;
    int local_let_3_internal_4;
    float local_let_3_internal_5;
    int local_let_3_internal_6;
    float local_let_3_internal_7;
    int local_let_3_internal_8;
    local_let_3_internal_0 = param_param_param_a_0_0_0;
    local_let_3_internal_1 = param_param_b_1_1;
    local_let_3_internal_2 = param_c_2;
    local_let_3_internal_3 = local_let_3_internal_0 + local_let_3_internal_1;
    local_let_3_internal_4 = printf("%.6g\n", local_let_3_internal_3);

    local_let_3_internal_5 = local_let_3_internal_1 * local_let_3_internal_2;
    local_let_3_internal_6 = printf("%.6g\n", local_let_3_internal_5);

    local_let_3_internal_7 = local_let_3_internal_2 / local_let_3_internal_0;
    local_let_3_internal_8 = printf("%.6g\n", local_let_3_internal_7);

    return local_let_3_internal_7;
}