#define PI 3.141592
#define E 2.71828
#include <stdio.h>
#include <stdlib.h>
float function_method_at_MyClass();
int main();
MyClass *function_let_2(MyClass *a);

typedef struct
{
    float a;
} MyClass;

float function_method_at_MyClass()
{
    float local_method_at_MyClass_internal_0;
    int local_method_at_MyClass_internal_1;
    local_method_at_MyClass_internal_0 = 2;
    local_method_at_MyClass_internal_1 = printf("%f\n", local_method_at_MyClass_internal_0);

    return local_method_at_MyClass_internal_0;
}
int main()
{
    MyClass *local__internal_0;
    MyClass *local__internal_1;
    local__internal_0 = malloc(sizeof(MyClass));

    local__internal_1 = function_let_2(local__internal_0);
    return 0;
}
MyClass *function_let_2(MyClass *a)
{
    MyClass *local_let_2_internal_0;
    local_let_2_internal_0 = a;
    return function_method_at_MyClass();
}