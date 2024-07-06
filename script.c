#define PI  3.141592
#define E 2.71828
#include <stdio.h>

int main(){ 
float local__internal_0;

local__internal_0 = function_block_1();
return 0;
 }
    int function_block_1(){ 
float local_block_1_internal_0;
float local_block_1_internal_1;
float local_block_1_internal_2;
float local_block_1_internal_3;
float local_block_1_internal_4;
float local_block_1_internal_5;
float local_block_1_internal_6;
float local_block_1_internal_7;

local_block_1_internal_1 = 10 * 1.0;
local_block_1_internal_0 = local_block_1_internal_1 * 1.0;
local_block_1_internal_2 = 10 * 1.0;
local_block_1_internal_3 = local_block_1_internal_0 == local_block_1_internal_2 * 1.0;
goto my_begin;
my_if:
local_block_1_internal_4 = 3 * 1.0;
local_block_1_internal_5 = local_block_1_internal_0 + local_block_1_internal_4 * 1.0;
local_block_1_internal_6 = printf("%f\n", local_block_1_internal_5);

goto my_end;
my_else:
local_block_1_internal_7 = printf("%f\n", local_block_1_internal_0);

goto my_end;
my_begin:
if( local_block_1_internal_3) 
	goto my_if;
 else 
	goto my_else;

my_end:
return ;
 }