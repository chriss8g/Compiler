#define PI 3.141592
#define E 2.71828
#include <stdio.h>

int main()
{
    int local__internal_0;
    local__internal_0 = function_block_1();
    return 0;
}
int function_block_1()
{
    int local_block_1_internal_0;
    int local_block_1_internal_1;
    int local_block_1_internal_2;
    int local_block_1_internal_3;
    int local_block_1_internal_4;
    int local_block_1_internal_5;
    int local_block_1_internal_6;
    local_block_1_internal_1 = 10;
    local_block_1_internal_0 = local_block_1_internal_1;
    goto while_label;
body:
    local_block_1_internal_2 = printf("%d\n", local_block_1_internal_0);

    local_block_1_internal_3 = 1;
    local_block_1_internal_4 = local_block_1_internal_0 - local_block_1_internal_3;
    local_block_1_internal_0 = local_block_1_internal_4;
while_label:
    local_block_1_internal_5 = 0;
    local_block_1_internal_6 = local_block_1_internal_0 >= local_block_1_internal_5;
    if (local_block_1_internal_6)
        goto body;
    else
        goto endwhile_label;

endwhile_label:
    return;
}