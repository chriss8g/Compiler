#include <stdio.h>

int main(){ 
int local__internal_0;

local__internal_0 = function_block_1();
return 0;
 }
    int function_block_1(){ 
int local_block_1_internal_0;
int local_block_1_internal_1;
int local_block_1_internal_2;
int local_block_1_internal_3;
int local_block_1_internal_4;
int local_block_1_internal_5;

local_block_1_internal_1 = 10;
local_block_1_internal_0 = local_block_1_internal_1;
local_block_1_internal_2 = 10;
local_block_1_internal_3 = local_block_1_internal_0 == local_block_1_internal_2;
goto my_begin;
my_if:
local_block_1_internal_4 = 3;
local_block_1_internal_5 = local_block_1_internal_0 + local_block_1_internal_4;
printf("%d\n", local_block_1_internal_5);

goto my_end;
my_else:
printf("%d\n", local_block_1_internal_0);

goto my_end;
my_begin:
if( local_block_1_internal_3) 
	goto my_if;
 else 
	goto my_else;

my_end:
return ;
 }