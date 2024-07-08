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
int local_block_1_internal_3;
int local_block_1_internal_4;
int local_block_1_internal_5;
local_block_1_internal_1 = 6;
local_block_1_internal_0 = local_block_1_internal_1;
local_block_1_internal_3 = 7;
local_block_1_internal_4 = local_block_1_internal_0 * local_block_1_internal_3;
local_block_1_internal_2 = local_block_1_internal_4;
local_block_1_internal_5 = printf("%d\n", local_block_1_internal_2);

return local_block_1_internal_5;
}
int function_block_2(){ 
int local_block_2_internal_0;
int local_block_2_internal_1;
int local_block_2_internal_2;
int local_block_2_internal_3;
int local_block_2_internal_4;
int local_block_2_internal_5;
int local_block_2_internal_6;
int local_block_2_internal_7;
int local_block_2_internal_8;
int local_block_2_internal_9;
int local_block_2_internal_10;
int local_block_2_internal_11;
local_block_2_internal_1 = 5;
local_block_2_internal_0 = local_block_2_internal_1;
local_block_2_internal_3 = 10;
local_block_2_internal_2 = local_block_2_internal_3;
local_block_2_internal_5 = 20;
local_block_2_internal_4 = local_block_2_internal_5;
local_block_2_internal_6 = local_block_2_internal_0 + local_block_2_internal_2;
local_block_2_internal_7 = printf("%d\n", local_block_2_internal_6);

local_block_2_internal_8 = local_block_2_internal_2 * local_block_2_internal_4;
local_block_2_internal_9 = printf("%d\n", local_block_2_internal_8);

local_block_2_internal_10 = local_block_2_internal_4 / local_block_2_internal_0;
local_block_2_internal_11 = printf("%d\n", local_block_2_internal_10);

return local_block_2_internal_11;
}