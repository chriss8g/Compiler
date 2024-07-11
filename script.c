#define PI 3.141592
#define E 2.71828
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    float a;
} MyClass;

float function_method_at_MyClass();
int main();
MyClass *function_let_2(MyClass *param_a_0);

float function_method_at_MyClass()
{
    float local_method_at_MyClass_internal_0;
    int local_method_at_MyClass_internal_1;
    local_method_at_MyClass_internal_0 = 2;
    local_method_at_MyClass_internal_1 = printf("%.6g\n", local_method_at_MyClass_internal_0);

    return local_method_at_MyClass_internal_0;
}
int main()
{
    MyClass *local__internal_0;
    float local__internal_1;
    local__internal_0 = malloc(sizeof(MyClass));

    local__internal_1 = function_let_2(local__internal_0);
    return 0;
}
MyClass *function_let_2(MyClass *param_a_0)
{
    MyClass *local_let_2_internal_0;
    local_let_2_internal_0 = param_a_0;
    return function_method_at_MyClass();
}