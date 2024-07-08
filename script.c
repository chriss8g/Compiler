#define PI  3.141592
#define E 2.71828
#include <stdio.h>


int main(){ 
int local__internal_0;
int local__internal_1;
local__internal_0 = function_block_1();
local__internal_1 = function_block_2();
return 0;
}
int function_block_1(){ 
int local_block_1_internal_0;
int local_block_1_internal_1;
int local_block_1_internal_2;
local_block_1_internal_1 = 7;
local_block_1_internal_0 = local_block_1_internal_1;
local_block_1_internal_2 = printf("%d\n", local_block_1_internal_0);

return local_block_1_internal_2;
}
int function_block_2(){ 
int local_block_2_internal_0;
int local_block_2_internal_1;
int local_block_2_internal_2;
local_block_2_internal_1 = 20;
local_block_2_internal_0 = local_block_2_internal_1;
local_block_2_internal_2 = printf("%d\n", local_block_2_internal_0);

return local_block_2_internal_2;
}