#include <stdio.h>

int main()
{
    int local__internal_0;

    local__internal_0 = function_block_1();
    ;
    return 0;
    ;
}
int function_block_1()
{
    int local_block_1_internal_0;
    int local_block_1_internal_1;
    int local_block_1_internal_2;
    int local_block_1_internal_3;

    local_block_1_internal_1 = 5;
    local_block_1_internal_0 = local_block_1_internal_1;
    local_block_1_internal_2 = 10;
    local_block_1_internal_3 = local_block_1_internal_0 == local_block_1_internal_2;
    if (local_block_1_internal_3)
        function_block_2();
    else
        function_block_3();
    ;
    return;
    ;
}
int function_block_2()
{
    int local_block_2_internal_0;
    int local_block_2_internal_1;

    local_block_2_internal_0 = 3;
    local_block_2_internal_1 = local_block_1_internal_0 + local_block_2_internal_0;
    printf("%d\n", local_block_2_internal_1);
    ;
    return 0;
    ;
}
int function_block_3()
{

    printf("%d\n", local_block_1_internal_0);
    ;
    return 0;
    ;
}