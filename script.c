#define PI  3.141592
#define E 2.71828
#include <stdio.h>



int main(){ 
int local__internal_0;
int local__internal_1;
local__internal_0 = 0;
local__internal_1 = function_block_1(local__internal_0);
return 0;
}
int function_block_1(int a){ 
int local_block_1_internal_0;
int local_block_1_internal_1;
int local_block_1_internal_2;
int local_block_1_internal_3;
local_block_1_internal_0 = a;
local_block_1_internal_1 = printf("%d\n", local_block_1_internal_0);

local_block_1_internal_2 = 1;
local_block_1_internal_0 = local_block_1_internal_2;
local_block_1_internal_3 = printf("%d\n", local_block_1_internal_0);

return local_block_1_internal_3;
}