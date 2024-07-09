#define PI  3.141592
#define E 2.71828
#include <stdio.h>



int main(){ 
int local__internal_0;
int local__internal_1;
int local__internal_2;
int local__internal_3;
local__internal_0 = 6;
local__internal_1 = function_block_1(local__internal_0);
local__internal_2 = 5;
local__internal_3 = function_block_3(local__internal_2);
return 0;
}
int function_block_1(int a){ 
int local_block_1_internal_0;
int local_block_1_internal_1;
int local_block_1_internal_2;
int local_block_1_internal_3;
local_block_1_internal_0 = a;
local_block_1_internal_1 = 7;
local_block_1_internal_2 = local_block_1_internal_0 * local_block_1_internal_1;
local_block_1_internal_3 = function_block_2(a, local_block_1_internal_2);
return local_block_1_internal_3;
}
int function_block_2(int a, int b){ 
int local_block_2_internal_0;
int local_block_2_internal_1;
int local_block_2_internal_2;
local_block_2_internal_0 = a;
local_block_2_internal_1 = b;
local_block_2_internal_2 = printf("%d\n", local_block_2_internal_1);

return local_block_2_internal_2;
}
int function_block_3(int a){ 
int local_block_3_internal_0;
int local_block_3_internal_1;
int local_block_3_internal_2;
local_block_3_internal_0 = a;
local_block_3_internal_1 = 10;
local_block_3_internal_2 = function_block_4(a, local_block_3_internal_1);
return local_block_3_internal_2;
}
int function_block_4(int a, int b){ 
int local_block_4_internal_0;
int local_block_4_internal_1;
int local_block_4_internal_2;
int local_block_4_internal_3;
local_block_4_internal_0 = a;
local_block_4_internal_1 = b;
local_block_4_internal_2 = 20;
local_block_4_internal_3 = function_block_5(a, b, local_block_4_internal_2);
return local_block_4_internal_3;
}
int function_block_5(int a, int b, int c){ 
int local_block_5_internal_0;
int local_block_5_internal_1;
int local_block_5_internal_2;
int local_block_5_internal_3;
int local_block_5_internal_4;
int local_block_5_internal_5;
int local_block_5_internal_6;
int local_block_5_internal_7;
int local_block_5_internal_8;
local_block_5_internal_0 = a;
local_block_5_internal_1 = b;
local_block_5_internal_2 = c;
local_block_5_internal_3 = local_block_5_internal_0 + local_block_5_internal_1;
local_block_5_internal_4 = printf("%d\n", local_block_5_internal_3);

local_block_5_internal_5 = local_block_5_internal_1 * local_block_5_internal_2;
local_block_5_internal_6 = printf("%d\n", local_block_5_internal_5);

local_block_5_internal_7 = local_block_5_internal_2 / local_block_5_internal_0;
local_block_5_internal_8 = printf("%d\n", local_block_5_internal_7);

return local_block_5_internal_8;
}