#define PI 3.141592
#define E 2.71828
#include <stdio.h>

#define data_0 "42"
int main(char *number)
{
    char *local__internal_0;
    char *local__internal_1;
    local__internal_0 = data_0;
    local__internal_1 = function_block_1(local__internal_0);
    return 0;
}
int function_block_1(char *number)
{
    char *local_block_1_internal_0;
    char *local_block_1_internal_1;
    local_block_1_internal_0 = number;
    local_block_1_internal_1 = printf("%s\n", local_block_1_internal_0);

    return local_block_1_internal_1;
}